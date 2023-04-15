from .presets import *

terminal_columns = shutil.get_terminal_size().columns

def init_conf(cmdgpt_conf_path):
    with open(cmdgpt_conf_path, "w+", encoding="utf-8") as f:
        cmdgpt_conf = {}
        cmdgpt_conf["openai_api_key"] = ""
        cmdgpt_conf["api_host"] = "api.openai.com"
        json.dump(cmdgpt_conf, f)
    return cmdgpt_conf

def load_conf(cmdgpt_conf_path):
    with open(cmdgpt_conf_path, "r", encoding="utf-8") as f:
        cmdgpt_conf = json.load(f)
        
    keys_to_delete = []
    for key in cmdgpt_conf:
        if key not in ["openai_api_key", "api_host"]:
            keys_to_delete.append(key)
    for key in keys_to_delete:
        del cmdgpt_conf[key]
    
    if "openai_api_key" not in cmdgpt_conf:
        cmdgpt_conf["openai_api_key"] = ""
    elif "api_host" not in cmdgpt_conf:
        cmdgpt_conf["api_host"] = "api.openai.com"
        
    with open(cmdgpt_conf_path, "w", encoding="utf-8") as f:
        json.dump(cmdgpt_conf, f)
    return cmdgpt_conf

def process_file(filename):
    with open(filename, 'rb') as file:
        change = False
        output_data = bytearray()
        while (ch := file.read(1)):
            ch = ord(ch)
            if ch != 0x83:
                if change:
                    d = ch ^ 32
                else:
                    d = ch
                output_data.append(d)
                change = False
            else:
                change = True

        output_str = output_data.decode("utf-8")
        lines = output_str.splitlines(keepends=True)
        return lines
    
    
def get_cmd_history(current_shell, user_home):
    cmd_history = ""
    if "PowerShell" in current_shell:
        return ""
    elif "zsh" in current_shell:
        history_filename = os.path.join(user_home, ".zsh_history")
        cmd_history_list = process_file(history_filename)[-17:-1]
        for _ in cmd_history_list:
            cmd_history += _[15:]
    else:
        history_filename = os.path.join(user_home, ".bash_history")
        with open(history_filename, "rt", errors="ignore") as f:
            cmd_history_list = f.readlines()[-17:-1]
        for _ in cmd_history_list:
            cmd_history += _
    return cmd_history
    

def full_column_str(str):
    return str + " " * (terminal_columns - len(str))

if os.name == 'nt':  # Windows
    import msvcrt

    def get_key():
        if msvcrt.kbhit():
            return msvcrt.getch().decode()
elif os.name == 'posix':  # Linux or macOS
    import sys
    import tty
    import termios

    def get_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
