# {{cookiecutter.plugin_name.title()}}

基于 [NoneBot2](https://github.com/nonebot/nonebot2) 的插件

[![License](https://img.shields.io/github/license/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}?style=flat-square)](LICENSE)
![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg?style=flat-square)
![NoneBot Version](https://img.shields.io/badge/nonebot-2.0.0rc2+-red.svg?style=flat-square)
[![Pypi Version](https://img.shields.io/pypi/v/{{cookiecutter.project_name}}.svg?style=flat-square)](https://pypi.python.org/pypi/{{cookiecutter.project_name}})

## 安装

### 从 PyPI 安装（推荐）

- 使用 nb-cli  

```
nb plugin install {{cookiecutter.project_name}}
```

- 使用 pdm

```
pdm add {{cookiecutter.project_name}}
```

- 使用 pip

```
pip install {{cookiecutter.project_name}}
```

### 从 GitHub 安装（不推荐）

```
git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}.git
```

### 使用

**使用前请先确保命令前缀为空，否则请在以下命令前加上命令前缀 (默认为 `/` )。**
