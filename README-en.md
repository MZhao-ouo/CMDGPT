<div align="right">
  <!-- 语言: -->
  <a title="简体中文" href="README.md">简体中文</a> | English
</div>

<img height="128" align="left" src="https://user-images.githubusercontent.com/70903329/228310136-b27cbe83-e7e1-4560-ba75-1b418ba9e5a0.png" alt="Logo">

# CMDGPT | Manipulate command line with natural language

[![Release](https://github.com/MZhao-ouo/CMDGPT/actions/workflows/release.yml/badge.svg)](https://github.com/MZhao-ouo/CMDGPT/actions/workflows/release.yml) 
[![Version](https://img.shields.io/pypi/v/cmdgpt?label=Release%20Version)](https://pypi.org/project/cmdgpt/) 
[![Pypi](https://img.shields.io/pypi/dm/cmdgpt?logo=pypi)](https://pypi.org/project/cmdgpt/) 

![cmdgpt演示-_online-video-cutter com_](https://user-images.githubusercontent.com/70903329/227725280-2d22322e-accd-4371-8f1b-51a698566e64.gif)

## Install

```sh
pip install cmdgpt
```

**Error: `command not found: cmdgpt`**

Please add the following content to your `/.bashrc` or `/.zshrc` file:
```sh
export PATH=$PATH:~/.local/bin
```
Then run `source ~/.bashrc` or `source ~/.zshrc` to reload the file.

## Usage

**Set OpenAI api-key:**
```sh
cmdgpt --key "sk-xxx……xxx"
```

**Describe your opeartion**
```sh
cmdgpt "Create a folder named 'www' with an 'index.html' file inside."
```

**Chat Mode**
```sh
cmdgpt --chat
```

**Set api-url**
```sh
cmdgpt --url "你的api-url"
```

**Know Issue**
- Unable to use commands such as `cd` and `source`.
- CMDGPT on Windows only supports providing commands, it cannot execute them.
