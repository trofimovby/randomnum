import random
import telebot

# создаем бота с помощью токена
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

# функция, которая генерирует случайное число от 1 до 100
def generate_number():
    return random.randint(1, 100)

# обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я загадал число от 1 до 100. Попробуй его угадать!')

    # генерируем число и сохраняем его в пользовательских данных
    user_data = bot.get_chat_member(message.chat.id, message.from_user.id)
    user_data.number = generate_number()

# обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def guess_number(message):
    # проверяем, является ли сообщение числом
    if not message.text.isdigit():
        bot.send_message(message.chat.id, 'Пожалуйста, введите число!')
        return

    # получаем загаданное число из пользовательских данных
    user_data = bot.get_chat_member(message.chat.id, message.from_user.id)
    number = user_data.number

    # проверяем, угадал ли пользователь число
    guess = int(message.text)
    if guess == number:
        bot.send_message(message.chat.id, 'Поздравляю, вы угадали число!')
        return

    # отправляем подсказку пользователю
    hint = 'Мое число ' + ('больше' if guess < number else 'меньше') + ' ' + str(guess)
    bot.send_message(message.chat.id, hint)

# запускаем бота
bot.polling(none_stop=True)
