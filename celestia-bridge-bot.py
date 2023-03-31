from __future__ import print_function
import time
import os
import json
import requests
import sys
import datetime
import discord
from discord.ext import commands

token = os.environ['DISCORD_TOKEN']

# Discord Bot
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents, help_command=None)

# Output when Bot is online and ready to use
@client.event
async def on_ready():
	print('Bot is ready.')
	print('Logged in as:')
	print(client.user.name)
	print(client.user.id)
	print('------')

# Error Handling
@client.event
async def on_command_error(ctx, error):

	if isinstance(error, commands.errors.MissingRequiredArgument):
		embed = discord.Embed(title="", description="", timestamp=datetime.datetime.utcnow(), color=0xff0000)
		embed.set_author(name="ITN Bridge Node Status", icon_url="https://pbs.twimg.com/profile_images/1404854187721203715/zZp1s7c3_400x400.jpg")
		embed.add_field(name="Error:", value='`Missing Bridge Node ID`', inline=False)
		await ctx.send(ctx.author.mention)
		await ctx.send(embed=embed)
		return

	if isinstance(error, commands.errors.CommandNotFound):
		embed = discord.Embed(title="", description="", timestamp=datetime.datetime.utcnow(), color=0xff0000)
		embed.set_author(name="ITN Bridge Node Status", icon_url="https://pbs.twimg.com/profile_images/1404854187721203715/zZp1s7c3_400x400.jpg")
		embed.add_field(name="Error:", value='`%s`' % error, inline=False)
		await ctx.send(ctx.author.mention)
		await ctx.send(embed=embed)
		return

	if isinstance(error, commands.errors.CommandInvokeError):
		embed = discord.Embed(title="", description="", timestamp=datetime.datetime.utcnow(), color=0xff0000)
		embed.set_author(name="ITN Bridge Node Status", icon_url="https://pbs.twimg.com/profile_images/1404854187721203715/zZp1s7c3_400x400.jpg")
		embed.add_field(name="Error:", value='`Invalid Bridge Node ID or response was empty`', inline=False)
		await ctx.send(ctx.author.mention)
		await ctx.send(embed=embed)
		return

# $help Command
client.remove_command('help')

@client.command()
async def help(ctx):
    embed = discord.Embed(title="", description="", timestamp=datetime.datetime.utcnow(), color=0x792BF9)
    embed.set_author(name="Available Commands", icon_url="https://pbs.twimg.com/profile_images/1404854187721203715/zZp1s7c3_400x400.jpg")
    embed.add_field(name="Bridge Node Status", value="`$status <bridge_node_id>`", inline=False)
    await ctx.send(ctx.author.mention)
    await ctx.send(embed=embed)

# $status Command
@client.command()
async def status(ctx, arg1, *argv):

	response = requests.get('https://leaderboard.celestia.tools/api/v1/nodes/'+arg1+'')

	json = response.json()
	node_id = json['node_id']
	uptime = str(round(json['uptime'], 2)) + '%'
	head = json['head']
	network_height = json['network_height']
	total_synced_headers = json['total_synced_headers']
	start_time = json['start_time']
	last_restart_time = json['last_restart_time']

	# Node Uptime
	node_runtime_counter_in_seconds = json['node_runtime_counter_in_seconds']
	node_uptime = datetime.timedelta(seconds = node_runtime_counter_in_seconds)

	embed = discord.Embed(title="", description="", timestamp=datetime.datetime.utcnow(), color=0x792BF9)
	embed.set_author(name="ITN Bridge Node Status", icon_url="https://pbs.twimg.com/profile_images/1404854187721203715/zZp1s7c3_400x400.jpg")
	embed.add_field(name="Bridge Node ID:", value=node_id, inline=False)
	embed.add_field(name="Uptime:", value=uptime, inline=True)
	embed.add_field(name="Head:", value=head, inline=True)
	embed.add_field(name="Network Height:", value=network_height, inline=True)
	embed.add_field(name="Total Synced Headers:", value=total_synced_headers, inline=False)
	embed.add_field(name="Uptime Since Last Restart:", value=node_uptime, inline=True)
	embed.add_field(name="Last Restart:", value=last_restart_time, inline=True)
	embed.add_field(name="Bridge Node Start Time:", value=start_time, inline=False)
	embed.set_footer(text="Made by 0xFury", icon_url="https://pbs.twimg.com/profile_images/1618486399107309568/pxn2clZj_400x400.jpg")
	await ctx.send(ctx.author.mention)
	await ctx.send(embed=embed)

client.run(token)