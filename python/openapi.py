import os
import requests

base_url = os.getenv('OPENAI_BASE_URL')
if not base_url:
    base_url = 'https://api.openai.com/v1'

openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("No OPENAI_API_KEY set")

def generate_text(prompt):
    headers = {
        'Authorization': f'Bearer {openai_api_key}',
        'Content-Type': 'application/json'
    }

    response = requests.post(
        f'{base_url}/chat/completions',
        headers=headers,
        json={
            'model': 'qwen2.5-coder-1.5b-instruct-q8_0.gguf',
            'messages': [
                {'role': 'user', 'content': prompt}
            ],
            'max_tokens': 100
        }
    )
    response.raise_for_status()
    response_data = response.json()
    return response_data['choices'][0]['message']['content'].strip()

prompt = "Write a short story about a cat in the rain"
generated_text = generate_text(prompt)
print(generated_text)