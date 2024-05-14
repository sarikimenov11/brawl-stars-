from flask import Flask, request
import requests

app = Flask(__name__)

# Замените на ваш токен бота и ID чата
BOT_TOKEN = '6932562913:AAE9pFMoVYeUzUfZtTtuWY2z9OaOYJ7l3CU'
CHAT_ID = '5682662110'

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/send-location', methods=['POST'])
def send_location():
    data = request.get_json()
    location = data['location']
    send_message_to_telegram(location)
    return {'message': 'Location sent to Telegram bot'}

def send_message_to_telegram(message):
    telegram_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': message}
    response = requests.post(telegram_url, json=payload)
    if response.status_code != 200:
        print(f'Error sending message to Telegram: {response.text}')

if __name__ == '__main__':
    app.run(debug=True)
