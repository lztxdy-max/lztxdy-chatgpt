from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

import os
from langchain.memory import ConversationBufferMemory
import httpx
http_client = httpx.Client(
        base_url=os.getenv("OPENAI_API_BASE"),
        follow_redirects=True,
    )


def get_chat_response(prompt, memory, openai_api_key):
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key,
                       openai_api_base=os.getenv("OPENAI_API_BASE"),
                       http_client=http_client)
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]


text = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("沈从文的作品有那些？", text, os.getenv("OPENAI_API_KEY")))
# print(get_chat_response("我上一个问题是什么？", text, os.getenv("OPENAI_API_KEY")))
