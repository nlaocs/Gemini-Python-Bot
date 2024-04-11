import os
import google.generativeai as genai
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-pro")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.hybrid_command(name="chat", description="Gemini-AI")
async def chat(ctx, *, message: str):
    botmessage = await ctx.send("考え中...")
    response = model.generate_content(message)
    assistant_response = response.text
    await botmessage.edit(content=f"{assistant_response}")

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} にログインしました")

bot.run(os.environ["TOKEN"])
