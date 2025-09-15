# MIT License

# Copyright (c) 2025 MoleculeDEV

# Разрешается бесплатное использование, копирование, изменение, слияние, публикация, распространение, сублицензирование и/или продажа копий данного ПО при условии, что в вышеуказанных копиях или других материалах, предоставленных вместе с ПО, будет содержаться следующая заметка о праве собственности:

# Этот программный продукт предоставляется "как есть", без каких-либо гарантий, прямо или косвенно, включая, но не ограничиваясь, гарантиями товарной пригодности или пригодности для конкретной цели. В любом случае авторы или правообладатели не несут ответственности за любые претензии, убытки или другие обязательства, будь то в действии контракта, деликте или другом правовом основании, возникающие из, в связи с или в результате использования данного ПО.

from telethon import events
from TgNet import handle_say, handle_stop
from TgNetUWP import handle_name, handle_delname, handle_setname, handle_stop as handle_uwp_stop

@events.register(events.NewMessage(pattern=r'\.say (.+)'))
async def handle_command(event):
    text = event.pattern_match.group(1).strip()
    if text:
        await handle_say(event, text)

@events.register(events.NewMessage(pattern=r'\.stop'))
async def stop_sending(event):
    await handle_stop(event)
    await handle_uwp_stop(event)

@events.register(events.NewMessage(pattern=r'\.name (.+)'))
async def name_command(event):
    text = event.pattern_match.group(1).strip()
    await handle_name(event, text)

@events.register(events.NewMessage(pattern=r'\.delname'))
async def delname_command(event):
    await handle_delname(event)

@events.register(events.NewMessage(pattern=r'\.setname (.+)'))
async def setname_command(event):
    name = event.pattern_match.group(1).strip()
    await handle_setname(event, name)