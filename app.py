from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import google.generativeai as genai
import os


model = genai.GenerativeModel('gemini-pro')

#model = genai.GenerativeModel('gemini-pro')
my_api_key_gemini = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=my_api_key_gemini)

app = Flask(__name__)
# Explicitly allow CORS for app
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/chat', methods=['POST'])
def chat():
    try:
        message = request.json['message']
        response = model.generate_content(message)
        if response.text:
            return jsonify({"response": response.text})
        else:
            return jsonify({"response": "Sorry, I don't have a response for that."})
    except Exception as e:
        print(f"Exception: {str(e)}")
        return jsonify({"response": "Sorry, something went wrong."})

if __name__ == '__main__':
    creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar.readonly'])
    response = model.generate_content("Why is your api bad")
    print(response)
    #app.run(debug=True)

