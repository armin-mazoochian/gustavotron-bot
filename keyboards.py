from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

INLINE_KEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "Mention All",
                callback_data="data"
            ),
            InlineKeyboardButton(
                "Version",
                callback_data="version"
            ),
        ],
        [
            InlineKeyboardButton(
                "Enable/Disable STFU",
                callback_data="stfu_enable"
            )
        ]
    ]
)

REPLY_KEYBOARD = ReplyKeyboardMarkup(
    [
        ["Help", "Version"],
    ],
)
