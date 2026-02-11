from aiogram.utils.keyboard import ReplyKeyboardBuilder

def generate_user_info_confirmation_keyboard():
    keyboard = ReplyKeyboardBuilder()

    keyboard.button(text = "Ha")
    keyboard.button(text = "Yo'q")
    keyboard.adjust(2)

    return keyboard.as_markup(resize_keyboard=True)

