BotToken="Replace with your bot token"
tags=['amateur', 'ass', 'onlyfans', 'cumshot', 'teen', 'pussy', 'cute', 'boobs', 'nsfw', 'asian', 'pov', 'doggystyle', 'sex', 'riding', 'orgasm', 'public', 'thick', 'petite', 'japanese', 'cosplay', 'rule34', 'hentai', 'solo', 'dildo', 'anal', 'cowgirl', 'missionary', 'creampie', 'homemade', 'JAV', 'legal teens', 'barely legal']
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from redgifs import API, Tags
import random
api = API().login()
def video(update: Update, context: CallbackContext) -> None:
    name = random.choice(tags) if not context.args else ' '.join(context.args)
    z=51
    x = random.randint(1,z)
    while z>1:
         try:
         	result = api.search(name, count=z)
         	gif=result.gifs[x]
         	video_url=gif.urls.sd
         	update.message.reply_video(video=video_url)
         	break
         except:
         	z=z-5
def main():
    updater = Updater(BotToken)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('video', video))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
