import nonebot
from nonebot.adapters.cqhttp import Bot

nonebot.init()
app = nonebot.get_asgi()
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", Bot)
nonebot.load_plugin("{{cookiecutter.package_name}}")

if __name__ == "__main__":
    nonebot.run(app="__mp_main__:app")
