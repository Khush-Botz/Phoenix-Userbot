from pyrogram import Client, filters
from pyrogram.types import Message
from Toxic import cmd

@Client.on_message(cmd(['google', 'g']))
async def webshot(client: Client, message: Message):
    user_request = ' '.join(message.command[1:])

    if user_request == '':
        if message.reply_to_message:
            reply_user_request = message.reply_to_message.text
            request = reply_user_request.replace(' ', '+')
            full_request = f'https://lmgtfy.app/?s=g&iie=1&q={request}'
            await message.edit(f'<a href={full_request}>{reply_user_request}</a>')

    else:
        request = user_request.replace(' ', '+')
        full_request = f'https://lmgtfy.app/?s=g&iie=1&q={request}'
        await message.edit(f'<a href={full_request}>{user_request}</a>')


modules_help.update({'google': '''google [request] - To teach the interlocutor to use Google, 
                                  google - Answer a stupid question of your interlocutor to teach him how to use Google''',
                     'google module': 'Google: google'})
