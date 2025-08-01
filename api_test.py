import openai

openai.api_key = "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"

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Tell me a joke!"}
        ]
    )
    print(response['choices'][0]['message']['content'])
except openai.error.RateLimitError as e:
    print("Rate limit exceeded:", e)
except Exception as e:
    print("Something went wrong:", e)
