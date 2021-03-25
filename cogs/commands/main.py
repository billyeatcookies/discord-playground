from discord.ext import commands

import lib
import utils
import constants


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # groups
    @commands.group(name="bn2", aliases=["baseneg2", "basenegative2"])
    async def _bn2(self, ctx):
        if ctx.invoked_subcommand is None:
            command_list = {
                "int": constants.bn2.description_int_to_nb,
                "nb": constants.bn2.description_nb_to_int
            }
            await ctx.send(embed=utils.embed.menu(constants.bn2.title_bn2,
                                                  constants.bn2.description_bn2,
                                                  command_list))

    @commands.group(name="excel", aliases=["Excel"])
    async def _excel(self, ctx):
        if ctx.invoked_subcommand is None:
            command_list = {
                "countif": constants.excel.description_countif,
                "sumif": constants.excel.description_sumif,
                "averageif": constants.excel.description_averageif
            }
            await ctx.send(embed=utils.embed.menu(constants.excel.title_excel,
                                                  constants.excel.description_excel,
                                                  command_list))

    # commands
    @_bn2.command(name="int")
    async def _int(self, ctx, i: int):
        await ctx.send(embed=utils.embed.result(constants.bn2.title_int_to_nb,
                                                lib.bn2.int_to_negabinary(i), True))

    @_bn2.command(name="nb")
    async def _nb(self, ctx, nb):
        await ctx.send(embed=utils.embed.result(constants.bn2.title_nb_to_int,
                                                lib.bn2.negabinary_to_int(nb), True))

    @commands.command(name="rpgdiceroller", aliases=["rolldice"])
    async def _roll_dice(self, ctx, desc, verbose: bool=False):
        await ctx.send(embed=utils.embed.result(constants.rpgdiceroller.title_roll_dice,
                                                lib.rpgdiceroller.roll_dice(desc, verbose), True))

    @commands.command(name="extractdomain", aliases=["domainname", "domain_name"])
    async def extract_domain(self, ctx, url):
        await ctx.send(embed=utils.embed.result(constants.extractdomain.title_domain_name,
                                                lib.extractdomain.domain_name(url), True))

    @commands.command(name="notverysecure", aliases=["alphanumeric"])
    async def not_very_secure(self, ctx, password):
        await ctx.send(embed=utils.embed.result(constants.alphanumeric.title_alphanumeric,
                                                lib.alphanumeric.alphanumeric(password), True))

    @_excel.command(name="countif", aliases=["count_if"])
    async def count_if(self, ctx, values: list, criteria):
        await ctx.send(embed=utils.embed.result(constants.excel.title_countif,
                                                lib.excel.count_if(values, criteria), True))

    @_excel.command(name="sumif", aliases=["sum_if"])
    async def sum_if(self, ctx, values, criteria):
        await ctx.send(embed=utils.embed.result(constants.excel.title_sumif,
                                                lib.excel.sum_if(values, criteria), True))

    @_excel.command(name="averageif", aliases=["average_if"])
    async def average_if(self, ctx, values, criteria):
        await ctx.send(embed=utils.embed.result(constants.excel.title_averageif,
                                                lib.excel.average_if(values, criteria), True))


def setup(bot):
    bot.add_cog(Main(bot))
