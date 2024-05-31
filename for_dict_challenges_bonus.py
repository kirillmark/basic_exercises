"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

Так же есть функция generate_chat_history, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.

messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def get_count_elem(users_lst, elem):
    result_dict = {}
    for message in users_lst:
        result_dict[message[elem]] = result_dict.setdefault(message[elem], 0) + 1
    return result_dict


def get_id(lst, value):
    for message in lst:
        if message['id'] == value:
            return message['sent_by']


def get_id_max_uniq_mess(lst):
    result_dict = {}
    for message in lst:
        key = message['sent_by']
        result_dict.setdefault(key, set())
        result_dict[key] = result_dict[key].union(message['seen_by'])
    return result_dict


def get_most_popular(d):
    len_d = {k: len(v) for k, v in d.items()}
    max_val = max(len_d, key=len_d.get)
    return [k for k, v in len_d.items() if v == len_d[max_val]]


# Тут запутался малость
# def branches(lst):
#     headers = {x['id']: [] for x in lst if x['reply_for'] is None}
#     print(headers)
#
#     for m in lst:
#         reply_id = m['reply_for']
#         if reply_id in headers:
#             headers[reply_id].append(m['id'])
#     print(headers)
#
#     for m in lst:
#         reply_id = m['reply_for']
#         if reply_id is not None and headers.get(reply_id) and reply_id in headers[reply_id]:
#             headers[reply_id].append(m['id'])
#
#     return headers


def max_time_zone(lst):
    # утром (с 5 до 12 часов), днём (12-18 часов) или вечером (с 18 часов до 23).
    morning = day = evening = 0
    for m in lst:
        h = m['sent_at'].hour
        if 5 <= h < 12:
            morning += 1
        elif 12 <= h < 18:
            day += 1
        elif 18 <= h < 23:
            evening += 1
    max_res = max(morning, day, evening)
    if morning == max_res:
        return f'в чате больше всего сообщений: утром'
    elif day == max_res:
        return f'в чате больше всего сообщений: днем'
    else:
        return f'в чате больше всего сообщений: вечером'


if __name__ == "__main__":
    chat = generate_chat_history()
    print(1)
    send_max_mess = get_count_elem(chat, 'sent_by')
    print(max(send_max_mess, key=send_max_mess.get))
    print(2)
    reply_for_dict = get_count_elem(chat, 'reply_for')
    if max(reply_for_dict, key=reply_for_dict.get):
        print(max(reply_for_dict, key=reply_for_dict.get))
    else:
        max_message_id = sorted(reply_for_dict, key=reply_for_dict.get)[-2]
        print(get_id(chat, max_message_id))
    print(3)
    print(*get_most_popular(get_id_max_uniq_mess(chat)))
    print(4)
    print(max_time_zone(chat))

