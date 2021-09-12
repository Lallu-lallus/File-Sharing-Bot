import asyncio
from database.sql import query_msg
from pyrogram.errors import FloodWait

async def users_info(bot):
    users = 0
    blocked = 0
    identity = await query_msg()
    for id in identity:
        name = bool()
        try:
            name = await bot.send_chat_action(int(id[0]), "typing")
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception:
            pass
        if bool(name):
            users += 1
        else:
            blocked += 1
    return users, blocked
Mmm bro I set but cannot working the cmd

@pyrogram.Client.on_message(pyrogram.filters.command(["status"]))

async def _status(_, m: Message):

    total, used, free = shutil.disk_usage(".")

    total = humanbytes(total)

    used = humanbytes(used)

    free = humanbytes(free)

    cpu_usage = psutil.cpu_percent()

    ram_usage = psutil.virtual_memory().percent

    disk_usage = psutil.disk_usage('/').percent

    total_users = await db.total_users_count()

    await m.reply_text(

        text=f"**Total Disk Space:** {total} \n**Used Space:** {used}({disk_usage}%) \n**Free Space:** {free} \n**CPU Usage:** {cpu_usage}% \n**RAM Usage:** {ram_usage}%\n\n**Total Users in DB:** {total_users}",

        parse_mode="Markdown",

        quote=True

    )
