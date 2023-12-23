from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("6772726500:AAEeGP9QvL6wmYDKgKSXmr6M90-dVJRqwUs").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()
