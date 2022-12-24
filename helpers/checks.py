from typing import Callable, TypeVar

from discord.ext import commands

from exceptions import *
from helpers import db_manager

T = TypeVar("T")


# def is_owner() -> typing.Callable[[T], T]:
#     """
#     This is a custom check to see if the user executing the command is an owner of the bot.
#     """
#     async def predicate(context: commands.Context) -> bool:
#         owners = os.getenv("owner").split(",")
#         if context.author.id not in owners:
#             raise UserNotOwner
#         return True

#     return commands.check(predicate)

# Remove the not_blacklisted function

# def not_blacklisted() -> typing.Callable[[T], T]:
#     """
#     This is a custom check to see if the user executing the command is blacklisted.
#     """
#     async def predicate(context: commands.Context) -> bool:
#         if await db_manager.is_blacklisted(context.author.id):
#             raise UserBlacklisted
#         return True

#     return commands.check(predicate)