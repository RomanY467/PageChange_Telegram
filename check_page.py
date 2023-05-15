import requests
import time

# Configure the Telegram bot and chat ID
bot_token = '<your_bot_token_here>'
chat_id = '<your_chat_id_here>'

# URL to monitor
url = '<your_url_here>'

# Text to search for on the web page
search_text = '<your_search_text_here>'

# Telegram API endpoint
api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

# Main loop
while True:
    # Send a GET request to the URL
    response = requests.get(url)
    print(response.text)

    # Check if the search text is found on the web page
    if not search_text in response.text:
        # Send a message to the Telegram group
        message = '<your_message_here>'
        data = {'chat_id': chat_id, 'text': message}
        response = requests.post(api_url, data=data)
        print("Found!!!")

    # Wait for 10 seconds before checking again
    time.sleep(10)
