from telethon import version

from FIREX.utils import *
from userbot import *
from userbot.cmdhelp import CmdHelp

# -------------------------------------------------------------------------------

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "eviral"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

eviral = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={eviral})"


PM_IMG = "https://telegra.ph/file/4f03f6d4e9521902eb57f.jpg"
pm_caption = "**ππΙ ΓͺΙ³ΜdαΊΓΈβοΈ πΈπ πΎπππππ**\n\n"

pm_caption += f"**βπ₯βtΝαΊΜΈ ππΙ ΓͺΙ³ΜdαΊΓΈβοΈtπ₯β**\n"
pm_caption += f"**β£π πΌπ’ πΌπππππ    : {mention}**\n"
pm_caption += f"**β£π ππππππππ : `{version.__version__}`**\n"
pm_caption += f"**β£π ππΙ ΓͺΙ³ΜdαΊΓΈβοΈ : {eviralversion}**\n"
pm_caption += f"**β£π ππππ     : `{sudou}`**\n"
pm_caption += f"**β£π πΎπ πππ     : [ππΙ ΓͺΙ³Μd](https://t.me/Eviral)**\n"
pm_caption += f"**β[β¦οΈπΆππππβ¦οΈ](https://t.me/FirexSupport)β**\n"

pm_caption += "    [β¨ΡΡΟΞΏβ¨](https://github.com/Teameviral/FIREX) πΉ [πLicenseπ](https://github.com/Teameviral/FIREX/blob/master/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="bot$"))
@bot.on(sudo_cmd(pattern="bot$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("alv").add_command(
    "alive", None, "Check weather the bot is alive or not"
).add_command(
    "bot",
    None,
    "Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg",
).add_warning(
    "Harmless Module"
).add_info(
    "Are u alive?"
).add_type(
    "Official"
).add()
