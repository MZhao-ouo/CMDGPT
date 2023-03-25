from .presets import *
from .openai_func import *
from .utils import *

# show help
def show_help():
    print("Usage:")
    print("\tcmdgpt <Your Purpose>")
    print("Arguments:")
    print("\t--key:\t set OpenAI api key")
    print("\t--usage:\t get OpenAI usage")
    print("\t--apiurl:\t set OpenAI api url")
    print("\t--reset_conf:\t reset the default configuration")
    print("\t--debug:\t enable debug mode")
    
# execute query
def exec_query(query):
    prompt = args.query
    pre_prompt = prepare_prompt()
    response = get_chat_response(prompt, pre_prompt, apiurl=cmdgpt_conf["apiurl"])
    response_contents = decode_chat_response(response)
    try_exec(response_contents)

def try_exec(response_contents):
    cmd = ""
    print(f"{Fore.BLUE}CMDGPT:{Style.RESET_ALL} Do you want to execute the following command? (y/n):")
    for chunk in response_contents:
        print(Fore.YELLOW + chunk + Style.RESET_ALL, end="", flush=True)
        cmd += chunk
    print()
    if "MZHAO" in cmd:
        print(Fore.RED + "Please provide a valuable description." + Style.RESET_ALL)
        return
    if "\n" in cmd:
        print("It is a multi-line command. Please execute it manually.")
        return
    while True:
        pressed_key = get_key()
        if pressed_key:
            pressed_key = pressed_key.lower()
            if pressed_key == "y":
                os.system(cmd)
                break
            elif pressed_key == "n":
                print("Canceled.")
                break

# set openai api key
def set_openai_key(api_key):
    cmdgpt_conf["openai_api_key"] = api_key
    with open(cmdgpt_conf_path, "w+") as f:
        json.dump(cmdgpt_conf, f)
        
# set openai api url
def set_apiurl(apiurl):
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
