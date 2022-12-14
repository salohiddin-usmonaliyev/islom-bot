from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

region_keys = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="π Toshkent", callback_data="Toshkent"),
        InlineKeyboardButton(text="π Farg'ona", callback_data="Farg%27ΠΎna"),
    ],
    [
        InlineKeyboardButton(text="π Andijon", callback_data="Toshkent"),
        InlineKeyboardButton(text="π Namangan", callback_data="Farg%27ΠΎna"),
    ],
    [
        InlineKeyboardButton(text="π Samarqand", callback_data="Toshkent"),

    ],
    [
        InlineKeyboardButton(text="β Uashish", switch_inline_query="Namoz vaqtlari, Qurondagi 50 ta surani audiosi, Payg'ambarimiz mo'jizalari, Payg'ambarlar tarixini bilish uchun bot"),
    ],
    [
      InlineKeyboardButton("π Bosh Menyu", callback_data="mainmenu")
    ],
])
