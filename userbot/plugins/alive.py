import time

from telethon import version
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from FIREX.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import ALIVE_NAME, eviralversion
from userbot.cmdhelp import CmdHelp  # eviral
from userbot.Config import Config

from . import *


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
DEFAULTUSER = ALIVE_NAME or "๐๐ษ รชษณฬdแบรธโ๏ธ ๐ฎ๐ณ"
eviral_IMG = "https://telegra.ph/file/153977a71b928874151a5.jpg"
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "eviral Choice ๐๐ษ รชษณฬdแบรธโ๏ธ"
CUSTOM_YOUR_GROUP = Config.YOUR_GROUP or "@FirexSupport"

eviral = bot.uid
mention = f"[{DEFAULTUSER}](tg://user?id={eviral})"


@bot.on(admin_cmd(outgoing=True, pattern="eviral$"))
@bot.on(sudo_cmd(pattern="eviral$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if eviral_IMG:
        eviral_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"

        eviral_caption += f"~~~~~~~~~~~~~~~~~~~~~~~\n"
        eviral_caption += f"        **โ๐ญ๐โ  ๐พ๐๐๐๐๐โ** \n"
        eviral_caption += f"โข๐ฅโข **Oีกีฒฬาฝฬษพ**          ~ {ALIVE_NAME}\n\n"
        eviral_caption += f"โข๐โข **๐๐ษ รชษณฬdแบรธโ **ย   ~ {eviralversion}\n"
        eviral_caption += f"โข๐โข **โ าฝฬlาฝฬthรธีฒฬ**     ~ `{version.__version__}`\n"
        eviral_caption += f"โข๐โข **๐ฯtime**         ~ `{uptime}`\n"
        eviral_caption += f"โข๐โข **๐ถ๐๐๐๐**           ~ [๐ถ๐๐๐๐](t.me/FirexSupport)\n"
        eviral_caption += f"โข๐โข **๐ผ๐ข ๐ถ๐๐๐๐**  ~ {CUSTOM_YOUR_GROUP}\n"

        await alive.client.send_file(
            alive.chat_id, eviral_IMG, caption=eviral_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"         \n"
            f"โขโกโข ๐ฟัโัฯะฝฮฟะธ    : `{version.__version__}`\n"
            f"๐ฎ๐ณ eviralฯฮฟฯ  : `{eviralversion}`\n"
            f"๐ฎ๐ณ ฯฯฯฮนะผั        : `{uptime}`\n"
            f"๐ฑ ษฑฮฑเธฃฦญฮตษพ        : {mention}\n"
            f"๐ฑ ฯฯษณฮตษพ         : [eviral](t.me/Eviral)\n",
        )


msg = f"""
**  โ๏ธ FIRE-X ฮนั ฯะธโฮนะธั โ๏ธ**

       {Config.ALIVE_MSG}
    **  Bรธโ๏ธ แบโ๏ธฮฑโ๏ธยตั **
**โขโ๏ธโขรีกีฒฬาฝฬr     :** **{mention}**
**โข๐นโข๐๐ษ รชษณฬdแบรธโ๏ธ  :** {eviralversion}
**โข๐นโขโ๏ธาฝฬlาฝฬฦญhรธีฒ  :** {version.__version__}
**โข๐นโขรbรปรรช     :**  {abuse_m}
**โข๐นโขรudรธ      :**  {is_sudo}
**โข๐นโขBรธt.      :** {Config.BOY_OR_GIRL}
"""
botname = Config.BOT_USERNAME


@bot.on(admin_cmd(pattern="alive$"))
@bot.on(admin_cmd(pattern="alive$", allow_sudo=True))
async def eviral_a(event):
    try:
        eviral = await bot.inline_query(botname, "alive")
        await eviral[0].click(event.chat_id)
        if event.sender_id == Eviral:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command("bot", None, "ฯัั ฮฑะธโ ััั").add_command(
    "eviral", None, "Its Same Like Alive"
).add_command("alive", None, "Its Show ur Alive Template").add_warning(
    "Harmless Moduleโ"
).add_info(
    "Checking Alive"
).add_type(
    "Official"
).add()
