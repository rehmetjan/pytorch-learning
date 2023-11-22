"""ChatGPG sample code using OPENAI API."""
import openai

openai.api_key = 'sk-eOg4nqGPuSDpHMmXMkUqT3BlbkFJOGnl7CdcGuXDICD7Ihca3'

response = openai.Completion.create(
    engine="text-davinci-003",  # 或者使用其他可用的引擎
    prompt="openAI是什么时候成立的？",
    max_tokens=150
)

print(response['choices'][0]['text'])
