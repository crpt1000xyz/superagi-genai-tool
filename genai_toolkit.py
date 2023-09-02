from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from generate_image import GenerateImageTool

class GenAIToolkit(BaseToolkit, ABC):
    name: str = "GenAI Toolkit"
    description: str = "GenAI tool kit contains all tools related to GenAI system"

    def get_tools(self) -> List[BaseTool]:
        return [GenerateImageTool()]

    def get_env_keys(self) -> List[str]:
        return ["API_HOST"]