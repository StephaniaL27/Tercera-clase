import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def saludar(ctx):
    await ctx.send('¡Hola!Soy un bot de prueba!')

@bot.command()
async def sumar(ctx, a: int, b: int):
    await ctx.send(f'La suma de {a} y {b} es {a + b}')

@bot.command()
async def lanzar_dado(ctx):
    resultado = random.randint(1, 6)
    if resultado == 1:
        await ctx.send('¡Has sacado un 1! ¡Intenta de nuevo!')
    elif resultado == 6:
        await ctx.send('¡Has sacado un 6! ¡Felicidades!')
    else:
        await ctx.send(f'Has sacado un {resultado}. ¡Sigue jugando!')

@bot.command()
async def generar_contraseña(ctx):
    elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(8):
        password += random.choice(elements)
    await ctx.send(f"Tu contraseña es: {password}")

bot.run('token')