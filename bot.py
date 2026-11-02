
import os
import logging

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
    BotCommand
)

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
)

# ==================================
# IHope2U BOT CONFIGURATION
# ==================================

BOT_TOKEN = os.getenv("BOT_TOKEN")

WEB_APP_URL = "https://ihope2u.github.io/ihope2u-app/"

CONTACT_URL = os.getenv("CONTACT_URL", "")

# ==================================
# LOGGING
# ==================================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)


# ==================================
# MAIN MENU
# ==================================

def main_keyboard():

    buttons = [
        [
            InlineKeyboardButton(
                "🌐 OPEN IHOPE2U APP",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ],
        [
            InlineKeyboardButton(
                "📚 Education",
                url=WEB_APP_URL
            ),
            InlineKeyboardButton(
                "📰 News & Blogs",
                url=WEB_APP_URL
            )
        ],
        [
            InlineKeyboardButton(
                "ℹ️ About Us",
                callback_data="about"
            ),
            InlineKeyboardButton(
                "❓ Help",
                callback_data="help"
            )
        ]
    ]

    if CONTACT_URL.startswith("https://"):
        buttons.append([
            InlineKeyboardButton(
                "📩 Contact Us",
                url=CONTACT_URL
            )
        ])

    return InlineKeyboardMarkup(buttons)


# ==================================
# START COMMAND
# ==================================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user
    first_name = user.first_name if user else "Friend"

    message = (
        f"नमस्कार {first_name}! ❤️\n\n"
        "🌟 WELCOME TO IHOPE2U 🌟\n\n"
        "❤️ Your Hope, Our Support!\n\n"
        "IHope2U में आपका हार्दिक स्वागत है।\n\n"
        "यहाँ आपको मिलेगा:\n\n"
        "📚 शिक्षा और उपयोगी जानकारी\n"
        "📰 समाचार और अपडेट\n"
        "✍️ रोचक ब्लॉग और लेख\n"
        "🎬 मनोरंजन और वीडियो\n"
        "💡 ज्ञान और नई जानकारियाँ\n\n"
        "👇 हमारा App खोलने के लिए नीचे क्लिक करें।\n\n"
        "आपका स्वागत है! ❤️"
    )

    await update.message.reply_text(
        message,
        reply_markup=main_keyboard()
    )


# ==================================
# HELP COMMAND
# ==================================

async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    message = (
        "❓ IHope2U HELP CENTER\n\n"
        "हमारे Bot की कमांड:\n\n"
        "/start - Bot शुरू करें\n"
        "/help - सहायता प्राप्त करें\n"
        "/about - हमारे बारे में जानें\n"
        "/website - वेबसाइट खोलें\n"
        "/contact - संपर्क जानकारी\n\n"
        "किसी भी जानकारी के लिए हमारा App खोलें। ❤️"
    )

    await update.message.reply_text(
        message,
        reply_markup=main_keyboard()
    )


# ==================================
# ABOUT COMMAND
# ==================================

async def about(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    message = (
        "❤️ ABOUT IHOPE2U\n\n"
        "IHope2U एक डिजिटल प्लेटफॉर्म है।\n\n"
        "हमारा उद्देश्य शिक्षा, समाचार, "
        "जानकारी, ब्लॉग और मनोरंजन से जुड़ी "
        "उपयोगी सामग्री आप तक पहुँचाना है।\n\n"
        "🌟 Your Hope, Our Support!"
    )

    await update.message.reply_text(
        message,
        reply_markup=main_keyboard()
    )


# ==================================
# WEBSITE COMMAND
# ==================================

async def website(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🌐 Visit IHope2U",
                url=WEB_APP_URL
            )
        ]
    ])

    await update.message.reply_text(
        "IHope2U वेबसाइट खोलने के लिए नीचे क्लिक करें।",
        reply_markup=keyboard
    )


# ==================================
# CONTACT COMMAND
# ==================================

async def contact(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if CONTACT_URL.startswith("https://"):

        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "📩 Contact IHope2U",
                    url=CONTACT_URL
                )
            ]
        ])

        await update.message.reply_text(
            "हमसे संपर्क करने के लिए नीचे क्लिक करें।",
            reply_markup=keyboard
        )

    else:

        await update.message.reply_text(
            "📩 संपर्क लिंक अभी उपलब्ध नहीं है।"
        )


# ==================================
# BUTTON CALLBACKS
# ==================================

async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    if query.data == "about":

        await query.message.reply_text(
            "❤️ IHope2U शिक्षा, जानकारी और "
            "मनोरंजन से जुड़ी उपयोगी सामग्री "
            "उपलब्ध कराने का प्रयास करता है।"
        )

    elif query.data == "help":

        await query.message.reply_text(
            "सहायता के लिए /help कमांड भेजें।"
        )


# ==================================
# AUTO REPLY
# ==================================

async def auto_reply(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    message = (
        "नमस्कार! ❤️\n\n"
        "आपका संदेश IHope2U तक पहुँच गया है।\n\n"
        "हमारी वेबसाइट और सेवाओं के लिए "
        "नीचे दिए गए बटन पर क्लिक करें।"
    )

    await update.message.reply_text(
        message,
        reply_markup=main_keyboard()
    )


# ==================================
# BOT MENU COMMANDS
# ==================================

async def setup_commands(
    application: Application
):

    commands = [
        BotCommand("start", "Start IHope2U"),
        BotCommand("help", "Help Center"),
        BotCommand("about", "About IHope2U"),
        BotCommand("website", "Visit Website"),
        BotCommand("contact", "Contact Us")
    ]

    await application.bot.set_my_commands(commands)


# ==================================
# ERROR HANDLER
# ==================================

async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE
):

    logger.error(
        "Bot error: %s",
        context.error,
        exc_info=context.error
    )


# ==================================
# MAIN BOT
# ==================================

def main():

    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN environment variable missing!"
        )

    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(setup_commands)
        .build()
    )

    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        CommandHandler("help", help_command)
    )

    application.add_handler(
        CommandHandler("about", about)
    )

    application.add_handler(
        CommandHandler("website", website)
    )

    application.add_handler(
        CommandHandler("contact", contact)
    )

    application.add_handler(
        CallbackQueryHandler(button_handler)
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            auto_reply
        )
    )

    application.add_error_handler(error_handler)

    logger.info("IHope2U Bot started successfully!")

    application.run_polling(
        allowed_updates=Update.ALL_TYPES
    )


if __name__ == "__main__":
    main()
