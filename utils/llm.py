import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models
import json


class LLM:
    def __init__(self, return_json: bool = False):
        vertexai.init(project="kristeligt-dagblad", location="europe-west1")
        self.model = GenerativeModel(
            "gemini-1.5-flash-001",
        )

        self.generation_config = {
            "max_output_tokens": 8192,
            "temperature": 1,
            "top_p": 0.95,
        }

        self.return_json = return_json
        if self.return_json:
            self.generation_config.update({"response_mime_type": "application/json"})

        self.safety_settings = {
            generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        }

    def response_to_json(self, model_response_text: str) -> dict:
        return json.loads(model_response_text.replace("json", "").replace("```", ""))

    def generate(self, input_text: str) -> dict:
        response = self.model.generate_content(
            [input_text],
            generation_config=self.generation_config,
            safety_settings=self.safety_settings,
        )

        if self.return_json:
            return self.response_to_json(
                json.loads(response.candidates[0].content.parts[0].text)
            )
        else:
            return json.loads(response.candidates[0].content.parts[0].text)
