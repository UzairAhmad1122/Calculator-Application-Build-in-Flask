from flask import Flask, render_template, request, jsonify
import webbrowser
from threading import Timer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data.get('expression', '')
        
        # Security check: restrict allowed characters
        allowed_chars = set("0123456789+-*/.() ")
        if not set(expression).issubset(allowed_chars):
            return jsonify({'error': 'Invalid Input'}), 400

        # Evaluate the mathematical expression
        result = eval(expression)
        return jsonify({'result': result})

    except Exception:
        return jsonify({'error': 'Error'}), 400

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    # Delay opening the browser by 1 second to allow the Flask server to start
    Timer(1, open_browser).start()
    app.run(debug=True)