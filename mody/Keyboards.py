import os
from os import getenv
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import ReplyKeyboardRemove

Keyboard = ReplyKeyboardMarkup([
    [("اخفاء الكيبورد")],
    [("الاحصائيات")],
    [("تفعيل التواصل"), ("تعطيل التواصل")],
    [("• اوامر الاذاعة للخاص •")],
    [("اذاعة بالتثبيت"), ("اذاعة"), ("اذاعة بالتوجيه")],
    [("• اوامر الاذاعة بالجروبات •")],
    [("اذاعة بالمجموعات"), ("اذاعة بالتثبيت بالمجموعات")],
    [("تفعيل الاشتراك"), ("تعطيل الاشتراك")],
    [("ضع قناة الاشتراك"), ("حذف قناة الاشتراك")],
    [("قناة الاشتراك")],
    [("رفع ادمن"), ("تنزيل ادمن")],
    [("قائمه الأدمنيه")],
    [("المستخدمين"), ("الأدمنية"), ("الجروبات")],
    [("نقل ملكية البوت")],
    [("الغاء")]
], resize_keyboard=True)

fane = ReplyKeyboardMarkup([
    ["المطور", "مطور السورس"],
    ["السورس"],
    ["افتار شباب", "افتار بنات"],
    ["استوريهات 🥹"],
    ["النقشبندي", "قران"],
    ["فيلمك 🎥"],
    ["اقتباسات", "هيدرات"],
    ["غنيلي 🎙"],
    ["صوره", "انميي"],
    ["متحركه 🎬"],
    ["تويت", "صراحه"],
    ["نكته", "كتبات"],
    ["اذكار"],
    ["لو خيروك", "انصحني"],
    ["انصحني"],
    ["حساب العمر", "ابراج"],
    ["اخفاء الازرار 🕷"]
], resize_keyboard=True)

admins_commands = [
   'الاحصائيات', 'تفعيل التواصل',
   'تعطيل التواصل', 'اذاعة بالتثبيت', 'اذاعة',
   'اذاعة بالتوجيه', 'تفعيل الاشتراك', 'تعطيل الاشتراك',
   'ضع قناة الاشتراك', 'حذف قناة الاشتراك', 'قناة الاشتراك','قائمه الأدمنيه',
   'المستخدمين', 'الأدمنية', 'الجروبات',
   'اذاعة بالمجموعات','اذاعة بالتثبيت بالمجموعات', 'اخفاء الكيبورد'
   ]
   
owner_commands = [
   'نقل ملكية البوت', 'رفع ادمن', 'تنزيل ادمن'
]

keyboard_Azann = [
    [
        InlineKeyboardButton("السعودية 🇸🇦", callback_data='Azann saudi_arabia-riyadh'),
        InlineKeyboardButton("مصر 🇪🇬", callback_data='Azann egypt-cairo')
    ],
    [
        InlineKeyboardButton("سوريا 🇸🇾", callback_data='Azann syria-damascus'),
        InlineKeyboardButton("العراق 🇮🇶", callback_data='Azann iraq-baghdad')
    ],
    [
        InlineKeyboardButton("الجزائر 🇩🇿", callback_data='Azann algeria-algiers'),
        InlineKeyboardButton("المغرب 🇲🇦", callback_data='Azann morocco-rabat')
    ],
    [
        InlineKeyboardButton("تونس 🇹🇳", callback_data='Azann tunisia-tunis'),
        InlineKeyboardButton("الإمارات 🇦🇪", callback_data='Azann uae-abu_dhabi')
    ],
    [
        InlineKeyboardButton("قطر 🇶🇦", callback_data='Azann qatar-doha'),
        InlineKeyboardButton("الكويت 🇰🇼", callback_data='Azann kuwait-kuwait_city')
    ],
    [
        InlineKeyboardButton("الأردن 🇯🇴", callback_data='Azann jordan-amman'),
        InlineKeyboardButton("فلسطين 🇵🇸", callback_data='Azann palestine-jerusalem')
    ],
    [
        InlineKeyboardButton("لبنان 🇱🇧", callback_data='Azann lebanon-beirut'),
        InlineKeyboardButton("موريتانيا 🇲🇷", callback_data='Azann mauritania-nouakchott')
    ],
    [
        InlineKeyboardButton("جيبوتي 🇩🇯", callback_data='Azann djibouti-djibouti_city'),
        InlineKeyboardButton("الصومال 🇸🇴", callback_data='Azann somalia-mogadishu')
    ],
    [
        InlineKeyboardButton("السودان 🇸🇩", callback_data='Azann sudan-khartoum')
    ]
]


video_url = getenv(
    "video_url",
    "https://telegra.ph/file/497649408d404270450b5.mp4",
)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/xxStitch")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/iwiwwiq")
DEV_SOURCE = getenv("DEV_SOURCE", "https://t.me/U_D_8")

New = InlineKeyboardButton("By", url=f"https://t.me/U_D_8")
dev = InlineKeyboardButton("丂丨几丂", url=f"https://t.me/xxStitch")
UD = InlineKeyboardMarkup(inline_keyboard=[
    [New],
    [dev]
])

subs = InlineKeyboardMarkup(
        [
            [
                dev,
            ],
        ]
    )