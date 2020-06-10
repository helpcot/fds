import discord
import os
import random
import asyncio
from discord.ext import commands


prefix = "/"
bot = commands.Bot(command_prefix=prefix)




@bot.command() ## Стандартное объявление комманды
async def load(ctx, extensions): ## объявление функции
    bot.load_extension(f'cogs.{extensions}')## загрузка доплонений
    await ctx.send("loaded")


@bot.command()
async def unload(ctx, extensions):
    bot.unload_extension(f'cogs.{extensions}')
    await ctx.send("unloaded")


@bot.command()
async def reload(ctx, extensions):
    bot.unload_extension(f'cogs.{extensions}')# отгружаем ког
    bot.load_extension(f'cogs.{extensions}')# загружаем
    await ctx.send('reloaded')



for filename in os.listdir('./cogs'): # Цикл перебирающий файлы в cogs
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

token = os.environ.get('BOT_TOKEN') # Получаем токен с heroku который ты указывал в настройках
bot.run(str(token)) # запускаем бота