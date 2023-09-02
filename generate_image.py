from typing import Type
from pydantic import BaseModel, Field
from genai_tool import GenAITool

class GenerateImageSchema(BaseModel):
    prompt: str = Field(..., description="Prompt to generate image")

class GenerateImageTool(GenAITool):
    name: str = "GenAI Image Generator"
    args_schema: Type[BaseModel] = GenerateImageSchema
    description: str = "Generate Image in GenAI system"

    def _execute(self, prompt: str) -> str:
        try:
            data = self.generate("/image", { "prompt": prompt })
            if "image_url" in data:
                image_url = data["image_url"]
                return f"Image generated successfully. Here is the URL: {image_url}"
            else:
                raise Exception("Image URL not found")
        except Exception as err:
            return f"Error: Unable to generate an image {err}"