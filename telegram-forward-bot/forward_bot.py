from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

BOT_TOKEN = '7659530956:AAFXJ62QEJqmLcurO7Txu-mTCWDeWexnzsg'
GROUP_CHAT_ID = -1002415844395

def forward_to_group(update: Update, context: CallbackContext):
    if update.message:
        context.bot.forward_message(
            chat_id=GROUP_CHAT_ID,
            from_chat_id=update.message.chat_id,
            message_id=update.message.message_id
        )

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_to_group))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
