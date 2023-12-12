import discord
import random
from discord.ext import commands

# ZundaCogクラスの定義
class ZundaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # pingコマンドの定義
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong!")  # "pong!"と返す

    # pingコマンドの定義
    @commands.command()
    async def greet(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send(f"Hi {ctx.author.mention}!")  # メッセージにメンションを含めて送信
        else:
            await ctx.send(f"Hi {member.mention}!")

    # おみくじコマンドの定義
    @commands.command()
    async def omikuji(self, ctx):
        fortunes = [
            "大吉",
            "吉",
            "中吉",
            "小吉",
            "末吉",
            "凶",
            "大凶",
        ]
        # おみくじの結果をランダムに選ぶ
        result = random.choice(fortunes)
        # 結果を送信
        await ctx.send(f"おみくじの結果: **{result}**")

    # zundaコマンドの定義
    @commands.command()
    async def zunda(self, ctx, *, message):
        response = f"{message} なのだ"
        await ctx.send(response)

# setup関数の定義
async def setup(bot):
    await bot.add_cog(ZundaCog(bot))  # ZundaCogクラスのインスタンスをボットに追加
