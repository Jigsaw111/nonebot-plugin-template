# NoneBot Template Plugin

**注意，这并不是一个 NoneBot2 插件，而是 NoneBot2 插件模板！**

*突然发现我写的大部分插件基本上都采用了类似的结构，干脆就做成模板好了。*

## Usage

### Cookiecutter

```shell
cookiecutter gh:nonepkg/nonebot-template-plugin
```

### nb-cli

```shell
nb plugin new -t gh:nonepkg/nonebot-template-plugin
```

## Structure

```shell
nonebot-plugin-template（项目名）
│  .env
│  .gitignore
│  .pre-commit-config.yaml
│  bot.py
│  LICENSE
│  pyproject.toml
│  README.md
│  pyrightconfig.json
│
│─nonebot_plugin_template（包名）
│    data.py
│    handle.py
│    parser.py
│    __init__.py
│
│─.devcontainer
│    devcontainer.json
│
|-.github
|--workflows
|    publish_to_pypi.yaml
```
