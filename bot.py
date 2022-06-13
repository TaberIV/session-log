import lightbulb
import os

bot = lightbulb.BotApp(
    token=os.environ['DISCORD_TOKEN'],
    default_enabled_guilds=(659809913194807306)
)


bot.load_extensions_from('./extensions')
bot.run()
