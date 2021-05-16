from nonebot.rule import ArgumentParser

parser = ArgumentParser("command")

subparsers = parser.add_subparsers(dest="handle")

subcommand_parent = subparsers.add_parser(
    "subcommand", help="Subcommand example", add_help=False
)
subparsers.add_parser("subcommand", parents=[subcommand_parent])
subparsers.add_parser("sc", parents=[subcommand_parent])