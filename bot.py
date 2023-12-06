import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
spam_chats = []

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply(
    "__**ɪ'ᴍ ᴍᴇɴᴛɪᴏɴᴀʟʟ ʙᴏᴛ**, ɪ ᴄᴀɴ ᴍᴇɴᴛɪᴏɴ ᴀʟᴍᴏsᴛ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ 👻\nᴄʟɪᴄᴋ **/ʜᴇʟᴘ** ᴀᴜʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴋᴇ ʟɪʏᴇ__\n\n ᴅᴍ ᴋᴀʀʟᴏ ᴏᴡɴᴇʀ ᴘᴀʀ[@its_Your_Aryan]",
    link_preview=False,
    buttons=( 
      [
        Button.url('ᴄʜᴀɴɴᴇʟ', 'https://t.me/Lily_x_bots'),
        Button.url('ʀᴇᴘᴏ', 'https://t.me/Its_Your_Aryan')
      ]
    )
  )

@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ ᴍᴇɴᴛɪᴏɴᴀʟʟʙᴏᴛ**\n\nCommand: /ᴍᴇɴᴛɪᴏɴᴀʟʟ\n__ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ᴛᴇxᴛ ᴡʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs.__\n`ᴇxᴀᴍᴘʟᴇ: /mentionall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ!`\n__ʏᴏᴜ ᴄᴀɴ ʏᴏᴜ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ. ʙᴏᴛ ᴡɪʟʟ ᴛᴀɢ ᴜsᴇʀs ᴛᴏ ᴛʜᴀᴛ ʀᴇᴘʟɪᴇᴅ ᴍᴇsssᴀɢᴇ__.\n\nᴅᴍ ᴋᴀʀʟᴏ ᴏᴡɴᴇʀ ᴘᴀʀ[@its_Your_Aryan"
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('ᴄʜᴀɴɴᴇʟ', 'https://t.me/Lily_x_bots'),
        Button.url('ʀᴇᴘᴏ', 'https://t.me/Its_Your_Aryan')
      ]
    )
  )
  
@client.on(events.NewMessage(pattern="^/mentionall ?(.*)"))
async def mentionall(event):
  chat_id = event.chat_id
  if event.is_private:
    return await event.respond("__ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ʙᴇ ᴜsᴇ ɪɴ ɢʀᴏᴜᴘ's ansd chasnnels!__")
  
  is_admin = False
  try:
    partici_ = await client(GetParticipantRequest(
      event.chat_id,
      event.sender_id
    ))
  except UserNotParticipantError:
    is_admin = False
  else:
    if (
      isinstance(
        partici_.participant,
        (
          ChannelParticipantAdmin,
          ChannelParticipantCreator
        )
      )
    ):
      is_admin = True
  if not is_admin:
    return await event.respond("__ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ!__")
  
  if event.pattern_match.group(1) and event.is_reply:
    return await event.respond("__ɢɪᴠᴇ ᴍᴇ ᴏɴᴇ ᴀʀɢᴜᴍᴇɴᴛ!__")
  elif event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.is_reply:
    mode = "text_on_reply"
    msg = await event.get_reply_message()
    if msg == None:
        return await event.respond("__ɪ ᴄᴀɴ'ᴛ ᴍᴇɴᴛɪᴏɴ ᴍᴇᴍʙᴇʀs ғᴏʀ ᴏʟᴅᴇʀ ᴍᴇssᴀɢᴇs! (ᴍᴇssᴀɢᴇs ᴡʜɪᴄʜ ᴀʀᴇ ɢᴏɪɴɢ ʙᴇғᴏʀᴇ ɪ'ᴍ ᴀᴅᴅᴇᴅ to ɢʀᴏᴜᴘ)__")
  else:
    return await event.respond("__ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs!__")
  
  spam_chats.append(chat_id)
  usrnum = 0
  usrtxt = ''
  async for usr in client.iter_participants(chat_id):
    if not chat_id in spam_chats:
      break
    usrnum += 1
    usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
    if usrnum == 5:
      if mode == "text_on_cmd":
        txt = f"{usrtxt}\n\n{msg}"
        await client.send_message(chat_id, txt)
      elif mode == "text_on_reply":
        await msg.reply(usrtxt)
      await asyncio.sleep(2)
      usrnum = 0
      usrtxt = ''
  try:
    spam_chats.remove(chat_id)
  except:
    pass

@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
  if not event.chat_id in spam_chats:
    return await event.respond('__ᴛʜᴇʀᴇ ɪs ɴᴏ ᴘʀᴏᴄᴄᴇss ᴏɴ ɢᴏɪɴɢ...__')
  else:
    try:
      spam_chats.remove(event.chat_id)
    except:
      pass
    return await event.respond('__sᴛᴏᴘᴘᴇᴅ.__')

print(">> BOT STARTED <<")
client.run_until_disconnected()
