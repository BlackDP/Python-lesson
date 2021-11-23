from telegram.ext import Updater, CommandHandler


def greet_user(update, context):
    print('Вызван /start')
    print (update)
    update.message.reply_text('Привет, ты начал общаться с ботом, вызвав /start')


def main():
    mybot = Updater('2036491217:AAEfksApd3IcVvmjxPscj_d7cMp3OomEyjM', use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))

    mybot.start_polling()
    mybot.idle()

main()
