from .presets import *
from .openai_func import *
from .utils import *
import shutil, datetime
    
# execute query
def exec_query(query):
    messages = [
            {"role": "system", "content": exec_prompt},
            {"role": "user", "content": prepare_prompt()},
            {"role": "user", "content": query}
        ]
    response = get_chat_response(messages, temperature=0,apiurl=COMPLETIONS_URL)
    response_contents = decode_chat_response(response)
    try_exec(response_contents)

def try_exec(response_contents):
    cmd = ""
    print(f"{Fore.BLUE}CMDGPT:{Style.RESET_ALL} ")
    print("Run(R), Cancel(C)", end="", flush=True)
    print("\x1b[1A\r\x1b[8C", end="")
    for chunk in response_contents:
        print(Fore.YELLOW + chunk + Style.RESET_ALL, end="", flush=True)
        cmd += chunk
    print("\x1b[1B\r\x1b[18C", end="")
    if "MZHAO" in cmd:
        print("\r" + Fore.RED + "Please provide a valuable description." + Style.RESET_ALL)
        return
    if os.name == "nt":
        print("\r" + "Please execute it manually in Windows.")
        return
    if "\n" in cmd:
        print("\r" + "It is a multi-line command. Please execute it manually.")
        return
    while True:
        pressed_key = get_key()
        if pressed_key:
            pressed_key = pressed_key.lower()
            if pressed_key == "r":
                print("\x1b[1A", end="")
                os.system(cmd)
                break
            elif pressed_key == "c":
                print("\rCanceled." + " " * 20)
                break

# set openai api key
def set_openai_key(api_key):
    cmdgpt_conf["openai_api_key"] = api_key
    with open(cmdgpt_conf_path, "w+") as f:
        json.dump(cmdgpt_conf, f)
        
# set openai api url
def set_apihost(apiurl):
    cmdgpt_conf["apiurl"] = apiurl
    with open(cmdgpt_conf_path, "w+") as f:
        json.dump(cmdgpt_conf, f)

# reset configuration
def reset_conf():
    print("Do you want to reset the default configuration? (y/n):")
    while True:
        pressed_key = get_key()
        if pressed_key:
            pressed_key = pressed_key.lower()
            if pressed_key == "y":
                init_conf(cmdgpt_conf_path)
                print("Reset the default configuration.")
                return
            elif pressed_key == "n":
                print("Canceled.")
                return

# Chat with AI
def chat_ai():
    print("Enable chat mode. Press Ctrl+C to exit.")
    terminal_columns = shutil.get_terminal_size().columns
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]
    while True:
        print(f"===== User {(terminal_columns-11) * '='}")
        prompt = input()
        messages.append({"role": "user", "content": prompt})
        print(f"{Fore.YELLOW}===== AI {(terminal_columns-9) * '='}")
        response = get_chat_response(messages, temperature=0.7, apiurl=COMPLETIONS_URL)
        response_contents = decode_chat_response(response)
        answer = ""
        for chunk in response_contents:
            print(chunk, end="", flush=True)
            answer += chunk
        messages.append({"role": "assistant", "content": answer})
        print(Style.RESET_ALL)
        
# Get Credit
def get_credit(credit_url):
    data = get_billing_data(credit_url)
    total_used = data['total_used']
    total_granted = data['total_granted']
    print(f"You have used {Fore.YELLOW}{total_used}$/{total_granted}${Style.RESET_ALL}.")

# Get Usage
def get_usage(usage_url, start_date=None, end_date=None):
    # date的格式是YYYY-MM-DD
    if start_date is None and end_date is None:
        end_date = datetime.datetime.now().strftime("%Y-%m-%d")
        start_date = datetime.datetime.now().replace(day=1).strftime("%Y-%m-%d")
    elif start_date is None:
        start_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    elif end_date is None:
        end_date = datetime.datetime.now().strftime("%Y-%m-%d")
        
    usage_url = usage_url + f"?start_date={start_date}&end_date={end_date}"
    data = get_billing_data(usage_url)
    total_usage = data['total_usage'] / 100
    print(f"You have used {Fore.YELLOW}{total_usage}${Style.RESET_ALL} from {start_date} to {end_date}.")
