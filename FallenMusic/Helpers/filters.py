from typing import List, Union
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import UserNotParticipant
from FallenMusic import app

other_filters = filters.group

def command(commands: Union[str, List[str]]):
    return filters.command(commands, "")


channel = "cczza" # Your Channel
async def subscription(_, __: Client, message: Message):
    user_id = message.from_user.id
    try: await app.get_chat_member(channel, user_id)
    except UserNotParticipant: return False
    return True
    
subscribed = filters.create(subscription)
