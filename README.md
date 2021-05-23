# Nonebot Template Plugin

**注意，这并不是一个 Nonebot 插件，而是 Nonebot 插件模板！**

*突然发现我写的大部分插件基本上都采用了类似的结构，干脆就做成模板好了。*

适用于

## Usage

### Cookiecutter

```shell
cookiecutter gh:nonepkg/nonebot-template-plugin
```

### nb-cli

```shell
nb plugin new -T gh:nonepkg/nonebot-template-plugin
```

## Structure

```shell
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
│    __init__.py
```

## To Do

- [x] 魔改 nb-cli 使其支持自定义插件模板
