import time

from telethon import version

from FIREX.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import StartTime, eviralversion
from userbot.cmdhelp import CmdHelp

from . import *


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


eviral_IMG = Config.AWAKE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "eviral Choice eviralฯฮฟฯ"
CUSTOM_YOUR_GROUP = Config.YOUR_GROUP or "@FirexSupport"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="awake$"))
@bot.on(sudo_cmd(pattern="awake$", allow_sudo=True))
async def amireallyalive(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)

    if eviral_IMG:
        eviral_caption = f"**{eviral_mention}**\n"

        eviral_caption += f"~~~~~~~~~~~~~~~~~~~~~~~\n"
        eviral_caption += f"     โ ๐๐ฎ๐ฐ๐ฎ๐ท๐ญ๐๐ธ๐ฝ ๐๐ผ ๐๐๐ช๐ด๐ฎ โ\n"
        eviral_caption += f"โข๐ฅโข FIRE-X     : ฮฝ3.0\n"
        eviral_caption += f"โข๐ฅโข ๐๐ด๐ป๐ด๐๐ท๐พ๐ฝ      : `{version.__version__}`\n"
        eviral_caption += f"โข๐ฅโข ๐๐ฟ๐๐ธ๐ผ๐ด         : `{uptime}`\n"
        eviral_caption += f"โข๐ฅโข ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป        : [๐ฎะฝฮฑะธะธัโ](t.me/Official_FIREX)\n"
        eviral_caption += f"โข๐ฅโข แดนสธ ๐ถ๐๐พ๐๐ฟ : {CUSTOM_YOUR_GROUP}\n"

        await event.client.send_file(
            event.chat_id, eviral_IMG, caption=eviral_caption, reply_to=reply_to_id
        )
        await event.delete()
    else:
        await edit_or_reply(
            awake,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"         ๐ญ๐๐ ๐พ๐๐๐๐๐\n"
            f"โขโกโข ๐ฟัโัฯะฝฮฟะธ    : `{version.__version__}`\n"
            f"๐ฎ๐ณ eviralฯฮฟฯ  : `{eviralversion}`\n"
            f"๐ฎ๐ณ ฯฯฯฮนะผั        : `{uptime}`\n"
            f"๐ฑ ษฑฮฑเธฃฦญฮตษพ        : {mention}\n"
            f"๐ฑ ฯฯษณฮตษพ         : [eviral](t.me/Eviral)\n",
        )


CmdHelp("awake").add_command("awake", None, "ฯัั ฮฑะธโ ััั").add_info(
    "Same Like Alive"
).add_type("Official").add()
