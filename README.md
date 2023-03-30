<div align="right">
  <!-- 语言: -->
  简体中文 | <a title="English" href="README-en.md">English</a>
</div>

<img height="128" align="left" src="https://user-images.githubusercontent.com/70903329/228310136-b27cbe83-e7e1-4560-ba75-1b418ba9e5a0.png" alt="Logo">

# CMDGPT | 用自然语言操作命令行

[![Release](https://github.com/MZhao-ouo/CMDGPT/actions/workflows/release.yml/badge.svg)](https://github.com/MZhao-ouo/CMDGPT/actions/workflows/release.yml) 
[![Version](https://img.shields.io/pypi/v/cmdgpt?label=Release%20Version)](https://pypi.org/project/cmdgpt/) 
[![Pypi](https://img.shields.io/pypi/dd/cmdgpt?logo=pypi)](https://pypi.org/project/cmdgpt/) 

![cmdgpt演示-_online-video-cutter com_](https://user-images.githubusercontent.com/70903329/227725280-2d22322e-accd-4371-8f1b-51a698566e64.gif)

## 安装

```sh
pip install cmdgpt
```

**如果遇到报错 `command not found: cmdgpt`**

请将以下内容添加到您的`/.bashrc`或`/.zshrc`文件中：
```sh
export PATH=$PATH:~/.local/bin
```
然后运行`source ~/.bashrc`或`source ~/.zshrc`重新加载文件。

## 用法

**设置 OpenAI api-key:**
```sh
cmdgpt --key "sk-xxx……xxx"
```

**自然语言交互**
```sh
cmdgpt "创建一个名为www的文件夹，里面有一个index.html文件"
```

**Chat模式**
```sh
cmdgpt --chat
```

**指定api_host**

你只需要填host即可，例如：
```sh
cmdgpt --api_host "api.openai.com"
```

## 已知问题
- 无法使用`cd`和`source`等命令。
- Windows上的CMDGPT仅支持提供命令，无法执行命令。

## 本地调试
1. Clone本仓库
```sh
git clone https://github.com/MZhao-ouo/CMDGPT.git
cd CMDGPT
```

2. 修改代码，代码位于cmdgpt文件夹
3. 运行:

先卸载旧版本
```sh
pip uninstall cmdgpt -y
```

生成python模块
```sh
python setup.py sdist bdist_wheel
```

安装本地python模块（注意版本号要与./cmdgpt/VERSION一致，且不小于当前版本）
```sh
pip install dist/cmdgpt-0.2.3-py3-none-any.whl
```

或者你可以一键执行（注意版本号要与./cmdgpt/VERSION一致，且不小于当前版本）
```sh
pip uninstall cmdgpt -y | python setup.py sdist bdist_wheel && pip install dist/cmdgpt-0.2.3-py3-none-any.whl
```
