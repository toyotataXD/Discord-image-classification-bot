import discord
from discord.ext import commands
from bot_logic import predict_image
from bot_token import TOKEN

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} Olarak giriş yapıldı!')
    

@bot.command()
async def detect_info(ctx):
    if ctx.message.attachments:
        await ctx.send("Algılama başladı")

        

        info_list = []

        for attachment in ctx.message.attachments:
            filename = attachment.filename
            await attachment.save(f"M7L1/images/{filename}")
            file_path = f"M7L1/images/{filename}"
            name, score = predict_image(file_path, "keras_model.h5", "labels.txt")  

            info_list.append({
                "id": attachment.id,
                "isim": attachment.filename,
                "boyut": attachment.size,
                "tip": attachment.content_type,
                "url": attachment.url
            })

        await ctx.send(f"Bulunan elemanlar:\n```{info_list}```")

    else:
        await ctx.send("Lütfen komutla birlikte fotoğraf ekleyin")


@bot.command()
async def detect(ctx):
    if ctx.message.attachments:  
        await ctx.send("Algılama başladı")
        for attachment in ctx.message.attachments:
            filename = attachment.filename
            filepath = f"M7L1/images/{filename}"
            await attachment.save(filepath)  
            name, score = predict_image(filepath, "M7L1/keras_model.h5", "M7L1/labels.txt")
            await ctx.send(f"{name} {score}")
    else:
        await ctx.send("Lütfen komutla birlikte fotoğraf ekleyin")

bot.run(TOKEN)