import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import datetime
import sys


def until_sbor():
    sbor_date = datetime.date(2022, 8, 22)
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
            vk.messages.send(message='Бот включен.',
                             random_id=random.randint(0, 2 ** 64),
                             peer_id='2000000002')
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    print(event.obj)
                    text = ''.join(event.obj['text'].lower().split())
                    if 'бот' in text and 'выключить.' in text and '1987' in text and event.obj['from_id'] == 215831994:
                        vk.messages.send(message='Бот выключен.',
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                        sys.exit()
                    if ('как' in text or 'какой' in text) and ('эл' in text or 'назва' in text or 'называ' in text):
                        vk.messages.send(message=help_name,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if 'через' in text and 'боль' in text:
                        vk.messages.send(message=f"Зачем через боль? Тренируйся с умом:\n{flexibility}",
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if ('спасибо' in text or 'от души' in text or 'благодар' in text) and 'бот' in text:
                        vk.messages.send(message="обращайся.",
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if ('где' in text or 'когда' in text or 'инфа' in text) and 'сбор' in text:
                        vk.messages.send(message=sbor_message,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if 'бот смени инфу' in text:
                        if len(event.obj['fwd_messages']) == 0:
                            vk.messages.send(message="Не на хуй менять инфу про сбор",
                                             random_id=random.randint(0, 2 ** 64),
                                             peer_id=event.obj['peer_id'])
                        else:
                            sbor_message = event.obj['fwd_messages'][0]['text']
                            vk.messages.send(message=f"Инфа про сбор сменена на \n{sbor_message}",
                                             random_id=random.randint(0, 2 ** 64),
                                             peer_id=event.obj['peer_id'])
                    if 'бот смени приветствие' in text:
                        if len(event.obj['fwd_messages']) == 0:
                            vk.messages.send(message="Не на хуй менять приветствие",
                                             random_id=random.randint(0, 2 ** 64),
                                             peer_id=event.obj['peer_id'])
                        else:
                            welcome_message = event.obj['fwd_messages'][0]['text']
                            vk.messages.send(message=f"Приветствие сменено на \n{welcome_message}",
                                             random_id=random.randint(0, 2 ** 64),
                                             peer_id=event.obj['peer_id'])
                    if 'action' in event.obj:
                        act = event.obj['action']
                        if act['type'] == 'chat_invite_user' or act['type'] == 'chat_invite_user_by_link':
                            vk.messages.send(message=welcome_message,
                                             random_id=random.randint(0, 2 ** 64),
                                             peer_id=event.obj['peer_id'])
                    if ('как' in text or 'помоги' in text or 'помощ' in text or 'инф' in text) \
                            and ('растяжк' in text or 'растяг' in text or 'тянут' in text):
                        vk.messages.send(message=flexibility,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if ('как' in text or 'помоги' in text or 'помощ' in text or 'инф' in text) \
                            and ('назвать' in text or 'называ' in text
                                 or 'термин' in text or 'мод' in text or 'приставка' in text or 'узел' in text):
                        vk.messages.send(message=modifications,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if ('как' in text or 'помоги' in text or 'помощ' in text or 'инф' in text) \
                            and ('размят' in text or 'разомн' in text or 'размин' in text):
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
                    if ('учит' in text or 'как' in text or 'че' in text) and ('начат' in text or 'нов' in text):
                        vk.messages.send(message=newbie_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if ('что' in text or 'че' in text or 'шо' in text) and ('имбар' in text) or ('основ' in text):
                        vk.messages.send(message=basic_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if ('как' in text or 'шо' in text or 'че' in text or 'што' in text or 'что' in text) and ('катег' in text) and ('эл' in text):
                        vk.messages.send(message=category_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if ('как' in text or 'шо' in text or 'че' in text or 'што' in text or 'что' in text) and \
                            ('куш' in text or 'есть' in text or 'питат' in text or 'жрат' in text or 'хава' in text):
                        vk.messages.send(message=eat_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if ('как' in text or 'шо' in text or 'че' in text or 'што' in text or 'что' in text) and \
                            ('сил' in text or "кач" in text):
                        vk.messages.send(message=strength_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if ('как' in text or 'шо' in text or 'че' in text or 'што' in text or 'что' in text) and \
                            ('нивел' in text or 'ниву' in text or 'nivelad' in text):
                        vk.messages.send(message=nivelada_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if ('как' in text or 'шо' in text or 'че' in text or 'што' in text or 'что' in text) and \
                            ('эску' in text or 'escuad' in text):
                        vk.messages.send(message=escuadra_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])
                    if ('как' in text or 'шо' in text or 'че' in text or 'што' in text or 'что' in text) and \
                            ('anclad' in text or 'флаг' in text or 'анклад' in text):
                        vk.messages.send(message=anclado_help,
                                         random_id=random.randint(0, 2 ** 64),
                                         peer_id=event.obj['peer_id'])

        except Exception:
            pass




if __name__ == '__main__':
    sbor_message = "Сбор 2021" \
                   "\n🗺 Место:г. Москва, метро Орехово, площадка в парке «Борисовские пруды»." \
                   "\n🕑 Время:22 августа 14:00" \
                   "\nОстальная инфа по сбору: vk.cc/gimbarrpublic" \
                   "\nБеседа по сбору: vk.cc/c4kkc5"
    welcome_message = "Пивет! Это беседа по Джимбарру 🌿" \
                      "\n••••••••••••••••••••••••••••••••••••••••••••" \
                      "\n🔥Ежегодный сбор 22 августа, Москва!!!🔥" \
                      "\n••••••••••••••••••••••••••••••••••••••••••••" \
                      "\nПолезные ссылки:" \
                      "\n• Джел (группа с отснятыми элементами): vk.com/gimbarr_elementos" \
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
    main()