import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "🌟 Welcome to IHope2U!\n\n"
        "❤️ Your Hope, Our Support!\n\n"
        "शिक्षा, समाचार, ब्लॉग और मनोरंजन की दुनिया में आपका स्वागत है।\n\n"
        "🚀 हमारा ऐप खोलने के लिए नीचे IHope2U बटन दबाएँ।"
    )
    await update.message.reply_text(message)

app = Application.builder().token(os.environ["BOT_TOKEN"]).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
