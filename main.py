from openai import OpenAI

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("NVIDIA_API_KEY")

MODEL = "nvidia/nemotron-3-ultra-550b-a55b"


client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = api_key
)

def call_api():
    print("calling client...")

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role":"system","content":"You are a helpful assistant."},
            {"role":"user","content":"Write a limerick about the wonders of GPU computing."}
        ],
        temperature=1,
        top_p=0.95,
        max_tokens=16384,
        extra_body={"chat_template_kwargs":{"enable_thinking":False}},
        stream=False
    )
    print(completion.choices[0].message)

if __name__ == "__main__":
    call_api()
