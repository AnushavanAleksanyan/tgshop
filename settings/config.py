import os
from emoji import emojize

TOKEN = "6401415271:AAHot77zVjngwpEi8bGHaX3onG2URlp-MDI"
# название БД
NAME_DB = 'products.sqlite'
# версия приложения
VERSION = '0.0.1'
# автор приложения
AUTHOR = 'User'

# родительская директория
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# путь до базы данных
DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)

COUNT = 0

# кнопки управления
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Կատալոգ'),
    'INFO': emojize(':speech_balloon: Մեր մասին'),
    'SETTINGS': emojize('⚙️ Կարգավորումներ'),
    'SEMIPRODUCT': emojize(':desktop_computer: Էլեկտրոնիկա'),
    'GROCERY': emojize(':house_with_garden: Անշարժ գույք'),
    'ICE_CREAM': emojize(':man_mechanic: Աշխատանք'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ՊԱՏՎԵՐ'),
    'X': emojize('❌'),
    'DOUWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLAY': '✅ Հաստատել պատվերը',
    'COPY': '©️'
}

# id категорий продуктов
CATEGORY = {
    'SEMIPRODUCT': 1,
    'GROCERY': 2,
    'ICE_CREAM': 3,
}

# названия команд
COMMANDS = {
    'START': "start",
    'HELP': "help",
}
