# MIT License

# Copyright (c) 2025 MoleculeDEV

# Разрешается бесплатное использование, копирование, изменение, слияние, публикация, распространение, сублицензирование и/или продажа копий данного ПО при условии, что в вышеуказанных копиях или других материалах, предоставленных вместе с ПО, будет содержаться следующая заметка о праве собственности:

# Этот программный продукт предоставляется "как есть", без каких-либо гарантий, прямо или косвенно, включая, но не ограничиваясь, гарантиями товарной пригодности или пригодности для конкретной цели. В любом случае авторы или правообладатели не несут ответственности за любые претензии, убытки или другие обязательства, будь то в действии контракта, деликте или другом правовом основании, возникающие из, в связи с или в результате использования данного ПО.

import asyncio
import random
from os.path import exists

titles_file = 'titles.txt'
is_sending = False

async def delete_message(event):
    if hasattr(event, 'delete'):
        await event.delete()

async def handle_name(event, text):
    global is_sending
    name = ''
    
    if exists(titles_file):
        with open(titles_file, 'r', encoding='utf-8') as file:
            name = file.read().strip()
    
    await delete_message(event)

    if name and not text.startswith(name):
        text = f"{name} {text}"

    words = text.split()
    
    if len(words) <= 12:
        await event.reply(text)
    else:
        is_sending = True
        while len(words) > 0 and is_sending:
            size = random.randint(8, 12)
            chunk = words[:size]
            words = words[size:]
            await event.reply(" ".join(chunk))
            await asyncio.sleep(1)

async def handle_stop(event):
    global is_sending
    await delete_message(event)
    if is_sending:
        is_sending = False

async def handle_delname(event):
    if exists(titles_file):
        with open(titles_file, 'w', encoding='utf-8') as file:
            file.truncate(0)
    await delete_message(event)

async def handle_setname(event, name):
    with open(titles_file, 'w', encoding='utf-8') as file:
        file.write(name.strip())
    await delete_message(event)