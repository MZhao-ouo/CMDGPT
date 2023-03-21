# CMDGPT

[![Release](https://github.com/MZhao-ouo/CMDGPT/actions/workflows/release.yml/badge.svg)](https://github.com/MZhao-ouo/CMDGPT/actions/workflows/release.yml)

A CLI tool to interact with GPT-3.5-turbo

![image](https://user-images.githubusercontent.com/70903329/226573800-dee29ae9-6a25-4d5c-b22f-c761b35caf19.png)


## Install

```sh
wget https://github.com/MZhao-ouo/CMDGPT/releases/latest/download/cmdgpt_0.1.deb
sudo dpkg -i cmdgpt_0.1.deb
```

## Usage

**Set your OpenAI api-key:**
```sh
cmdgpt --set_key "sk-xxx……xxx"
```

**Provide a command:**
```sh
cmdgpt "create a folder named "www" with a file named "index.html" inside"
```
