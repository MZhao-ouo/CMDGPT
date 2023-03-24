#!/usr/bin/env python3
from .presets import *
from .openai_func import *

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


def prepare_prompt():
    pre_prompt = ""
    pre_prompt += f"My system infomation is:\n{sys_info}\n"
    pre_prompt += f"My current shell is:\n{current_shell}\n"
    pre_prompt += f"My current working directory is:\n{cwd_path}\n"
    pre_prompt += f"My command history is:\n{cmd_history}\n"
        
    logging.info(f"Pre prompt: \n{pre_prompt}")
    return pre_prompt
                

def set_openai_key(api_key):
    cmdgpt_conf["openai_api_key"] = api_key
    with open(cmdgpt_conf_path, "w+") as f:
        json.dump(cmdgpt_conf, f)


def main():
    if cmdgpt_conf["openai_api_key"]=="" and args.set_key==None:
        print("Please set your OpenAI API key first.")
        print("You can get it from https://beta.openai.com/account/api-keys")
        print("Then run the following command:")
        print("cmdgpt --set_key YOUR_API_KEY")
        sys.exit(0)
        
    if len(sys.argv) == 1:
        show_help()
        exit()
    
    if args.query:
        prompt = args.query
        pre_prompt = prepare_prompt()
        response = get_chat_response(prompt, pre_prompt)
        response_contents = decode_chat_response(response)
        try_exec(response_contents)
        exit()
        
    if args.set_key:
        set_openai_key(args.set_key)
        exit()
        
    if args.usage:
        get_usage()
        exit()

if __name__ == "__main__":
    main()
