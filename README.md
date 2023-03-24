# CMDGPT

[![Release](https://github.com/MZhao-ouo/CMDGPT/actions/workflows/release.yml/badge.svg)](https://github.com/MZhao-ouo/CMDGPT/actions/workflows/release.yml)

A CLI tool to interact with GPT-3.5-turbo

![image](https://user-images.githubusercontent.com/70903329/226573800-dee29ae9-6a25-4d5c-b22f-c761b35caf19.png)


## Install

```sh
pip install cmdgpt
```

## Usage

**Set your OpenAI api-key:**
```sh
cmdgpt --set_key "sk-xxx……xxx"
```

**Provide a command:**
```sh
cmdgpt "create a folder named 'www' with a file named 'index.html' inside"
```
**If `command not found: cmdgpt`**

Add the following line to your `~/.bashrc` or `~/.zshrc` file:
```sh
export PATH=$PATH:~/.local/bin
```
Then run `source ~/.bashrc` or `source ~/.zshrc` to reload the file.

**Known issues:**
- Commands such as `cd` and `source` cannot be used
