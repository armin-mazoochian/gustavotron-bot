import math
import time
from pyrogram import Client, filters
import random
from keyboards import INLINE_KEYBOARD, REPLY_KEYBOARD
from stfu import get_stfu_mode, set_stfu_mode, stfu_enabled
from dotenv import load_dotenv
from exceptions import EnvironmentFileError
import os

load_dotenv()

api_id: int = int(os.environ.get("API_ID", None))
api_hash: str = os.environ.get("API_HASH")

if not api_id or api_hash is None:
    raise EnvironmentFileError

app = Client("my_account", api_id=api_id, api_hash=api_hash)

racista_ratio = 1
version = '2.1'
gus_api_ver = '1.2'
fela_ver = '5.8'


async def func(_, __, query):
    return query.data == "data"


static_data_filter = filters.create(func)


async def ver(_, __, query):
    return query.data == "version"


version_callback_filter = filters.create(ver)


async def stfu_func(_, __, query):
    return query.data == "stfu_enable"


stfu_callback_filter = filters.create(stfu_func)


@app.on_message(filters.command(['stfu']))
async def stfu_set(_, message):
    set_stfu_mode()
    if get_stfu_mode():
        await message.reply("✅ STFU enabled!")
    else:
        await message.reply("❌ STFU Disabled")


def set_racista_ratio(ratio: int) -> None:
    global racista_ratio
    racista_ratio = ratio


async def get_chat_members_mention_string(chat_id):
    mentions = []
    async for member in app.get_chat_members(chat_id):
        mentions.append(member.user)
    return mentions


@app.on_callback_query(stfu_callback_filter)
@stfu_enabled
async def stfu_callback_handler(_, query):
    set_stfu_mode()
    if get_stfu_mode():
        await query.message.edit("✅ STFU enabled!")
    else:
        await query.message.edit("❌ STFU Disabled")


@app.on_callback_query(version_callback_filter)
@stfu_enabled
async def version_handler(_, query):
    await query.message.edit(f"**Gustavotron - Free**\n\n__Version__: {version}\n__Gustavo API Level__: {gus_api_ver}"
                             f"\n__Fela API Level__: {fela_ver}\n\n"
                             f"Licensed to Gustavo Fring (@NowPremiumUser)\n__For legal information and privacy policy "
                             f"contact @OnetimeUsername__")


@app.on_callback_query(static_data_filter)
@stfu_enabled
async def button_press(_, query):
    text = ''
    mentions = await get_chat_members_mention_string(query.message.chat.id)
    k = 0
    for i in range(math.ceil(len(mentions) / 5)):
        for person in mentions[k:k + 5]:
            text = text + person.mention(style="md") + ' '
        time.sleep(3.0)
        await app.send_message(query.message.chat.id, text)
        text = ''
        k += 5


@app.on_message(filters.command(['i', 'inline']))
@stfu_enabled
async def keyboard(_, message):
    await message.reply(
        "**At your service!**\nWhat do you wanna do? :)",
        reply_markup=INLINE_KEYBOARD
    )


@app.on_message(filters.command(['k', 'keyboard']))
@stfu_enabled
async def keyboard(_, message):
    await message.reply(
        "This is a ReplyKeyboardMarkup example",
        reply_markup=REPLY_KEYBOARD,
        resize_keyboard=True  # Make the keyboard smaller
    )


@app.on_message(filters.command(['f', 'fela']) & (filters.chat(["me", -1001874611480]) | filters.private))
@stfu_enabled
async def racista(_, message):
    insults = ["you incompetent fuck", "lmao you gai", "fuck off", "bitch", "dumbass TSF fuck",
               "yo mama so fat she can eat all unigram bugs and still be hungry", "candy ass madafakas",
               "shut your face you non-dev scumbag", "fuck you, lucas and every user ever", "lol you so stoooopid"
               "joe mama sooooo gai", "dima has more hair than joe mama", "hoe",
               "if you were italian your name would be Retardo", "suck my Qt dick",
               "here's a box of boosts you poor-ass bitch", "TSF stands for True Suckers For devs",
               "you're on the latest beta. I'm on your gal"]
    await message.reply(insults[random.randint(0, len(insults))])


@app.on_message(filters.command(['version']))
@stfu_enabled
async def change_racista(_, message):
    global version, gus_api_ver
    await message.reply(f"**Gustavotron - Free**\n\n__Version__: {version}\n__Gustavo API Level__: {gus_api_ver}"
                        f"\n__Fela API Level__: {fela_ver}\n\n"
                        f"Licensed to Gustavo Fring (@NowPremiumUser)\n__For legal information and privacy policy "
                        f"contact @OnetimeUsername__")


@app.on_message(filters.command(['setracista']))
@stfu_enabled
async def change_racista(_, message):
    r = int(message.command[1])
    if r < 0 or r > 100:
        await message.reply(f"Unacceptable input: {r}%, the number should be between 0 and 100.")
        return
    set_racista_ratio(r)
    await message.reply(f"Racista ratio set to {r}%")


@app.on_message(filters.command(['r', 'racista']) & (filters.chat(["me", -1001874611480]) | filters.private))
@stfu_enabled
async def racista(_, message):
    await message.reply_to_message.reply("racista")


@app.on_message(filters.text | filters.chat([-1001874611480]))
@stfu_enabled
async def auto_racista(_, message):
    rand = random.randint(0, 100)
    if rand <= racista_ratio:
        await message.reply("racista")


app.run()
