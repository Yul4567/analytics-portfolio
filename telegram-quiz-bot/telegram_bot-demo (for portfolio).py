import telebot
import logging
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot('YOUR_TOKEN_HERE')

# Питання з варіантами і коментарями
questions = {
    0: {
        'question': "З чого зазвичай починаються найцікавіші пригоди?",
        'options': {
            'Із чаювання': "А як же без теплого початку?",
            'З ідеї!': "Саме так — усе починається з думки)",
            'З несподіванки': "О, інтрига — двигун життя!"
        }
    },
    1: {
        'question': "Яка подорож запам’ятається найбільше?",
        'options': {
            'Несподівана': "Вона завжди залишає слід!",
            'Планована': "Є свої переваги: і бюджет, і маршрут)",
            'Гастрономічна': "Що може бути краще за смачну мандрівку?"
        }
    },
    2: {
        'question': "Що обираєш на святковому столі?",
        'options': {
            'Щось новеньке': "Сміливо, експеримент — це шлях до відкриттів!",
            'Класичне': "Класика завжди в моді)",
            'Головне, щоб було смачно': "Справедливий підхід!"
        }
    },
    3: {
        'question': "Що зазвичай роблять після великої пригоди?",
        'options': {
            'Планують наступну': "Так тримаєш ритм пригод!)",
            'Розслабляються': "І відпочинок — частина мандрівки!",
            'Роблять альбом спогадів': "Чудова ідея для пам’яті)"
        }
    },
    4: {
        'question': "Який подарунок найприємніший?",
        'options': {
            'Той, що зроблений з душею': "Усе, що з турботою, — безцінне)",
            'Несподіваний': "Сюрприз — це завжди «вау» ефект!",
            'Той, що потрібен': "Практичність + увага — ідеальна формула!"
        }
    }
}

user_progress = {}

# Старт бота
@bot.message_handler(commands=['start'])
def start_game(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Почати гру"))
    bot.send_message(message.chat.id, 
        "Це інтерактивна гра з несподіванками! У ній немає неправильних відповідей — лише цікаві варіанти й сюрприз наприкінці :)",
        reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text == "Почати гру")
def begin_questions(message):
    user_progress[message.chat.id] = 0
    send_question(message.chat.id)

def send_question(chat_id):
    q_index = user_progress[chat_id]

    if q_index >= len(questions):
        show_final_message(chat_id)
        return

    q_data = questions[q_index]
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for option in q_data['options']:
        markup.add(option)

    bot.send_message(chat_id, q_data['question'], reply_markup=markup)

@bot.message_handler(func=lambda message: message.chat.id in user_progress)
def handle_response(message):
    chat_id = message.chat.id
    q_index = user_progress[chat_id]


    # Логування відповіді в реальному часі в консоль
    q_data = questions[q_index]
    user_answer = message.text
    print(f"Користувач {chat_id} відповів на запитання: '{q_data['question']}' вибором: '{user_answer}'")



 # Обробка відповіді
    if q_index >= len(questions):
        return

    if user_answer in q_data['options']:
        response = q_data['options'][user_answer]
        bot.send_message(chat_id, response)

        user_progress[chat_id] += 1

        # Перевіряємо: якщо це було останнє питання, показуємо фінал
        if user_progress[chat_id] >= len(questions):
            show_final_message(chat_id)
        else:
            send_question(chat_id)
    else:
        bot.send_message(chat_id, "Оберіть один з варіантів нижче :)")


def show_final_message(chat_id):

    bot.send_message(chat_id, 
        "Ти пройшов усю гру — вітаю! 🎉\nА тепер шукай сюрприз! 🔍")

    # Фото
    with open('123.jpg', 'rb') as photo:
        bot.send_photo(chat_id, photo=photo, caption='Підказка 👀')


# Зупиняємо гру, щоб більше не відправлялись питання
    del user_progress[chat_id]

# Кнопки для підказки
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("Треба!"),
        KeyboardButton("Не треба) вже знайшов)")
    )
    bot.send_message(chat_id, "Треба підказку?)", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Треба!", "Не треба) вже знайшов)"])
def handle_hint_request(message):
    chat_id = message.chat.id


    # Логування натискання кнопки "Треба підказку?" або "Не треба"
    print(f"Користувач {chat_id} натиснув кнопку: {message.text}")
    
    # Якщо користувач натиснув "Треба!"
    if message.text == "Треба!":
        bot.send_message(chat_id, "Спробуй пошукати на найвищому і найочевиднішому місці в кімнаті :)")

        # Додаємо кнопку "Знайшов!"
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton("Знайшов!"))
        bot.send_message(chat_id, "Якщо знайшов — натискай!", reply_markup=markup)

        # Якщо натиснута кнопка "Не треба)"
    elif message.text == "Не треба) вже знайшов)":
        bot.send_message(chat_id, "Молодець! 😘")

@bot.message_handler(func=lambda message: message.text == "Знайшов!")
def handle_found(message):
    chat_id = message.chat.id

    # Логування натискання кнопки "Знайшов!"
    print(f"Користувач {chat_id} натиснув кнопку: Знайшов!")

    bot.send_message(chat_id, "Молодець! 😘")

# Запуск
bot.polling()
