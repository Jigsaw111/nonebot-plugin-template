# Nonebot Plugin Template

**注意，这并不是一个 Nonebot 插件，而是 Nonebot 插件模板！**

*突然发现我写的大部分插件基本上都采用了类似的结构，干脆就做成模板好了。*

## Usage

*cookiecutter 在你安装 nb-cli 的时候就已经安装好了了。*

```
cookiecutter gh:Jigsaw111/nonebot-plugin-template
```

## Structure

```
nonebot-plugin-template
│  .gitignore
│  LICENSE
│  pyproject.toml
│  README.md
│  
│─nonebot_plugin_template
│    data.py
│    handle.py
│    parser.py
│    typing.py
│    __init__.py
```

## To Do

- [ ] 增加自动安装 GOCQ 的脚本
- [ ] 魔改 nb-cli 使其支持自定义插件模板