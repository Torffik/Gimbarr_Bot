import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import datetime
import sys

# GIMBARR BOT v1.1 by Eroropka and Torf0lane

# Слава Тебе, Боже наш, слава Тебе. Царю Небесный, Утешителю, Душе истины, Иже везде сый и вся исполняяй, Сокровище
# благих и жизни Подателю, прииди и вселися в ны, и очисти ны от всякия скверны, и спаси, Блаже, души наша. Святый Боже,
# Святый Крепкий, Святый Бессмертный, помилуй нас.


def is_in_text(words, checked_text):
    global trigger_lists
    for trigger in trigger_lists[words]:
        if trigger in checked_text:
            return True
    return False


def until_sbor():
    sbor_date = datetime.date(2023, 8, 21)
    today_date = datetime.date.today()
    until = str((sbor_date - today_date).days)
    if until[-1] == '1':
        prefix = ' день'
    elif 2 <= int(until[-1]) <= 4:
        prefix = ' дня'
    else:
        prefix = ' дней'
    return until + prefix


def main():
    global sbor_message, welcome_message
    while True:
        try:
            vk_session = vk_api.VkApi(
                token='9c8e42b7711b8cf451444c94f917ea645bdc5c516c79ba2ee7cb7fef7151375e6187efacdd1ce40b4243f')
            longpoll = VkBotLongPoll(vk_session, 204026405)
            vk = vk_session.get_api()
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    print(event.obj)
                    text = ''.join(event.obj['text'].lower().split())
                    if 'бот' in text and 'выключить.' in text and '1987' in text:
                        if event.obj['from_id'] == 215831994 or\
                           event.obj['from_id'] == 175494314:
                            vk.messages.send(message='Бот выключен.',
                                             random_id=random.randint(0, 2 ** 64),
                                             peer_id=event.obj['peer_id'])
                            sys.exit()
                        else:
                            vk.messages.send(message='У тебя здесь нет власти.',
                                             random_id=random.randint(0, 2 ** 64),
                                             peer_id=event.obj['peer_id'])

                    if is_in_text('what', text) and (is_in_text('trick', text) or is_in_text('name', text)):
                        vk.messages.send(message=help_name,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])

                    if 'через' in text and 'боль' in text:
                        vk.messages.send(message=f"Зачем через боль? Тренируйся с умом:\n{flexibility}",
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])

                    if is_in_text('thanks', text) and ('бот' in text):
                        vk.messages.send(message="обращайся.",
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])

                    if (is_in_text('where', text)) and ('сбор' in text):
                        vk.messages.send(message=sbor_message,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if 'action' in event.obj:
                        act = event.obj['action']
                        if act['type'] == 'chat_invite_user' or act['type'] == 'chat_invite_user_by_link':
                            vk.messages.send(message=welcome_message,
                                             random_id=random.randint(0, 2 ** 64),
                                             peer_id=event.obj['peer_id'])
                    if is_in_text('help', text) and is_in_text('flexibility', text):
                        vk.messages.send(message=flexibility,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if is_in_text('help', text or is_in_text('what', text)) \
                            and is_in_text('name', text) or is_in_text('terms', text):
                        vk.messages.send(message=modifications,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if (is_in_text('help', text) or is_in_text('what', text)) and is_in_text('warmup', text):
                        vk.messages.send(message=warmup,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if ('оцен' in text and 'техник' in text) \
                            or ('разниц' in text or 'различ' in text or 'отлич' in text or 'инф' in text) \
                            and ('техник' in text or 'исполн' in text):
                        vk.messages.send(message=execution_technique,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if 'ддс' in text or (('дни' in text or 'дней' in text) and 'сбор' in text):
                        vk.messages.send(message=f"До сбора осталось {until_sbor()}",
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if is_in_text('what', text) and (('начат' in text or 'нов' in text) or ('учит' in text)) :
                        vk.messages.send(message=newbie_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if (is_in_text('what', text)) and (is_in_text('gimbarr', text)) or ('основ' in text):
                        vk.messages.send(message=basic_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if (is_in_text('what', text) or is_in_text('help', text)) and (is_in_text('category', text)):
                        vk.messages.send(message=category_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if (is_in_text('what', text) or is_in_text('help', text)) and is_in_text('eat', text):
                        vk.messages.send(message=eat_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if (is_in_text('what', text) or is_in_text('help', text)) and is_in_text('strength', text):
                        vk.messages.send(message=strength_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if (is_in_text('what', text) or is_in_text('help', text)) and \
                            (is_in_text('nivelada', text) or is_in_text('y', text)):
                        vk.messages.send(message=nivelada_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if (is_in_text('what', text) or is_in_text('help', text)) and (is_in_text('escuadra', text)):
                        vk.messages.send(message=escuadra_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if (is_in_text('what', text) or is_in_text('help', text)) and \
                            ('anclad' in text or 'флаг' in text or 'анклад' in text):
                        vk.messages.send(message=anclado_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if is_in_text('hello', text) and ('бот' in text):
                        vk.messages.send(message='ПОШЁЛ НА ХУЙ ПИДОРАС ТЫ ЕБАНЫЙ ЕБАЛ ТЕБЯ И ВСЮ ТВОЮ СЕМЬЮ'
                                                 'И СЕМЬЮ ТВОЕЙ СЕМЬИ И ТВОИХ ДРУЗЕЙ И ИХ СЕМЬИ '
                                                 'И ТВОИХ ПИТОМЦЕВ И ИХ ДРУЗЕЙ И ТВОИХ ЗНАКОМЫХ '
                                                 'И ИХ СЕМЬИ И ИХ ДРУЗЕЙ ГАНДОН ШТОПАННЫЙ',
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if ('бот' in text) and ('хуеглот' in text):
                        vk.messages.send(message=': (',
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if (is_in_text('what', text) or is_in_text('help', text)) and \
                            ('morter' in text or 'мортер' in text or 'кокон' in text):
                        vk.messages.send(message=mortero_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if (is_in_text('what', text) or is_in_text('help', text)) and \
                            ('gan' in text or 'ган' in text or 'уно' in text or 'uno' in text or 'фрауд' in text or 'fraud' in text):
                        vk.messages.send(message=ungan_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if (is_in_text('what', text) or is_in_text('help', text)) and \
                            ('singl' in text or 'сингл' in text or 'савок' in text or 'sawok' in text or 'бамбин' in text or 'bambin' in text):
                        vk.messages.send(message=single_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if (is_in_text('what', text) or is_in_text('help', text)) and \
                            ('cript' in text or 'крипт' in text or 'aqua' in text or 'аква' in text or 'палечн' in text):
                        vk.messages.send(message=cripta_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if (is_in_text('what', text) or is_in_text('help', text)) and \
                            ('kraken' in text or 'кракен' in text or 'doman' in text or 'доман' in text):
                        vk.messages.send(message=kraken_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])

        except Exception:
            pass


if __name__ == '__main__':
    # trigger_lists - словарь с часто попадающимися вопросами

    trigger_lists = {'what': ['че', 'что', 'што', 'шо', 'чё', 'как', 'инф'],
                     'help': ['помог', 'помощ', 'хелп', 'совет', 'подска', 'список', 'списка', 'инф', 'разви'],
                     'where': ['когда', 'числ', 'где', 'инф'],
                     'anclado': ['anclad', 'анклад', 'флаг', 'флаж'],
                     'nivelada': ['nivel', 'нивел', 'нива', 'нивы', 'ниву', 'ниве'],
                     'escuadra': ['escua', 'эск', 'еск'],
                     'strength': ['сил', 'кач'],
                     'eat': ['куш', 'пита', 'жрат', 'хава'],
                     'gimbarr': ['gimbar', 'джимбар', 'гимбар', 'жимбар'],
                     'hello': ['привет', 'здаров', 'пивет', 'салам', 'здоров', 'хай'],
                     'trick': ['эл', 'трюк', 'трик'],
                     'name': ['назыв', 'назв', 'имя'],
                     'warmup': ['размин', 'разогр', 'размя', 'разомн'],
                     'category': ['катег', 'сери', 'групп', 'подсери', 'подгрупп'],
                     'terms': ['термин', 'мод', 'пристав', 'узел', 'узл'],
                     'thanks': ['спасибо', 'от души', 'благодар', 'спс', 'дякую'],
                     'flexibility': ['растяжк', 'тяну', 'тяне', 'тяни', 'жидк', 'гибк', 'растяг'],
                     'difference': ['различ', 'разниц', 'отлич'],
                     'y': ['игрег', 'игрик', 'игрек']}

    sbor_message = "Сбор 2021" \
                   "\n🗺 Место:г. Москва, метро Орехово, площадка в парке «Борисовские пруды»." \
                   "\n🕑 Время:21 августа 14:00" \
                   "\nОстальная инфа по сбору: vk.cc/gimbarrpublic" \
                   "\nБеседа по сбору: vk.cc/c4kkc5"
    welcome_message = "Пивет! Это беседа по Джимбарру 🌿" \
                      "\n••••••••••••••••••••••••••••••••••••••••••••" \
                      "\n🔥Ежегодный сбор 22 августа, Москва!!!🔥" \
                      "\n••••••••••••••••••••••••••••••••••••••••••••" \
                      "\nПолезные ссылки:" \
                      "\n• Джимбарр Элементос (группа с отснятыми элементами): vk.com/gimbarr_elementos" \
                      "\n• Паблик (группа с предложкой): vk.com/gimbarrofficial" \
                      "\n• Канал Justo Gimbarr: vk.cc/c3W9Ia" \
                      "\n• Канал Dima Gukasyan: vk.cc/c3W91v" \
                      "\nПравила: нельзя 228/porn/расчлененка/спам" \
                      "\nПо любым вопросам: vk.com/gimbarr.official"
    flexibility = "Увеличение гибкости в Джимбарре:" \
                  "\n✅ Правила растяжки: vk.cc/c4kknf" \
                  "\n✅ Топ упражнений часть1: vk.cc/c4kks6" \
                  "\n✅ Топ упражнений часть2: vk.cc/c4kksX" \
                  "\n✅ Биомеханика: vk.cc/ceffgy"
    modifications = "Все термины в Джимбарре:" \
                    "\n✅ Определения: vk.cc/c4kkJ1" \
                    "\n✅ Все перехваты: vk.cc/c4kk3i" \
                    "\n✅ Обычные узлы: vk.cc/c4kkLN" \
                    "\n✅ Узлы в лотосе: vk.cc/c4kkN9" \
                    "\n✅ Захваты Barra a Barra: vk.cc/c4kkOe" \
                    "\n✅ Упавшие флаги: vk.cc/c4kkPC" \
                    "\n✅ Самые простые хваты и положения: vk.cc/c4kkR3" \
                    "\n✅ Самые сложные хваты и положения: vk.cc/c4kkSi" \
                    "\n✅ Легкие флаги: https://vk.cc/c4kRbU" \
                    "\n✅ Сложные флаги: https://vk.cc/c4kRwo"
    warmup = "\n✅ Инфа по разминке: vk.cc/c4kl1z"
    execution_technique = "Техника и исполнение, почему это разные вещи:" \
                          "\n✅ Про исполнение элементов: vk.cc/c4kl37" \
                          "\n✅ Про технику элементов: vk.cc/c4kl4w"
    help_name = "Не знаешь название элемента? Попробуй:" \
                "\n✅ Поискать тут и в комментариях: vk.cc/c4ldmV" \
                "\n✅ Составить сам с помощью видео по терминам:" \
                "\n✅ В конце концов обратиться сюда: vk.cc/c4ldoH"
    newbie_help = "Видео по Джимбарру для новичков:" \
                  "\n✅ Топ 50 элементов для новичка: https://vk.cc/c6uCMl" \
                  "\n✅ С чего начать Джимбарр(Дмитрий Гукасян): https://vk.cc/c6uCNd" \
                  "\n✅ Как начать Джимбарр: https://vk.cc/c6uCNS"
    basic_help = "Основа Джимбарра:" \
                 "\n✅ Что такое Джимбарр: https://vk.cc/ca6MmK" \
                 "\n✅ Богатства Джимбарра: https://vk.cc/ca6MqD"
    category_help = "Категории элементов Джимбарра:" \
                    "\n✅ Категория фигуры: https://vk.cc/ca6NIt" \
                    "\n✅ Категория хиро: https://vk.cc/ca6NQd" \
                    "\n✅ Категория йойо: https://vk.cc/ca6NLf"
    eat_help = "Советы по питанию:" \
               "\n✅ Желатин, коллаген: https://vk.cc/ca6OCE" \
               "\n✅ Электролиты, минералка, изотоник: https://vk.cc/ca6OIC"
    strength_help = "Увеличение силы в Джимбарре:" \
                    "\n✅ Типы мышечных волокон: vk.cc/ceff9p" \
                    "\n✅ СФП и периодизация тренировок: vk.cc/ceffe7" \
                    "\n✅ Биомеханика: vk.cc/ceffgy"
    nivelada_help = "Изучение нивелады в Джимбарре:" \
                    "\n✅ Начальное изучение: vk.cc/ceffKY" \
                    "\n✅ Улучшение нивелады: vk.cc/ceffIC"\
                    "\n✅ Нивелада Y: vk.cc/ceffX5"
    escuadra_help = "Изучение эскуадры в Джимбарре:" \
                    "\n✅ Начальное изучение: vk.cc/ceffTA" \
                    "\n✅ Виды эскуадры: vk.cc/ceffS8"
    anclado_help = "Изучение флагов в Джимбарре:" \
                   "\n✅ Начальное изучение: vk.cc/cefg2j" \
                   "\n✅ Улучшение флага: vk.cc/cefg4A"\
                   "\n✅ Сложные флаги: vk.cc/c4kRwo"\
                   "\n✅ Простые флаги: vk.cc/c4kRbU"
    mortero_help = "Разбор группы Mortero:" \
                   "\n✅ Видео (Любимый Алекс❤): https://vk.cc/cgxURv"
    ungan_help = "Разбор группы Ungan:" \
                 "\n✅ Видео (Любимый Алекс❤): https://vk.cc/cgxV33"
    single_help = "Разбор группы Single" \
                  "\n✅ Видео (Любимый Алекс❤): https://vk.cc/cgxVdO"
    kraken_help = "Разбор группы Kraken" \
                  "\n✅ Видео (Любимый Алекс❤): https://vk.cc/cgxV87"
    cripta_help = "Как развить хват Cripta/Aqua:" \
                  "\n✅ Обучалка от Юрия Юрия: https://vk.cc/cgxVmi" \
                  "\n✅ Видео (Любимый Алекс❤): https://vk.cc/cgxVfF"
    main()
