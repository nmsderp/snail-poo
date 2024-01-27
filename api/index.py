# app.py
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def fetch_and_display_text():
    txt_url = "https://editor.snail-ide.com/poo.txt"

    try:
        response = requests.get(txt_url)
        response.raise_for_status()  # Raise an exception for bad responses
        text_content = response.text
        return jsonify({"text_content": text_content})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
