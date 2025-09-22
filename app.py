from flask import Flask, request, jsonify
import sqlite3
import xml.etree.ElementTree as ET
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

def get_response(intent):
    tree = ET.parse('backend/intents.xml')
    root = tree.getroot()
    for item in root.findall('intent'):
        if item.get('name') == intent:
            return item.find('response').text
    return "Sorry, I didn't understand that."

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    lang = request.json['lang']
    translated = translator.translate(user_input, dest='en').text
    response = get_response('greeting') if 'hello' in translated.lower() else get_response('fallback')
    final_response = translator.translate(response, dest=lang).text
    return jsonify({'response': final_response})

if __name__ == '__main__':
    app.run(debug=True)
