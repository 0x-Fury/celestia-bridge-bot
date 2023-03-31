# celestia-bridge-bot

**Clone Repo & Build Image:**

```
cd $HOME && \
git clone https://github.com/0x-Fury/celestia-bridge-bot.git && \
cd celestia-bridge-bot && \
docker build -t 0xfury/celestia-bridge-bot .
```

**Run Docker Image:**

```
docker run -d -e DISCORD_TOKEN=<server_token> --name celestia-bridge-bot 0xfury/celestia-bridge-bot:latest
```

* Edit `<server_token>` in the environmental variable `DISCORD_TOKEN` to reflect the Discord bot token

## Create Discord Bot ##

1. Login to Discord https://discord.com/
2. Head to the 'Navigation' page and click 'New Application' ( https://discord.com/developers/applications )
3. Choose a name for the app
4. Go to the 'Bot' tab and then click 'Add Bot'
5. Once the bot is added, copy the token. This token is used in the `docker run` command env var `-e DISCORD_TOKEN=<server_token>`
6. Ensure 'MESSAGE CONTENT INTENT' is toggled on
7. Go to the 'OAuth2' tab and then click the 'URL Generator' tab
8. Check off 'bots' under Scopes. Under 'bot permissions' check off 'Send Messages'. Copy the generated invite URL.
9. Use the generated invite URL to add the bot to a server
10. Run docker image to start the bot

## Discord Bot Commands ##

* `$help`
* `$status <bridge_node_id>`
