MODEL_NAME = "ffm-mixtral-8x7b-32k-instruct"
API_KEY = "{API_KEY}"
API_URL = "{API_URL}"

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

chat_ffm = ChatFormosaFoundationModel(
        base_url = API_URL,
        max_new_tokens = 350,
        temperature = 0.5,
        top_k = 50,
        top_p = 1.0,
        frequence_penalty = 1.0,
        ffm_api_key = API_KEY,
        model = MODEL_NAME
    )

messages = [
    HumanMessage(content="人口最多的國家是?"),
    AIMessage(content="人口最多的國家是印度。"),
    HumanMessage(content="主要宗教為?")
]

result = chat_ffm(messages)
print(result.content)