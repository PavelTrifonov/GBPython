from loader_bot import dp, bot
from aiogram import types
from random import randint as RD

@dp.message_handler(commands=["start"])
async def message_start(message:types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}, рад тебя видеть!!!")
    await message.answer(f"{message.from_user.first_name}, для запуска игры воспользуйся командой /new_game") 
number=0
step=0
@dp.message_handler(commands=["new_game"])
async def message_start(message:types.Message):
    global number
    global step
    await message.answer(f'{message.from_user.first_name}, давай поиграем в игру "Конфеты", вот правила: на столе лежит N колчесвто конфет,\
    которое можно задать командой "/value (нужное число)" или же оно будет задано рандомно от 100 до 200, первый ход выбирается жеребьевкой, за один ход\
    можно брать от 1 до 28 конфет включительно, выигрывает тот кто ходит последний') 
    number=RD(100,201)
    await bot.send_message(message.from_user.id, f"На столе лежит {number} конфет")
    if RD(0,2)==0:
        step=f"{message.from_user.first_name}"
        await bot.send_message(message.from_user.id, f"Жеребьевка дает право хотить {message.from_user.first_name} первым")
    else:
        step="Я"
        await bot.send_message(message.from_user.id, f"Жеребьевка дает право ходить мне первым")
        bot_play=number%29
        await bot.send_message(message.from_user.id, f"А я возьму {bot_play} конфет)))")
        number-=bot_play
        await bot.send_message(message.from_user.id, f"Конфет стало меньше - {number}")


@dp.message_handler(commands=["value"])
async def message_value(message:types.Message):
    global number
    count=message.text.split()[1]
    number=int(count)
    await message.answer(f"Было задано новое количество конфет: {number}")
    await bot.send_message(message.from_user.id, f"Теперь на столе лежит {number} конфет")

@dp.message_handler()
async def message_game(message:types.Message):
    global number
    if message.text.isdigit():
        play=int(message.text)
        step=f"{message.from_user.first_name}"
        if play in range(1,29):
            number-=play
            if number==0:
                await bot.send_message(message.from_user.id, f"{step}, выиграл эту партию!!!")
            await bot.send_message(message.from_user.id, f"{message.from_user.first_name} взял {play} конфет, на столе осталось {number} конфет")
            if number%29!=0:
                bot_play=number%29
                step="Я"
                # await bot.send_message(message.from_user.id, f"{message.from_user.first_name} взял {play} конфет, на столе осталось {number} конфет")
                await bot.send_message(message.from_user.id, f"А я возьму {bot_play} конфет)))")
                number-=bot_play
                await bot.send_message(message.from_user.id, f"Конфет стало меньше - {number}")
                if number==0:
                    await bot.send_message(message.from_user.id, f"{step}, выиграл эту партию!!!")
            elif number%29==0:
                bot_play=RD(1,28)
                # await bot.send_message(message.from_user.id, f"{message.from_user.first_name} взял {play} конфет, на столе осталось {number} конфет")
                await bot.send_message(message.from_user.id, f"А я возьму {bot_play} конфет)))")
                number-=bot_play
                await bot.send_message(message.from_user.id, f"Конфет стало меньше - {number}")
            # else:
            #     bot_play=RD(1,29)
            #     await bot.send_message(message.from_user.id, f"А я возьму {bot_play} конфет)))")
            #     number-=bot_play
            #     await bot.send_message(message.from_user.id, f"Конфет стало меньше - {number}")
        else:
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.send_message(message.from_user.id, f"{message.from_user.first_name}, так не пойдет, нужно ввести целое число от 1 до 28 включительно)))") 
    else:
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.send_message(message.from_user.id, f"{message.from_user.first_name}, так не пойдет, нужно ввести целое число)))")
    if number==0:
        number=RD(100,201)
        await bot.send_message(message.from_user.id, f"Теперь на столе лежит {number} конфет")
        if RD(0,2)==0:
            step=f"{message.from_user.first_name}"
            await bot.send_message(message.from_user.id, f"Жеребьевка дает право ходить {message.from_user.first_name} первым")
        else:
            step="Я"
            await bot.send_message(message.from_user.id, f"Жеребьевка дает право ходить мне первым")
            bot_play=number%29
            await bot.send_message(message.from_user.id, f"А я возьму {bot_play} конфет)))")
            number-=bot_play
            await bot.send_message(message.from_user.id, f"Конфет стало меньше - {number}")

@dp.message_handler(commands=["weather"])
async def message_weather(message:types.Message):
    await message.answer("Сейчас посмотрим...")

@dp.message_handler(text=["фига себе"])
async def message_cenz(message:types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer("Я тоже удивлен)))")
# @dp.message_handler()
# async def message_weather(message:types.Message):
#     await message.answer(f'Это ты написал: "{message.text}" ???')