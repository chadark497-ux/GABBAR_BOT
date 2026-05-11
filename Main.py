from telegram.ext import Application, CommandHandler

TOKEN = "YOUR_BOT_TOKEN"

async def start(update, context):
    await update.message.reply_text("Gabbar Music Bot 😎🎵")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
