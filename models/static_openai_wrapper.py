import config
import openai

"""
     This is a simple static wrapper class for the OpenAI API.
     ChatCompletion and Embedding are offered.
"""
class StaticOpenAIModel:

    @staticmethod
    def generate_response(messages, model="gpt-3.5-turbo"):
        #config.logger.debug(f"Entering generate_response with messages: {messages}")
        response_obj = openai.ChatCompletion.create(
            model=model,
            messages=messages,
        )

        return response_obj

    @staticmethod
    def generate_embedding(text, model="text-embedding-ada-002"):
        response = openai.Embedding.create(model=model, input=text)
        embedding = response.data[0].embedding
        return embedding
