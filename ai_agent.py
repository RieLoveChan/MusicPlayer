import openai

class AIAgent:
    def __init__(self):
        self.model = "text-davinci-003"  # GPT model

    def recommend_songs(self, user_query):
        response = openai.Completion.create(
            engine=self.model,
            prompt=f"Recommend songs based on: {user_query}",
            max_tokens=100
        )
        return response.choices[0].text.strip()
