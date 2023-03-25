#!/usr/bin/env python3
from .presets import *
from .openai_func import *
from .functions import *
from .utils import *

def main():
    if cmdgpt_conf["openai_api_key"]=="" and args.key==None:
        print(f"Please set your OpenAI API key first.\nYou can get it from https://platform.openai.com/account/api-keys\nThen run the following command:\n{Fore.YELLOW}cmdgpt --key <YOUR_API_KEY>{Style.RESET_ALL}")
        exit(0)
    if len(sys.argv) == 1:
        show_help()
        exit()
    if args.reset_conf:
        reset_conf()
        exit()
    if args.key:
        set_openai_key(args.key)
    if args.apiurl:
        set_apiurl(args.apiurl)
    if args.query:
        exec_query(args.query)
        exit()
    if args.usage:
        get_usage()
        exit()

if __name__ == "__main__":
    main()
