# NoneBot Template Plugin

**注意，这并不是一个 NoneBot2 插件，而是 NoneBot2 插件模板！**

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
