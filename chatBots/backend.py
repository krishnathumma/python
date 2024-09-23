import openai


class Chatbot:
    def __init__(self):
       openai.api_key = "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"

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
