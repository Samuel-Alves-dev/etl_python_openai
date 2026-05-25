users = [
  {
    "id": 4,
    "name": "Pyterson",
    "account": {
      "id": 7,
      "number": "00001-1",
      "agency": "0001",
      "balance": 0.0,
      "limit": 500.0
    },
    "card": {
      "id": 4,
      "number": "**** **** **** 1111",
      "limit": 1000.0
    },
    "features": [],
    "news": []
  },
  {
    "id": 5,
    "name": "Pip",
    "account": {
      "id": 8,
      "number": "00002-2",
      "agency": "0001",
      "balance": 0.0,
      "limit": 500.0
    },
    "card": {
      "id": 5,
      "number": "**** **** **** 2222",
      "limit": 1000.0
    },
    "features": [],
    "news": []
  },
  {
    "id": 6,
    "name": "Pep",
    "account": {
      "id": 9,
      "number": "00003-3",
      "agency": "0001",
      "balance": 0.0,
      "limit": 500.0
    },
    "card": {
      "id": 6,
      "number": "**** **** **** 3333",
      "limit": 1000.0
    },
    "features": [],
    "news": []
  }
]

import openai
from openai import OpenAI

sdw_openai_api = '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'

client = OpenAI(api_key=sdw_openai_api)

def generate_ai_news(user):
    try:
        completion = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um especialista em marketing bancário."
                },
                {
                    "role": "user",
                    "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"
                }
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:
        print(f"Erro na API: {e}")
        return f"{user['name']}, investir hoje é construir um futuro mais seguro!"

for user in users:
    news = generate_ai_news(user)
    print(news)
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news
    })
  
print(users)
