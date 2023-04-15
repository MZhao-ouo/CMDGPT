#!/usr/bin/env python3
from .functions import *

def show_help():
    print("Usage:")
    print("\tcmdgpt <Your Purpose>")
    print("Arguments:")
    print("\t--key\t\t:set OpenAI api key")
    print("\t--chat\t\t:chat with gpt-3.5")
    print("\t--credit\t:get OpenAI credit")
    print("\t--usage\t\t:get OpenAI usage")
    print("\t  --start_date\t:start date")
    print("\t  --end_date\t:end date")
    print("\t--api_host\t:set OpenAI api url")
    print("\t--reset_conf\t:reset the default configuration")
    print("\t--debug\t\t:enable debug mode")

def main():
    if cmdgpt_conf["openai_api_key"]=="" and args.key==None:
        print(f"Please set your OpenAI API key first.\nYou can get it from https://platform.openai.com/account/api-keys\nThen run the following command\n{Fore.YELLOW}cmdgpt --key <YOUR_API_KEY>{Style.RESET_ALL}")
        exit(0)
    if len(sys.argv) == 1:
        show_help()
        exit()
    if args.chat:
        chat_ai()
        exit()
    if args.reset_conf:
        reset_conf()
        exit()
    if args.key:
        set_openai_key(args.key)
    if args.api_host:
        set_apihost(args.api_host)
    if args.query:
        exec_query(args.query)
        exit()
    # if args.credit:
    #     get_credit(credit_url=CREDIT_URL)
    #     exit()
    if args.usage:
        get_usage(usage_url=USAGE_URL, start_date=args.start_date, end_date=args.end_date)
        exit()

if __name__ == "__main__":
    main()
