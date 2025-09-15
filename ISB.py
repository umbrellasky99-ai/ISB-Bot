# MIT License

# Copyright (c) 2025 MoleculeDEV

# Разрешается бесплатное использование, копирование, изменение, слияние, публикация, распространение, сублицензирование и/или продажа копий данного ПО при условии, что в вышеуказанных копиях или других материалах, предоставленных вместе с ПО, будет содержаться следующая заметка о праве собственности:

# Этот программный продукт предоставляется "как есть", без каких-либо гарантий, прямо или косвенно, включая, но не ограничиваясь, гарантиями товарной пригодности или пригодности для конкретной цели. В любом случае авторы или правообладатели не несут ответственности за любые претензии, убытки или другие обязательства, будь то в действии контракта, деликте или другом правовом основании, возникающие из, в связи с или в результате использования данного ПО.

from telethon import TelegramClient
from config import API_ID, API_HASH
from ToggleSwitch import handle_command, stop_sending, name_command, delname_command, setname_command

session_name = 'Accounts/session_session'
client = TelegramClient(session_name, API_ID, API_HASH)

async def main():
    await client.start() 
    client.add_event_handler(handle_command)
    client.add_event_handler(stop_sending)
    client.add_event_handler(name_command)
    client.add_event_handler(delname_command)
    client.add_event_handler(setname_command)
    await client.run_until_disconnected()

client.loop.run_until_complete(main())