import requests
from superagi.tools.base_tool import BaseTool

class GenAITool(BaseTool):
    def generate(self, route, data) -> dict:
        api_host = self.get_tool_config("API_HOST")
        response = requests.post(
            f"{api_host}{route}",
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            json = data,
        )
        return response.json()