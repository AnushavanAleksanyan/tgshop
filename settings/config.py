import os
from emoji import emojize

TOKEN = ""

NAME_DB ='products.sqlite'

VERSION = '0.0.1'

AUTHOR = 'User'

BASE_DIR = os.path.dirname(os.path.abspath((__file__)))

DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)

COUNT = 0

KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Ընտրել ապրանքը'),
    'INFO': emojize(':speach_baloon: Խանութի մասին'),
    'SETTINGS': emojize('⚙ Կարգավորումներ'),
    'SEMIPRODUCT': emojize(':pizza: Կիսաֆաբրիկատներ'),
    'GROCERY': emojize(':bread: Հացաբուլկեղեն'),
    'ICE_CREAM': emojize(':shaved_ice: Պաղպաղակ'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'APPLY': '✅ Հաստատել պատվերը',
}

CATEGORY = {
    'SEMIPRODUCT': 1,
    'GROCERY': 2,
    'ICE_CREAM': 3,
}

COMMANDS = {
    'START': "start",
    'HELP': "help",
}