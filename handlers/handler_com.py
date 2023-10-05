# импортируем класс родитель
from handlers.handler import Handler


class HandlerCommands(Handler):
    """
    Класс обрабатывает входящие команды /start и /help и т.п.
    """
    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_start(self, message):
        """
        обрабатывает входящие /start команды
        """
        self.bot.send_message(message.chat.id,
                              f'{message.from_user.first_name},'
                              f' здравствуйте! Жду дальнейших задач.',
                              reply_markup=self.keybords.start_menu())

    def handle(self):
        # обработчик(декоратор) сообщений,
        # который обрабатывает входящие /start команды.
        @self.bot.message_handler(commands=['start'])
        def handle(message):
            print(type(message))
            print(message)
            if message.text == '/start':
                self.pressed_btn_start(message)


# bot message
# {'content_type': 'text',
#  'id': 51,
#  'message_id': 51,
#  'from_user': {'id': 426114364,
#                'is_bot': False,
#                'first_name': 'Անուշավան',
#                'username': 'AleksanyanA',
#                'last_name': 'Ալեքսանյան',
#                'language_code': 'en',
#                'can_join_groups': None,
#                'can_read_all_group_messages': None,
#                'supports_inline_queries': None,
#                'is_premium': None,
#                'added_to_attachment_menu': None},
#  'date': 1696492016,
#  'chat': {'id': 426114364,
#           'type': 'private',
#           'title': None,
#           'username': 'AleksanyanA',
#           'first_name': 'Անուշավան',
#           'last_name': 'Ալեքսանյան',
#           'is_forum': None,
#           'photo': None,
#           'bio': None,
#           'join_to_send_messages': None,
#           'join_by_request': None,
#           'has_private_forwards': None,
#           'has_restricted_voice_and_video_messages': None,
#           'description': None, 'invite_link': None,
#           'pinned_message': None, 'permissions': None,
#           'slow_mode_delay': None,
#           'message_auto_delete_time': None,
#           'has_protected_content': None,
#           'sticker_set_name': None,
#           'can_set_sticker_set': None,
#           'linked_chat_id': None,
#           'location': None, 'active_usernames': None,
#           'emoji_status_custom_emoji_id': None,
#           'has_hidden_members': None,
#           'has_aggressive_anti_spam_enabled': None,
#           'emoji_status_expiration_date': None},
#  'sender_chat': None,
#  'forward_from': None,
#  'forward_from_chat': None,
#  'forward_from_message_id': None,
#  'forward_signature': None,
#  'forward_sender_name': None,
#  'forward_date': None,
#  'is_automatic_forward': None,
#  'reply_to_message': None,
#  'via_bot': None,
#  'edit_date': None,
#  'has_protected_content': None,
#  'media_group_id': None,
#  'author_signature': None,
#  'text': '/start',
#  'entities': [<telebot.types.MessageEntity object at 0x000002204634BC70>],
# 'caption_entities': None,
# 'audio': None, 'document': None, 'photo': None,
# 'sticker': None, 'video': None, 'video_note': None,
# 'voice': None, 'caption': None, 'contact': None,
# 'location': None, 'venue': None, 'animation': None,
# 'dice': None, 'new_chat_member': None,
# 'new_chat_members': None, 'left_chat_member': None,
# 'new_chat_title': None, 'new_chat_photo': None,
# 'delete_chat_photo': None, 'group_chat_created': None,
# 'supergroup_chat_created': None, 'channel_chat_created': None,
# 'migrate_to_chat_id': None, 'migrate_from_chat_id': None,
# 'pinned_message': None, 'invoice': None, 'successful_payment': None,
# 'connected_website': None, 'reply_markup': None, 'message_thread_id': None,
# 'is_topic_message': None, 'forum_topic_created': None,
# 'forum_topic_closed': None, 'forum_topic_reopened': None, 'has_media_spoiler': None,
# 'forum_topic_edited': None, 'general_forum_topic_hidden': None,
# 'general_forum_topic_unhidden': None, 'write_access_allowed': None,
# 'user_shared': None, 'chat_shared': None, 'story': None,
# 'json': {'message_id': 51,
#          'from': {'id': 426114364,
#                   'is_bot': False,
#                   'first_name': 'Անուշավան',
#                   'last_name': 'Ալեքսանյան',
#                   'username': 'AleksanyanA',
#                   'language_code': 'en'},
#          'chat': {'id': 426114364,
#                   'first_name': 'Անուշավան',
#                   'last_name': 'Ալեքսանյան',
#                   'username': 'AleksanyanA',
#                   'type': 'private'},
#          'date': 1696492016,
#          'text': '/start',
#          'entities': [{'offset': 0,
#                        'length': 6,
#                        'type': 'bot_command'}]}}
