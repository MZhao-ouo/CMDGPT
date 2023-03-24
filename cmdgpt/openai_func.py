from .presets import *

def get_chat_response(prompt, pre_prompt, model="gpt-3.5-turbo-0301", temperature=0):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {cmdgpt_conf['openai_api_key']}"
    }
    payload = {
        "model": model,
        "temperature": temperature,
        "stream": True,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": pre_prompt},
            {"role": "user", "content": prompt}
        ]
    }
    return requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, stream=True)

def decode_chat_response(response):
    for chunk in response.iter_lines():
        if chunk:
            chunk = chunk.decode()
            chunk_length = len(chunk)
            try:
                chunk = json.loads(chunk[6:])
            except json.JSONDecodeError:
                print(f"JSON解析错误。请重置对话。收到的内容: {chunk}")
                continue
            if chunk_length > 6 and "delta" in chunk["choices"][0]:
                if chunk["choices"][0]["finish_reason"] == "stop":
                    break
                try:
                    yield chunk["choices"][0]["delta"]["content"]
                except Exception as e:
                    # logging.error(f"Error: {e}")
                    continue


def get_usage():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {cmdgpt_conf['openai_api_key']}"
    }
    response = requests.get("https://api.openai.com/dashboard/billing/credit_grants", headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        total_used = data['total_used']
        total_granted = data['total_granted']
        print(f"You have used {Fore.YELLOW}{total_used}$/{total_granted}${Style.RESET_ALL}.")
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
