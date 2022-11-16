# RiZoeL X - Telegram Projects
# (c) 2022 - 2023 RiZoeL
# Don't Kang Bitch -!




import os
import sys
from random import choice
from SpamX import (OWNER_ID, HNDLR, SUDO_USERS, hl)
from pyrogram import Client, filters
from pyrogram.types import Message
from SpamX.data import *



@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["help"], prefixes=HNDLR))
async def help(_, e: Message):
        RiZoeL = e.text.split(" ")
        if len(RiZoeL) > 1:
            helping = RiZoeL[1]
            if helping.lower() == "spam":
                await e.reply(spam_help)
            elif helping.lower() == "dm":
                await e.reply(dm_help)
            elif helping.lower() == "userbot":
                await e.reply(userbot_help)
            elif helping.lower() == "leave":
                await e.reply(leave_help)
            elif helping.lower() == "extra":
                await e.reply(extra_help)
            else:
                await e.reply(help_menu)
        else:
            await e.reply(help_menu)


spam_help = f"""
**• sᴘᴀᴍ ᴄᴍᴅs•**

**sᴘᴀᴍ**: sᴘᴀᴍs ᴀ ᴍᴇssᴀɢᴇ ғᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ (ɴᴏ ᴄᴏᴜɴᴛ ʟɪᴍɪᴛ)
sʏɴᴛᴀx:
 {hl}spam (count) (message to spam)
 {hl}delayspam (delay time In seconds) (count) (message to spam) 
 {hl}fspam (count) (message to spam)
 {hl}pornspam (count)
 {hl}ispam (count) (username or reply to user)

**ʀᴀɪᴅ:** ᴀᴄᴛɪᴠᴀᴛᴇs ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜsᴇʀ ғᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ.
sʏɴᴛᴀx:
 {hl}raid (count) (username or user id)
 {hl}replyraid (username or reply to user)
 {hl}dreplyraid (username or reply to user)
 
**ʜᴀɴɢ:** ʜᴀɴɢ ᴍᴇssᴀɢᴇ sᴘᴀᴍ
sʏɴᴛᴀx:
{hl}hang (counts)


**© @HYPER_X_RACHIT**
"""


dm_help = f"""
**• ᴅᴍ sᴘᴀᴍs•**

**ᴅᴍ:** ᴅᴍ ᴛᴏ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜsɪɴɢ sᴘᴀᴍ ʙᴏᴛs
ᴄᴏᴍᴍᴀɴᴅ:
  {hl}dm (username or user id) (message)

**ᴅᴍ sᴘᴀᴍ:** sᴘᴀᴍ ɪɴ ᴅᴍ ᴏғ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜsᴇʀs
ᴄᴏᴍᴍᴀɴᴅ:
  {hl}dmspam (username or user id) (count)  (message to spam)

**ᴅᴍ ʀᴀɪᴅ:** ʀᴀɪᴅ ɪɴ ᴅᴍ ᴏғ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜsᴇʀs
ᴄᴏᴍᴍᴀɴᴅ:
  {hl}dmraid (count) (username or user id)

**© @ʜʏᴘᴇʀ_x_ʀᴀᴄʜɪᴛ**
"""

leave_help = f"""
**• ʟᴇᴀᴠᴇ ᴄᴍᴅs •**

**ʟᴇᴀᴠᴇ:** ʟᴇᴀᴠᴇ ᴀɴʏ ᴘᴜʙʟɪᴄ/ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ
sʏɴᴛᴀx:
i) {hl}leave group Username or chat user id
ii) {hl}leave

**© @HYPER_X_RACHIT**
"""

userbot_help = f"""
**• ᴜsᴇʀʙᴏᴛ ᴄᴍᴅs •**

- {hl}ᴘɪɴɢ : ᴛᴏ ᴄʜᴇᴄᴋ ᴘɪɴɢ

- {hl}ᴀʟɪᴠᴇ : ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴠᴇʀsɪᴏɴ ᴀɴᴅ ᴏᴛʜᴇʀ ɪɴғᴏ

- {hl}ʀᴇsᴛᴀʀᴛ : ᴛᴏ ʀᴇsᴛᴀʀᴛ ʏᴏᴜʀ sᴘᴀᴍ ʙᴏᴛs

**© @HYPER_X_RACHIT**
"""

help_menu = f"""
**ʜʏᴘᴇʀ x sᴘᴀᴍ ʜᴇʟᴘ ᴍᴇɴᴜ **

**ᴛʜᴇʀᴇ ᴀʀᴇ ғᴏʟʟᴏᴡɪɴɢ ᴄᴀᴛᴇɢᴏʀɪᴇs**

`owner` : ɢᴇᴛ ᴀʟʟ ᴏᴡɴᴇʀ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ɪᴛs ᴜsᴀɢᴇ
`spam` : ɢᴇᴛ ᴀʟʟ sᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ɪᴛs ᴜsᴀɢᴇ
`dm` : ɢᴇᴛ ᴀʟʟ ᴅᴍ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ɪᴛs ᴜsᴀɢᴇ
`join` : ɢᴇᴛ ᴊᴏɪɴ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ɪᴛs ᴜsᴀɢᴇ
`leave` : ɢᴇᴛ ʟᴇᴀᴠᴇ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ɪᴛs ᴜsᴀɢᴇ
`userbot` : ɢᴇᴛ ᴀʟʟ ᴜsᴇʀʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs
`extra` : ɢᴇᴛ ᴀʟʟ ᴇxᴛʀᴀ ᴄᴍᴅs

**Type** {hl}help (category) **ᴛᴏ ɢᴇᴛ ᴀʟʟ sʏɴᴛᴀx ɪᴍ ᴛʜᴀᴛ ᴄᴀᴛᴇɢᴏʀʏ ᴀɴᴅ ɪᴛs ᴜsᴀɢᴇ**
**Example**: `{hl}help spam`

**© @HYPER_X_RACHIT**
"""


extra_help = f"""
**• ᴜɴʟɪᴍɪᴛᴇᴅ ᴄᴍᴅs •**

**ᴜɴʟɪᴍɪᴛᴇᴅ sᴘᴀᴍ**
sʏɴᴛᴀx:
 {hl}uspam (message to spam)

**ᴜɴʟɪᴍɪᴛᴇᴅ ʀᴀɪᴅ**
sʏɴᴛᴀx:
 {hl}uraid (username or user id / reply to user)

**ᴀʙᴜss / ᴏɴᴇ ᴡᴏʀᴅ**
sʏɴᴛᴀx:
  {hl}absue (counts)

  **ʀᴇᴀᴅ**: ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀʙᴜsᴇ sɪᴍᴘʟʏ ᴛʏᴘᴇ {hl}abuse -!

**sᴛᴏᴘ ᴄᴍᴅ**: sɪᴍᴘʟʏ ᴛʏᴘᴇ {hl}stop ᴛᴏ sᴛᴏᴘ sᴘᴀᴍ/ᴀʙᴜsᴇ/ʀᴀɪᴅ ᴀɴʏ ᴏғ ᴛʜᴀᴛ

**© @HYPER_X_RACHIT**
"""
