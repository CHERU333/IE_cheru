import discord
from discord.ext import commands
from mylib.constant import EXTENTIONS, TOKEN

# MyBotクラスを定義
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="/",  # コマンドのプレフィックスを指定
            intents=discord.Intents.all(),  # すべてのインテントを使用
        )

    # 拡張機能を一括で読み込むためのメソッド
    async def setup_hook(self):
        for extension in EXTENTIONS:
            await self.load_extension(extension)

# メインの実行部分
if __name__ == "__main__":
    bot = MyBot()  # MyBotクラスのインスタンスを作成
    bot.run(token=TOKEN)  # ボットを実行するためのトークンを指定して実行

