import openai

class Chatbot:
    def __init__(self, api_key):
        openai.api_key = api_key

    def ask_question(self, question):
        response = openai.Completion.create(
            engine='text-davinci-003',  # Specify the model to use, e.g., 'text-davinci-003'
            prompt=question,
            max_tokens=100,  # Set the maximum length of the response
            n=1,  # Number of responses to generate
            stop=None,  # Specify a stop sequence to end the response
            temperature=0.7  # Controls the randomness of the response
        )
        answer = response.choices[0].text.strip()
        return answer

# Example usage
api_key = #Insert API key here****
chatbot = Chatbot(api_key)

while True:
    user_input = input("Griffin: ")
    if user_input.lower() == 'exit':
        break
    response = chatbot.ask_question(user_input)
    print("OpenAI Chatbot :", response)
    
