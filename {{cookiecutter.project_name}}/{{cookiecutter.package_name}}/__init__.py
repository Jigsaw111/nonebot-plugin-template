from nonebot.plugin import on_shell_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import (
    Bot,
    MessageEvent,
)

from {{cookiecutter.package_name}}.parser import Namespace, parser
from {{cookiecutter.package_name}}.handle import Handle
from {{cookiecutter.package_name}}.data import Data

command = on_shell_command("command", parser=parser, priority=1)

@command.handle()
async def _(bot: Bot, event: MessageEvent, state: T_State):

    args: Namespace = state["args"]

    if hasattr(args, "handle"):
        try:
            await bot.send(event, getattr(Handle, args.handle)(args))
        except:
            pass
    else:
        await bot.send(event, args.message)