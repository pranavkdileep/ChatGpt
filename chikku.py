import requests

def con(input_value):
    url = 'https://ora.ai/api/conversation'
    headers = {
        'authority': 'ora.ai',
        'accept': '*/*',
        'accept-language': 'en-IN,en;q=0.9',
        'content-type': 'application/json',
        'cookie': '__Host-next-auth.csrf-token=8b8372dd548d04118b010f73b7d28ebf964a0d21801e5db0f9ca745e5045e8fa%7C12e90d18e71d62b84fc03fd55df4bd6a7504fb622ab9ed69c41727512c9432d8; __Secure-next-auth.callback-url=https%3A%2F%2Fora.ai; _ga=GA1.1.623172915.1685004246; _ga_MWL7THFH58=GS1.1.1685004246.1.0.1685004246.0.0.0; __cf_bm=wbZ.aYmAH7N1rczxxmg.TaVQaN.FTBCyc_ABcg5x658-1685004246-0-AUaqgqsRRrqkeSz3dWE1xl5gtsE4w0rKRuYluPZkWotsh2TGklkQwNh0c7DW7qZVwPtaFtVApyNLYQnQowDigKEs0K6O5Ot26VThxoNGbNBV',
        'origin': 'https://ora.ai',
        'referer': 'https://ora.ai/openai/chatgpt',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }

    chatbot_id = '4e67085c-93a2-4f99-a858-288c0600226b'
    user_id = 'auto:1acacac3-3324-4336-8b18-60ea1cee9777'

    data = {
        'chatbotId': chatbot_id,
        'input': input_value,
        'userId': user_id,
        'provider': 'OPEN_AI',
        'config': False,
        'includeHistory': True
    }

    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()

    # Extract and return the response
    response_text = response_data.get('response')
    return response_text


def chatbot():
    print("Bot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        print("Bot: Generating...")
        response = con(user_input)
        
        print("Bot:", response)


# Start the chatbot
chatbot()
