import config
import logging
from tokenize import Token
from config import TOKEN
import stick as st
import telebot
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
bot = telebot.TeleBot(config.TOKEN)
# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
SHOW_MENU, MENU, RULES, GAME, CANDY_COUNT, PER_TURN , PLAYER_TURN, COMPUTER_TURN = range(8)

# функция обратного вызова точки входа в разговор
def start(update, _):
    reply_keyboard = [['GO ➡']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    bot.send_sticker(update.message.chat.id, st.hello)
    update.message.reply_text(
        'Добро пожаловать в игру!''\n'
        '🍬 <КОНФЕТА> 🍬' '\n',
        reply_markup=markup_key)    
    return SHOW_MENU

def show_menu(update, _):
    user = update.message.from_user
    logger.info("Пользователь ввёл: %s: %f / %f", user.first_name, update.message.text)
    reply_keyboard = [['📜 Rules', '🎮 Game', '🚪 Exit']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    bot.send_sticker(update.message.chat.id, st.game )
    update.message.reply_text(
        'Давайте сыграем? ''\n' 
        'Но для начала, прочитайте правила нажав кнопку <Rules> или можете отказаться нажав <Exit>',
        reply_markup=markup_key)
    return MENU

def menu(update, _):
    user = update.message.from_user
    logger.info("Пользователь ввёл: %s: %f / %f", user.first_name, update.message.text)
    choice = update.message.text
    if choice == '📜 Rules':
        reply_keyboard = [['GO ➡']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text('Вперёд к знаниям!', reply_markup=markup_key)
        return RULES
    if choice == '🎮 Game':
        reply_keyboard = [['PlAY ▶']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text('Поехали!!!', reply_markup=markup_key)
        return GAME
    if choice == '🚪 Exit':
        return cancel(update, _)

def rules(update, _):
    user = update.message.from_user
    logger.info("Пользователь ввёл: %s: %f / %f", user.first_name, update.message.text)
    reply_keyboard = [['BACK ⬅']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text('Правила просты: Вы играете против бота.''\n' 
                              'Первый ход бот вежливо уступает вам.'
        'Тот, кто берет последнюю конфету 🍬 - проиграл!', reply_markup=markup_key)
    bot.send_sticker(update.message.chat.id, st.info)
    return SHOW_MENU

def game(update, _):
    user = update.message.from_user
    logger.info("Пользователь ввёл: %s: %f / %f", user.first_name, update.message.text)
    bot.send_sticker(update.message.chat.id, st.thinks )
    update.message.reply_text(
            'Для начала давайте определим, сколько всего у нас будет конфет? 🍬')
    return CANDY_COUNT

def candy_count(update, context):
    user = update.message.from_user
    logger.info("Кол-во конфет: %s: %s", user.first_name, update.message.text)
    candy_count = update.message.text
    if candy_count.isdigit():
        candy_count = int(candy_count)
        context.user_data['candy_count'] = candy_count
        update.message.reply_text(
            f'В куче {candy_count} конфет 🍬\n')
        update.message.reply_text(
            f'Введите кол-во конфет, которое можно забрать за ход.''\n'
            'Оно должно быть меньше общего колличества конфет в куче: ') 
        bot.send_sticker(update.message.chat.id, st.info)
        return PER_TURN
    else:
         bot.send_sticker(update.message.chat.id, st.error)
         update.message.reply_text(
            f'Вы ввели не число\n')
         

def per_turn(update, context):
    user = update.message.from_user
    logger.info("Кол-во конфет за ход %s: %s", user.first_name, update.message.text)
    candy_count = context.user_data.get('candy_count')
    turn_count = update.message.text
    if turn_count.isdigit():
        turn_count = int(turn_count)
        if candy_count > turn_count and turn_count > 0:
                context.user_data['turn_count'] = turn_count
                update.message.reply_text(
                    f'За ход можно брать от 1 до {turn_count} конфет\n')
                update.message.reply_text(
                f'Ваш ход. Введите число в диапазоне от 1 до {turn_count}: ')
                return PLAYER_TURN
        else:
               bot.send_sticker(update.message.chat.id, st.error)
               update.message.reply_text(f'Максимально допустимое значение {candy_count -1}') 
    else:
         bot.send_sticker(update.message.chat.id, st.error)
         update.message.reply_text(
            f'Вы ввели не число\n')



def player_turn(update, context):
    user = update.message.from_user
    logger.info(
        "Ход игрока %s: %f / %f", user.first_name, update.message.text)
    turn_count =context.user_data.get('turn_count')
    candy_count = context.user_data.get('candy_count')
    if candy_count < turn_count:
        turn_count = turn_count - (turn_count - candy_count)
    player_turn = update.message.text
    if player_turn.isdigit():
        player_turn = int(player_turn)
        if player_turn <= turn_count:
                candy_count -= player_turn
                if candy_count < 1:
                    reply_keyboard = [['Реванш ➡']]
                    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
                    bot.send_sticker(update.message.chat.id, st.win)
                    update.message.reply_text(
                        f'Игрок проиграл', reply_markup=markup_key) 
                    return SHOW_MENU 
                context.user_data['candy_count'] = candy_count
                update.message.reply_text(
                        f'Вы ввели {player_turn} конфет. В куче осталось {candy_count}: ')
                reply_keyboard = [['GO ➡']]
                markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
                bot.send_sticker(update.message.chat.id, st.thinks)
                update.message.reply_text(f'Внимание ходит бот...', reply_markup=markup_key)
                context.user_data['turn_count']=turn_count             
                return COMPUTER_TURN
        else:
                bot.send_sticker(update.message.chat.id, st.error)
                update.message.reply_text(
                        f'Максимально допустимое значение за ход - {turn_count}')    
    else:
        bot.send_sticker(update.message.chat.id, st.error)
        update.message.reply_text(
                        f'Нужно ввести число')


        
def computer_turn(update, context):
    turn_count = context.user_data.get('turn_count')
    candy_count = context.user_data.get('candy_count')
    if candy_count < turn_count:
        turn_count = turn_count - (turn_count - candy_count)
    if candy_count > 1:
        candy_count -= turn_count-1
    else:
        candy_count -= turn_count
    if candy_count <1:
        reply_keyboard = [['Урра! ➡']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        bot.send_sticker(update.message.chat.id, st.losses)
        update.message.reply_text(
                        f'Бот проиграл', reply_markup=markup_key)
        return SHOW_MENU 
    context.user_data['candy_count'] = candy_count
    update.message.reply_text(
            f'Бот походил на {turn_count-1} конфет. В куче осталось {candy_count}: ')
    update.message.reply_text(
            f'Ваш ход. Введите число в диапазоне от 1 до {turn_count}: ')
    context.user_data['turn_count']=turn_count            
    return PLAYER_TURN



# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    bot.send_sticker(update.message.chat.id, st.goodbye)
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            SHOW_MENU: [MessageHandler(Filters.text, show_menu)],
            MENU: [MessageHandler(Filters.text, menu)],
            RULES: [MessageHandler(Filters.text, rules)],
            GAME: [MessageHandler(Filters.text, game)],
            CANDY_COUNT:[MessageHandler(Filters.text, candy_count)],
            PER_TURN: [MessageHandler(Filters.text, per_turn)],
            PLAYER_TURN:[MessageHandler(Filters.text, player_turn)],
            COMPUTER_TURN: [MessageHandler(Filters.text, computer_turn)]
            },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    print('server started')
    updater.start_polling()
    updater.idle()