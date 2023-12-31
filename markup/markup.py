# импортируем специальные типы телеграм бота для создания элементов интерфейса
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup
# импортируем настройки и утилиты
from settings import config
# импортируем класс-менеджер для работы с библиотекой
from data_base.dbalchemy import DBManager


class Keyboards:
    """
    Класс Keyboards предназначен для создания и разметки интерфейса бота
    """
    # инициализация разметки

    def __init__(self):
        self.markup = None
        # инициализируем менеджер для работы с БД
        self.BD = DBManager()

    def set_btn(self, name, step=0, quantity=0):
        """
        Создает и возвращает кнопку по входным параметрам
        """

        return KeyboardButton(config.KEYBOARD[name])

    def start_menu(self):
        """
        Создает разметку кнопок в основном меню и возвращает разметку
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('CHOOSE_GOODS')
        itm_btn_2 = self.set_btn('INFO')
        itm_btn_3 = self.set_btn('SETTINGS')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2, itm_btn_3)
        return self.markup

    def info_menu(self):
        """
        Создает разметку кнопок в меню 'О магазине'
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup

    def settings_menu(self):
        """
        Создает разметку кнопок в меню 'Настройки'
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        # рассположение кнопок в меню
        self.markup.row(itm_btn_1)
        return self.markup

    @staticmethod
    def remove_menu():
        '''հեռացնում է կնօպկայի տվյալները և վերադարձնում'''
        return ReplyKeyboardRemove()

    def category_menu(self):
        '''ստեղծում է ապրանքների կատեգորիաների կնոպկաների ռազմետկա'''
        self.markup = ReplyKeyboardMarkup(True, True, row_width=1)
        self.markup.add(self.set_btn('SEMIPRODUCT'))
        self.markup.add(self.set_btn('GROCERY'))
        self.markup.add(self.set_btn('WORK'))
        self.markup.row(self.set_btn('<<'), self.set_btn('ORDER'))
        return self.markup

    @staticmethod
    def set_inline_btn(name):
        '''ստեղծում և վերադարձնում է inline կնոպկա'''
        return InlineKeyboardButton(str(name),
                                    callback_data=str(name.id))

    def set_select_category(self, category):
        ''' ընտրված կատեգորիայում օնլայն կնոպկաների համար ռազմետկաների պատրաստում և վերադարձ'''
        self.markup = InlineKeyboardMarkup(row_width=1)

        for itm in self.BD.select_all_products_category(category):
            self.markup.add(self.set_inline_btn(itm))

        return self.markup
