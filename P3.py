bot = telebot.TeleBot("Your token")
video=cv2.VideoCapture(0)
run_app=Application(video)
run_app.loop2()
bot.polling(none_stop=True)