import openai


class Chatbot:
    def __init__(self):
        # openai.api_key = "sk-7nvh_wm0usfCMXcu_uu05DBVbn8qt9VF_5_Vi6tvgfT3BlbkFJ90GNQnBqAzXqn0n_4-qSqeQyrz0Ctn-Vy0Ka7mEiIA"
        # openai.api_key = "sk-75l6u07x73NZZ2H3yQkWqVhG8oSgZDKGSGFNgx69A5T3BlbkFJ5fekpDhaYUlqW_MHIXeXdCTvIevXHlXI3LnramObQA"
        # openai.api_key = "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"
        # openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=user_input,
            max_tokens=7,
            temperature=0
        ).choices[0].text

        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about a birds")
    print(response)
