from discord import Embed, Color


def result(title, description, format_result=False):
    if format_result:
        return Embed(title=title, description=get_formatted_result(description), color=Color.gold())
    else:
        return Embed(title=title, description=description, color=Color.blue())


def source(name, data):
    return Embed(title=name, description=data, color=Color.dark_theme())


def menu(title, description, items):
    embed = Embed(title=title, description=description, color=Color.blurple())
    for item in items.items():
        embed.add_field(name=item[0], value=f"```{item[1]}```", inline=False)
    return embed


def get_formatted_result(result):
    return f"```{result}```"
