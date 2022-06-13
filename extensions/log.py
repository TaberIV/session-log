import lightbulb

plugin = lightbulb.Plugin('Example')


@plugin.command
@lightbulb.command('log', 'Session log commands')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def log_group(ctx):
    pass


@log_group.child
@lightbulb.command('create', 'Create a session log')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def create(ctx):
    await ctx.respond("This command is not supported.")


@log_group.child
@lightbulb.command('get', 'Find a session log')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def get(ctx):
    await ctx.respond("This command is not supported.")


def load(bot):
    bot.add_plugin(plugin)
