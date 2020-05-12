# -*- coding: utf8 -*-
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
from random import *
import time
import cats
import requests
import tr
import vk
import sqlite3
import weather
from datetime import *

# подключение библиотек


token = "ce9dddf205929c95f0a68d1a818b43275645257a8e6b476828db4466e8305ca998a8ee48a249a3416c160"  # токен
vk_session = vk_api.VkApi(token=token)
dname = {}  # словарь имен пользователей от айди_вк
dage = {}  # словарь возраста от айди_вк
dlike = {}  # словарь того, что пользователь "любит" от айди_вк
duvl = {}  # словарь увлечений пользователей от айди_вк
dm = {}  # словарь любителей музыки от айди_вк
df = {}  # словарь любителей фильмов от айди_вк
session_api = vk_session.get_api()
con = sqlite3.connect("TableBot.db")  # подключение к бд

# Создание курсора
cur = con.cursor()

longpoll = VkLongPoll(vk_session)

spm = ['Мгновение – это одна сотая секунды',
       'Число 18 – уникальное. Сумма его цифр (1+8) вдвое меньше его самого. Больше подобных чисел нет',
       'Первой женщиной-математиком считается Гипатия из Александрии',
       ' Знак равенства появился относительно недавно, в 16 веке',
       'В столице Тайвани, городе Тайбэй официально разрешено не использовать число 4. Всё потому, что оно созвучно со '
       'словом «смерть». Во многих тайванских домах после третьего этажа сразу идёт пятый',
       'Известный математик современности Стивен Хокинг изучал царицу наук только в школе. Впоследствии, став преподав'
       'ателем в университете, он просто читал учебник перед занятием, а потом доносил эту информацию студентам',
       'Софья Ковалевская-Кюри вступила в фиктивный брак, чтобы иметь возможность заниматься математикой',
       'В счете древних римлян отсутствовало число 0. До сих пор записать римскими цифрами число 0 невозможно',
       'Все, наверное, слышали историю о студенте, опоздавшем на занятия. Увидев на доске условия задач, он решил, чт'
       'о это домашнее задание. Уравнения показались студенту немного сложнее предыдущих, но, поднапрягшись, он смог н'
       'айти решение. Так обычный учащийся Джордж Данциг решил задачи, над которыми несколько десятилетий бились велича'
       'йшие математики мира',
       'Отрицательные числа появились в 19 веке', 'Древние египтяне не пользовались дробями и таблицей умножения',
       'Первые квадратные уравнения появились в Индии в 6 веке',
       'Все слышали о математических трудах Эвклида. Некоторыми его работами пользуются до сих пор. Но какие-либо свед'
       'ения о личности Эвклида отсутствуют',
       'Существует легенда, что жена Альфреда Нобеля ушла от него к математику. Поэтому Нобель запретил вручать премию '
       'его имени представителям этой точной науки',
       'Первое использование числа Пи датируется 6 веком, и сделал это индийский учёный Будхайяна',
       'Известные нам знаки плюс и минус впервые использовал Ян Видман 500 лет назад',
       'Центилион – самое большое число из всех существующих',
       'Десятичную систему исчисления взяли на вооружение из-за количества пальцев на руках человека',
       '0 – единственное из существующих чисел, имеющее несколько названий',
       '«Алгебра» на всех языках мира звучит одинаково',
       'Автор «Алисы в стране чудес», знаменитый писатель Льюис Кэрролл был еще и неплохим математиком']
# список фактов по математике
d = {1: 'балл', 2: 'балла', 3: 'балла', 4: 'балла',
     5: 'баллов'}  # словарь для определения окончания при определении баллов за тест по информатике и математике
spi = [
    'Сначала информатикой называлась только техническая область, осуществляющая автоматическую обработку информации '
    'при помощи ЭВМ',
    'День программиста празднуется 13 сентября', 'Самой популярной социальной сетью является Фейсбук',
    'В 1936 году появилось слово «спам»', 'Электронную почту создали в 1971 году',
    'Сначала информатикой называлась только техническая область, осуществляющая автоматическую обработку информации '
    'при помощи ЭВМ',
    'Электронная вычислительная машина впервые была зарегистрирована в 1948 году и создана она была Рамеевым',
    'Электронная вычислительная машина создавалась на протяжении полугода, а логические схемы в ней были созданы '
    'на полупроводниках',
    'В 60-е годы был создан Интернет', 'Около 3-х миллиардов фото ежемесячно пользователи выкладывают в сети Фейсбук',
    'За всю историю информатики удалось выявить самый разрушительный вирус – LoveLetter',
    'Самой крупной и первой компьютерной атакой была та, которая называлась «Червь Морриса». Она нанесла ущерб '
    ''
    'примерно '
    '96 миллионов долларов']
# факты по информатике
flagi = False  # флаг информатика, чтобы узнать балл
flagm = False  # флаг математика, чтобы узнать балл
markm = {}  # баллы по математике
marki = {}  # баллы по информатике
ii = 0  # счетчик ответов по информатике
spmuz = ['audio307228931_456239299', 'audio307228931_456239303', 'audio-2001661968_64661968',
         'audio188106561_456240522', 'audio310497532_456239462', 'audio307228931_456239212', 'audio307228931_456239213',
         'audio307228931_456239216', 'audio307228931_456239249', 'audio307228931_456239261', 'audio307228931_456239266',
         'audio307228931_456239267', 'audio307228931_456239274', 'audio307228931_456239277', 'audio307228931_456239285',
         'audio307228931_456239290', 'audio307228931_456239295', 'audio307228931_456239293', 'audio307228931_456239294',
         'audio307228931_456239416', 'audio307228931_456239415', 'audio307228931_456239414', 'audio307228931_456239412',
         'audio307228931_456239407', 'audio307228931_456239403', 'audio307228931_456239396', 'audio307228931_456239393',
         'audio307228931_456239392', 'audio307228931_456239391', 'audio307228931_456239390', 'audio307228931_456239389',
         'audio307228931_456239387', 'audio307228931_456239386', 'audio307228931_456239380', 'audio307228931_45623937',
         'audio307228931_456239374', 'audio307228931_456239371', 'audio307228931_456239370', 'audio307228931_456239369',
         'audio307228931_456239366', 'audio307228931_456239365', 'audio307228931_456239351', 'audio307228931_456239353',
         'audio307228931_456239349', 'audio307228931_456239347', 'audio307228931_456239346', 'audio307228931_456239336',
         'audio307228931_456239321', 'audio307228931_456239319', 'audio307228931_456239305', 'audio295863990_456240883',
         'audio295863990_456240889', 'audio295863990_456240874', 'audio295863990_456240847', 'audio295863990_456240832',
         'audio295863990_456240825', 'audio295863990_456240814', 'audio295863990_456240813', 'audio295863990_456240776',
         'audio295863990_456240773', 'audio295863990_456240757']
# аудиозаписи для раздела музыка
spfilms = ['video-34542655_456250599', 'video-34542655_456250598', 'video-34542655_456250596',
           'video-34542655_456250592', 'video-34542655_456250583', 'video-34542655_456250578',
           'video-34542655_456250570', 'video-34542655_456250569', 'video-34542655_456250563',
           'video-34542655_456250570', 'video-34542655_456250569', 'video-34542655_456250563',
           'video-34542655_456250562', 'video-34542655_456250558', 'video-34542655_456250557',
           'video-34542655_456250555', 'video-34542655_456250549', 'video-34542655_456250548',
           'video-34542655_456250544', 'video-34542655_456250539', 'video-34542655_456250529',
           'video-34542655_456250527', 'video-34542655_456250524', 'video-34542655_456250518',
           'video-34542655_456250516', 'video-34542655_456250489', 'video-34542655_456250478',
           'video-34542655_456250475', 'video-34542655_456250463']


# трейлеры для фильмов в разделе фильмы

# функция для определения даты ивремени в прогнозе погоды
def tt():
    return datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")


# функция, в которой создаются клавиатуру бота по сообщению от пользователя
def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)
    if response == 'список возможностей' or response == 'открыть' or response == 'вернуться' or response == '/talk':

        keyboard.add_button('Развлечения', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Моя анкета', color=VkKeyboardColor.DEFAULT)

        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('Кто мы?', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Котики', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()
        keyboard.add_button('Закрыть клавиатуру', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Выход', color=VkKeyboardColor.PRIMARY)

    elif response == 'привет':
        keyboard.add_button('Список возможностей', color=VkKeyboardColor.POSITIVE)

    elif response == 'выход' or response == 'пока':
        keyboard.add_button('Список возможностей', color=VkKeyboardColor.POSITIVE)

    elif response == 'котики' or response == 'ещё котиков!':
        keyboard.add_button('Ещё котиков!', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == 'закрыть клавиатуру':
        return keyboard.get_empty_keyboard()

    elif response == 'игры':
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == 'развлечения':
        keyboard.add_button('Знания', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Рассказ', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Мне понравится', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Переводчик', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Рандомное число', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Погода', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('/talk', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == 'переводчик':
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == 'знания':
        keyboard.add_button('Математика', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Информатика', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('Текущие баллы', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == 'математика':
        keyboard.add_button('Задачки', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Интересные факты', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == 'интересные факты' or response == 'дальше':
        keyboard.add_button('Дальше', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == 'задачки':
        keyboard.add_button('12', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('14', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == '12' or response == '14':
        keyboard.add_button('Гедель', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Евклид', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == 'гедель' or response == 'евклид':
        keyboard.add_button('18', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('20', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == '18' or response == '20':
        keyboard.add_button('32', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('33', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == '32' or response == '33':
        keyboard.add_button('Декарт', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Пифагор', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == 'декарт' or response == 'пифагор':
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == 'информатика':
        keyboard.add_button('Задачки из ОГЭ', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Факты', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == 'факты' or response == 'далее':
        keyboard.add_button('Далее', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == 'задачки из огэ':
        keyboard.add_button('16', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('44', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == '16' or response == '44':
        keyboard.add_button('ГБВА', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('ГВБА', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == 'гбва' or response == 'гвба':
        keyboard.add_button('1000', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('950', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == '950' or response == '1000':
        keyboard.add_button('4', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('3', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == '3' or response == '4':
        keyboard.add_button('10', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('2', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == '10' or response == '2':
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == 'рассказ':
        keyboard.add_button('Будни (Ekaterina PERONNE)', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Рэй Брэдбери «Крик из-под земли»', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == 'рэй брэдбери «крик из-под земли»':
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == 'будни (ekaterina peronne)':
        keyboard.add_button('1 часть', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('2 часть', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == '1 часть' or response == '2 часть':
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == 'рандомное число':
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif response == 'моя анкета':
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif "люблю" == response[0:5] or 'мне понравится' in response:
        keyboard.add_button('Музыка', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Фильмы', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Книги', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif 'фильмы' in response or 'ещё' == response:
        keyboard.add_button('Ещё', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)
        if event.user_id not in df:
            df[event.user_id] = ''

    elif 'музыка' in response or 'хочу ещё' in response:
        keyboard.add_button('Хочу ещё', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)
        if event.user_id not in dm:
            dm[event.user_id] = ''

    elif 'книги' in response:
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    elif 'погода' == response or 'город' in response:
        keyboard.add_button('Город: Москва', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Город: Липецк', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Город: Санкт-Петербург', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

    keyboard = keyboard.get_keyboard()
    return keyboard


# функция, которая отправляет сообщения от бота
def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',
                      {id_type: id, 'message': message, 'random_id': 0, "attachment": attachment, 'keyboard': keyboard})


matem = 0  # счетчик ответов по математике
# цикл для приема и обрабатывания сообщений
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        '''print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        print(event.user_id)
        для отладки сообщения от бота и от пользователя показывались прямо в консоле в пайчарме'''
        response = event.text.lower()
        keyboard = create_keyboard(response)
        # условия обработки сообщений

        if event.from_user and not event.from_me:
            if response == "котики":
                attachment = cats.get(vk_session, session_api)
                send_message(vk_session, 'user_id', event.user_id, message='Держи котиков!', attachment=attachment,
                             keyboard=keyboard)
            elif response == "привет":
                send_message(vk_session, 'user_id', event.user_id,
                             message='', attachment='doc-165897409_472967931')
                send_message(vk_session, 'user_id', event.user_id,
                             message='Привет, я GamesBot, напиши "Имя:", а затем как тебя зовут, для того, '
                                     'что бы узнать, что я могу - нажми на кнопку.',
                             keyboard=keyboard)
            elif response == "выход" or response == "пока":
                send_message(vk_session, 'user_id', event.user_id, message='До скорого. Нажми на кнопку, чтобы начать.',
                             keyboard=keyboard)
            elif response == "список возможностей":
                send_message(vk_session, 'user_id', event.user_id,
                             message='Выбирай!) Если хочешь поболтать напиши "/talk"', keyboard=keyboard)
            elif response == 'команды':
                send_message(vk_session, 'user_id', event.user_id,
                             message='Список команд бота: \n \n 1)Команда1 \n 2)Команда2')

            elif response == 'закрыть клавиатуру':
                send_message(vk_session, 'user_id', event.user_id,
                             message='Уже убрали, если захочешь открыть то просто напиши "открыть"', keyboard=keyboard)
            elif response == 'открыть':
                send_message(vk_session, 'user_id', event.user_id, message='Сделано', keyboard=keyboard)
            elif response == 'игры':
                send_message(vk_session, 'user_id', event.user_id, message='Давайте попробуем', keyboard=keyboard)
            elif response == 'кто мы?':
                send_message(vk_session, 'user_id', event.user_id,
                             message='Это бот, с которым ты можешь повесилиться, поболтать или поиграть.'
                                     ' Я сделан в рамках проекта для Яндекс.Лицея, если будут еще вопросы, '
                                     'то мы непременно ответим на них позже.')
            elif response == 'вернуться':
                send_message(vk_session, 'user_id', event.user_id, message='Окей', keyboard=keyboard)
            elif response == 'ещё котиков!':
                attachment = cats.get(vk_session, session_api)
                send_message(vk_session, 'user_id', event.user_id, message='Держи котиков)', attachment=attachment,
                             keyboard=keyboard)
            elif response == 'развлечения':
                send_message(vk_session, 'user_id', event.user_id, message='Вы можете выбрать занятие по душе',
                             keyboard=keyboard)
            elif response == 'знания':
                send_message(vk_session, 'user_id', event.user_id,
                             message='', attachment='doc-165897409_472964477')
                send_message(vk_session, 'user_id', event.user_id,
                             message='Вы можете решить задания по математике или информатике',
                             keyboard=keyboard)
            elif response == 'математика':
                send_message(vk_session, 'user_id', event.user_id, message='Выберите: задачки или интересные факты',
                             keyboard=keyboard)
            elif response == 'задачки':
                send_message(vk_session, 'user_id', event.user_id,
                             message='Итак, первый вопрос. Чему равен корень из 144?', keyboard=keyboard)
            elif response == '12':
                matem += 1
                send_message(vk_session, 'user_id', event.user_id, message='Верно! Автор книги «Начала»?',
                             keyboard=keyboard)
            elif response == '14':
                send_message(vk_session, 'user_id', event.user_id, message='Вы ошиблись. Автор книги «Начала»?',
                             keyboard=keyboard)
            elif response == 'гедель':
                send_message(vk_session, 'user_id', event.user_id,
                             message='Неверно. В школьный буфет привезли два лотка с булочками.'
                                     ' На одном лотке было 40 булочек, на другом — 35. '
                                     'За первую перемену продали 57 булочек. Сколько булочек осталось?',
                             keyboard=keyboard)
            elif response == 'евклид':
                matem += 1
                send_message(vk_session, 'user_id', event.user_id,
                             message='Правильно! В школьный буфет привезли два лотка с булочками.'
                                     ' На одном лотке было 40 булочек, на другом — 35. '
                                     'За первую перемену продали 57 булочек. Сколько булочек осталось?',
                             keyboard=keyboard)
            elif response == '18':
                matem += 1
                send_message(vk_session, 'user_id', event.user_id,
                             message='Да вы гений! Оля решила нарисовать 72 букета. '
                                     'В понедельник она нарисовала 18 букетов, во вторник — 22 букета. '
                                     'Сколько букетов Оля не стала рисовать?',
                             keyboard=keyboard)
            elif response == '20':
                send_message(vk_session, 'user_id', event.user_id,
                             message='Ошибка. Далее: Оля решила нарисовать 72 букета. '
                                     'В понедельник она нарисовала 18 букетов, во вторник — 22 букета.'
                                     ' Сколько букетов Оля не стала рисовать?',
                             keyboard=keyboard)
            elif response == '32':
                matem += 1
                send_message(vk_session, 'user_id', event.user_id,
                             message='Супер! Великий учёный, чьё имя теперь носит прямоугольная система координат?',
                             keyboard=keyboard)
            elif response == '33':
                send_message(vk_session, 'user_id', event.user_id,
                             message='Не-а. Великий учёный, чьё имя теперь носит прямоугольная система координат?',
                             keyboard=keyboard)
            elif response == 'декарт':
                matem += 1
                flagm = True
                send_message(vk_session, 'user_id', event.user_id, message='Верно!',
                             keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message=f'Вы набрали {matem} {d[matem]}',
                             keyboard=keyboard)
                markm[event.user_id] = matem
                matem = 0
            elif response == 'пифагор':
                flagm = True
                send_message(vk_session, 'user_id', event.user_id, message='Вы ошиблись',
                             keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message=f'Вы набрали {matem} {d[matem]}',
                             keyboard=keyboard)
                markm[event.user_id] = matem
                matem = 0
            elif response == 'интересные факты' or response == 'дальше':
                k = randint(0, 20)
                send_message(vk_session, 'user_id', event.user_id, message=spm[k], keyboard=keyboard)
            elif response == 'информатика':
                send_message(vk_session, 'user_id', event.user_id, message='Выбирайте', keyboard=keyboard)
            elif response == 'факты' or response == 'далее':
                kk = randint(0, 11)
                send_message(vk_session, 'user_id', event.user_id, message=spi[kk], keyboard=keyboard)
            elif response == 'задачки из огэ':
                send_message(vk_session, 'user_id', event.user_id,
                             message='Напишите наибольшее целое число x, для которого истинно высказывание'
                                     ' \n (x < 17) И НЕ (x > 44)',
                             keyboard=keyboard)
            elif response == '16':
                ii += 1
                send_message(vk_session, 'user_id', event.user_id,
                             message='Верно! Костя записал IP-адрес школьного сервера на листке бумаги и положил его в '
                                     'карман куртки. Костина мама случайно постирала куртку вместе с запиской. '
                                     'После сти'
                                     'рки Костя обнаружил в кармане четыре обрывка с фрагментами IP-адреса. '
                                     'Эти фрагмент'
                                     'ы обозначены буквами А, Б, В и Г: А: .33, Б: 3.232, В: 3.20, Г: 23, восстановите'
                                     ' IP-адрес. В ответе укажите последовательность букв, обозначающих фрагменты, в '
                                     'порядке, соответствующем IP-адресу.',
                             keyboard=keyboard)
            elif response == '44':
                send_message(vk_session, 'user_id', event.user_id,
                             message='Ошибка. Костя записал IP-адрес школьного сервера на листке бумаги и положил'
                                     ' его в карман куртки. Костина мама случайно постирала куртку вместе с запиской. '
                                     'После стирки Костя обнаружил в кармане четыре обрывка с фрагментами IP-адреса. '
                                     'Эти фрагменты обозначены буквами А, Б, В и Г: А: .33, Б: 3.232, В: 3.20, Г: 23, '
                                     'восстановите IP-адрес. В ответе укажите последовательность букв, обозначающих '
                                     'фрагменты, в порядке, соответствующем IP-адресу.',
                             keyboard=keyboard)
            elif response == 'гвба':
                ii += 1
                send_message(vk_session, 'user_id', event.user_id,
                             message='Абсолютно верно. В языке запросов поискового севера для обозначения '
                                     'логических операций «ИЛИ» используется символ «|», а для обозначения логической '
                                     'операции «И» — символ «&». Зима & Средиземноморье -340, Зима - 560, '
                                     'Средиземноморье - 780. Какое количество страниц (в тысячах) будет найдено '
                                     'по запросу Зима | Средиземноморье?',
                             keyboard=keyboard)
            elif response == 'гбва':
                send_message(vk_session, 'user_id', event.user_id,
                             message='Неправильно. В языке запросов поискового севера для обозначения логических'
                                     ' операций «ИЛИ» используется символ «|», а для обозначения логической операции '
                                     '«И» — символ «&». Зима & Средиземноморье -340, Зима - 560, Средиземноморье - 780.'
                                     ' Какое количество страниц (в тысячах) будет найдено '
                                     'по запросу Зима | Средиземноморье?',
                             keyboard=keyboard)
            elif response == '1000':
                ii += 1
                send_message(vk_session, 'user_id', event.user_id,
                             message='Молодец. У исполнителя Альфа две команды. которым присвоены номера: '
                                     '\n 1. Вычти b \n 2. Умножь на 5 (b — неизвестно натуральное число). '
                                     'Выполняя первую из них, Альфа уменьшает число на экране на b, а выполняя вторую,'
                                     ' умножает это число на 5. Программа для исполнителя Альфа — это'
                                     ' последовательность номеров команд. Известно, что программа 21121 переводит '
                                     'число 2 в число 17. Определите значение b.',
                             keyboard=keyboard)
            elif response == '950':
                send_message(vk_session, 'user_id', event.user_id,
                             message='Не так. У исполнителя Альфа две команды. которым присвоены номера: '
                                     '\n 1. Вычти b \n 2. Умножь на 5 (b — неизвестно натуральное число). '
                                     'Выполняя первую из них, Альфа уменьшает число на экране на b, а выполняя вторую,'
                                     ' умножает это число на 5. Программа для исполнителя Альфа — это '
                                     'последовательность номеров команд. Известно, что программа 21121 переводит '
                                     'число 2 в число 17. Определите значение b.',
                             keyboard=keyboard)
            elif response == '3':
                ii += 1
                send_message(vk_session, 'user_id', event.user_id,
                             message='Прекрасно. Напишите наименьшее целое число x, для которого истинно высказывание: '
                                     '\n НЕ (X < 2) И НЕ (X > 10).',
                             keyboard=keyboard)
            elif response == '4':
                send_message(vk_session, 'user_id', event.user_id,
                             message='Ошибочка. Напишите наименьшее целое число x, для которого истинно высказывание: '
                                     '\n НЕ (X < 2) И НЕ (X > 10).',
                             keyboard=keyboard)
            elif response == '2':
                ii += 1
                flagi = True
                send_message(vk_session, 'user_id', event.user_id, message='Верно!',
                             keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message=f'Вы набрали {ii} {d[ii]}',
                             keyboard=keyboard)
                marki[event.user_id] = ii
                ii = 0
            elif response == '10':
                flagi = True
                send_message(vk_session, 'user_id', event.user_id, message='Вы ошиблись!',
                             keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message=f'Вы набрали {ii} {d[ii]}',
                             keyboard=keyboard)
                marki[event.user_id] = ii
                ii = 0
            elif response == 'рассказ':
                send_message(vk_session, 'user_id', event.user_id, message='', attachment='doc-165897409_472967988')
                send_message(vk_session, 'user_id', event.user_id, message='Выбирай', keyboard=keyboard)
            elif response == 'будни (ekaterina peronne)':
                send_message(vk_session, 'user_id', event.user_id, message='Какую часть?', keyboard=keyboard)
            elif response == '1 часть':
                send_message(vk_session, 'user_id', event.user_id, message='', attachment='wall-194519120_329',
                             keyboard=keyboard)
            elif response == '2 часть':
                send_message(vk_session, 'user_id', event.user_id, message='', attachment='wall-194519120_330',
                             keyboard=keyboard)
            elif response == 'переводчик':
                send_message(vk_session, 'user_id', event.user_id,
                             message='Напишите "Перевести:", а затем через пробел слово или фразу, которую хотите '
                                     'перевести на английский язык. После нее через пробел пишете либо "ru-en", '
                                     'либо "en-ru", смотря с какого языка вы переводите. Итоговый ввод примерно такой:'
                                     ' "Перевести: Яндекс.Лицей ru-en"',
                             keyboard=keyboard)
            elif "перевести:" in response:
                lang = response[len(response) - 5:]
                phrase = response[11:len(response) - 6]
                print(phrase)
                perev = tr.translate_me(phrase, lang)
                send_message(vk_session, 'user_id', event.user_id, message=''.join(perev["text"]))
            elif response == 'рандомное число':
                send_message(vk_session, 'user_id', event.user_id, message='Введите диапазон в формате (x1;x2) ',
                             keyboard=keyboard)
            elif '(' in response and ')' in response:
                response = response.split(';')
                f = int(response[0][1:])
                sec = int(response[1][:-1])
                send_message(vk_session, 'user_id', event.user_id, message=f'Ваше число: {randint(f, sec)}')
            elif response == '/talk':
                attachment = 'photo-159262407_456239042'
                if event.user_id in dname:
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=f'{dname[event.user_id]}, Вы вынуждаете меня с вами поговорить, ну давайте. '
                                         f'Для начала давайте узнаем друг друга. Что вы любите? Напишите "люблю:" и  '
                                         f'перечисляйте',
                                 attachment=attachment, keyboard=keyboard)
                else:
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=f'Вы вынуждаете меня с вами поговорить, ну давайте. Для начала давайте узнаем '
                                         f'друг друга. Что вы любите? Напишите "люблю:" и  перечисляйте',
                                 attachment=attachment, keyboard=keyboard)
            elif "имя:" in response:
                kname = response[5:]
                dname[event.user_id] = kname[0].upper() + kname[1:]
                send_message(vk_session, 'user_id', event.user_id,
                             message=f'Рад познакомиться, {dname[event.user_id]}, теперь введи свой возраст '
                                     f'в формате "9 лет"')
            elif 'лет' in response:
                age = response.split()[0]
                dage[event.user_id] = age
                send_message(vk_session, 'user_id', event.user_id,
                             message='Ох. Вы же знали, что пожилым людям сейчас лучше сидеть дома?!')
                send_message(vk_session, 'user_id', event.user_id,
                             message='Сведения о себе можете узнать в разделе "Моя анкета"')
            elif response == 'моя анкета':
                attachment = 'photo-188759640_457239018'
                if event.user_id in dname and event.user_id in dage:
                    result = cur.execute(
                        """select id_vk from saveinfo""")  # запоминаем в список все айди вк, которые уже есть в бд
                    a = [x[0] for x in result]
                    if event.user_id not in a:
                        """ в случае если такого айди еще нет, то добавляем в бд его имя и возраст, все это
                         происходит по нажатию моя анкета"""
                        cur.execute("""INSERT INTO saveinfo (id_vk, name, age) VALUES (?, ?, ?)""",
                                    (event.user_id, dname[event.user_id], dage[event.user_id]))
                        con.commit()
                if event.user_id in dname:
                    send_message(vk_session, 'user_id', event.user_id, message=f'Ваше имя: {dname[event.user_id]}',
                                 keyboard=keyboard)
                else:
                    send_message(vk_session, 'user_id', event.user_id, message=f'Ваше имя: Неизвестно',
                                 keyboard=keyboard)
                if event.user_id in dage:
                    send_message(vk_session, 'user_id', event.user_id, message=f'Ваш возраст: {dage[event.user_id]}',
                                 keyboard=keyboard)
                else:
                    send_message(vk_session, 'user_id', event.user_id, message=f'Ваш возраст: Неизвестно',
                                 keyboard=keyboard)
                if event.user_id in dlike:
                    send_message(vk_session, 'user_id', event.user_id, message=f'Вы любите: {dlike[event.user_id]}',
                                 keyboard=keyboard)
                else:
                    send_message(vk_session, 'user_id', event.user_id, message=f'Вы любите: вы мне не расскзали...',
                                 keyboard=keyboard)
                if event.user_id in df and event.user_id in dm:
                    send_message(vk_session, 'user_id', event.user_id, message='Вам нравится музыка и фильмы',
                                 keyboard=keyboard)
                elif event.user_id in df:
                    send_message(vk_session, 'user_id', event.user_id, message='Вам нравятся фильмы',
                                 keyboard=keyboard)
                elif event.user_id in dm:
                    send_message(vk_session, 'user_id', event.user_id, message='Вам нравится музыка',
                                 keyboard=keyboard)
                else:
                    send_message(vk_session, 'user_id', event.user_id, message='Да откуда я знаю, что вам нравится???',
                                 keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message='', attachment=attachment, keyboard=keyboard)
            elif "люблю" in response:
                like = response[6:]
                dlike[event.user_id] = like
                send_message(vk_session, 'user_id', event.user_id, message='Однако интересно')
                send_message(vk_session, 'user_id', event.user_id,
                             message='Выберите, что Вы любите из того что я Вам предложил, и я вам скину что-то '
                                     'интересное',
                             keyboard=keyboard)

            elif 'фильмы' in response or response == 'ещё':
                ss = randint(0, 25)
                send_message(vk_session, 'user_id', event.user_id, message='Ловите', attachment=spfilms[ss],
                             keyboard=keyboard)
            elif 'музыка' in response or 'хочу ещё' in response:
                ch = randint(0, 60)
                send_message(vk_session, 'user_id', event.user_id, message='Круто!', attachment=spmuz[ch],
                             keyboard=keyboard)
            elif 'книги' in response:
                send_message(vk_session, 'user_id', event.user_id, message='', attachment='video-194519120_456239017',
                             keyboard=keyboard)
            elif 'мне понравится' in response:
                send_message(vk_session, 'user_id', event.user_id, message='Давай посмотрим...', keyboard=keyboard)
            elif 'рэй брэдбери «крик из-под земли»' == response:
                send_message(vk_session, 'user_id', event.user_id, message='', attachment='wall-194519120_334',
                             keyboard=keyboard)
            elif 'погода' == response:
                send_message(vk_session, 'user_id', event.user_id,
                             message='Введите название вашего города в формате: "Город: Липецк"', keyboard=keyboard)
            elif 'город' in response:
                city = response[7:]
                spisok = weather.wet(city)
                cl = tt()  # получение текущего времени
                send_message(vk_session, 'user_id', event.user_id,
                             message=f'Сегодня {cl[:10]}, Московское время: {cl[11:]}. Прогноз погоды обновляется'
                                     f' примерно раз в 10 минут')
                # выводим пользователю информацию по погоде в его городе
                for x in spisok:
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=x, keyboard=keyboard)
                send_message(vk_session, 'user_id', event.user_id, message='', attachment='photo-194519120_457239550',
                             keyboard=keyboard)
            elif 'спасибо' in response:
                send_message(vk_session, 'user_id', event.user_id, message='Да пожалуйста')
            elif response == 'Расскажи ещё что-то':
                send_message(vk_session, 'user_id', event.user_id,
                             message='Я думаю, что основные способности бота ты уж узнал, так что давай перейдем к '
                                     'более интересным темам для разговора. А их нет, уупс')
            elif response == 'текущие баллы':
                if flagi and flagm:
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=f'У Вас по математике {markm[event.user_id]} {d[markm[event.user_id]]}')
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=f'У Вас по информатике {marki[event.user_id]} {d[marki[event.user_id]]}')
                elif flagi:
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=f'У Вас по информатике {marki[event.user_id]} {d[marki[event.user_id]]}')
                elif flagm:
                    send_message(vk_session, 'user_id', event.user_id,
                                 message=f'У Вас по математике {markm[event.user_id]} {d[markm[event.user_id]]}')
                else:
                    send_message(vk_session, 'user_id', event.user_id, message='Вы еще не прошли ни одного теста')
            else:
                send_message(vk_session, 'user_id', event.user_id, message='Я вас не понял...')

        # print('-' * 30) до этого применялось дл разделения между сообщениями
