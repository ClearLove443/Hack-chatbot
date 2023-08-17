import json
from typing import Any, List, Mapping, Optional

import requests
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM

url = "http://127.0.0.1:13000/chat"
headers = {"Content-Type": "application/json"}


class ChatGLM(LLM):
    @property
    def _llm_type(self) -> str:
        return "custom"

    type = "custom"

    # 重写基类方法，根据用户输入的prompt来响应用户，返回字符串
    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
    ) -> str:
        payload = json.dumps({"q": prompt})
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.text
