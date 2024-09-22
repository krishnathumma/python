import openai


class Chatbot:
    def __init__(self):

       
    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=user_input,
            max_tokens=1000,
            temperature=0
        ).choices[0].text

        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about a birds")
    print(response)
