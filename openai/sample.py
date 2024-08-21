"""ChatGPG sample code using OPENAI API."""
import openai

openai.api_key = 'sk-xxxxxx'  # 请替换为您的API Key

response = openai.Completion.create(
    engine="text-davinci-003",  # 或者使用其他可用的引擎
    prompt="openAI是什么时候成立的？",
    max_tokens=150
)

print(response['choices'][0]['text'])
