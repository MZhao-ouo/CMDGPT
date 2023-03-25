# CMDGPT

[![Release](https://github.com/MZhao-ouo/CMDGPT/actions/workflows/release.yml/badge.svg)](https://github.com/MZhao-ouo/CMDGPT/actions/workflows/release.yml)

A CLI tool to interact with GPT-3.5-turbo

![cmdgpt演示-_online-video-cutter com_](https://user-images.githubusercontent.com/70903329/227725280-2d22322e-accd-4371-8f1b-51a698566e64.gif)

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
- CMDGPT on Windows only supports providing commands and cannot execute them.
