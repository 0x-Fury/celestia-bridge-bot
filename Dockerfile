# docker build -t 0xfury/celestia-bridge-bot .

FROM python:3

ENV DISCORD_TOKEN=''

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY celestia-bridge-bot.py ./

CMD [ "python", "./celestia-bridge-bot.py" ]