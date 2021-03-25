from discord.ext import commands

import utils, src, constants


class Source(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Main group
    @commands.group(name="src", aliases=["source", "sourcecode"])
    async def _src(self, ctx):
        pass

    # Sub groups
    @_src.group(name="bn2", aliases=["baseneg2", "basenegative2"])
    async def bn2(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(embed=utils.embed.source(constants.bn2.title_bn2,
                                                    src.bn2.bn2()))

    @_src.group(name="excel", aliases=["Excel"])
    async def excel(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(embed=utils.embed.source(constants.excel.title_excel,
                                                    src.excel.excel()))

    # commands
    @bn2.command(name="int")
    async def int(self, ctx):
        await ctx.send(embed=utils.embed.source(constants.bn2.title_int_to_nb,
                                                src.bn2.negabinary_to_int()))

    @bn2.command(name="nb")
    async def nb(self, ctx):
        await ctx.send(embed=utils.embed.source(constants.bn2.title_nb_to_int,
                                                src.bn2.int_to_negabinary()))

    @_src.command(name="rpgdiceroller", aliases=['rolldice'])
    async def rpgdiceroller(self, ctx):
        await ctx.send(embed=utils.embed.source(constants.rpgdiceroller.title_roll_dice,
                                                src.rpgdiceroller.roll_dice()))

    @_src.command(name="extractdomain", aliases=["domainname", "domain_name"])
    async def extract_domain(self, ctx):
        await ctx.send(embed=utils.embed.source(constants.extractdomain.title_domain_name,
                                                src.extractdomain.domain_name()))

    @_src.command(name="notverysecure", aliases=["alphanumeric"])
    async def not_very_secure(self, ctx):
        await ctx.send(embed=utils.embed.source(constants.alphanumeric.title_alphanumeric,
                                                src.alphanumeric.alphanumeric()))

    @excel.command(name="countif", aliases=["count_if"])
    async def countif(self, ctx):
        await ctx.send(embed=utils.embed.source(constants.excel.title_countif,
                                                src.excel.countif()))

    @excel.command(name="sumif", aliases=["sum_if"])
    async def sumif(self, ctx):
        await ctx.send(embed=utils.embed.source(constants.excel.title_sumif,
                                                src.excel.sumif()))

    @excel.command(name="averageif", aliases=["average_if"])
    async def averageif(self, ctx):
        await ctx.send(embed=utils.embed.source(constants.excel.title_averageif,
                                                src.excel.averageif()))


def setup(bot):
    bot.add_cog(Source(bot))
