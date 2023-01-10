import nonebot

nonebot.init()
app = nonebot.get_asgi()
driver = nonebot.get_driver()
nonebot.load_plugin("{{cookiecutter.package_name}}")

if __name__ == "__main__":
    nonebot.run(app="__mp_main__:app")
