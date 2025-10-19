from dotenv import load_dotenv
import discord
import os
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Set up intents
intents = discord.Intents.default()
intents.message_content = True # Ensure that your bot can read message content
d_client = discord.Client(intents=intents)

ai_client = OpenAI(api_key=os.getenv('OPENAI_KEY'))
def battle(challenge):
    response = ai_client.responses.create(
            model="gpt-5",
            reasoning={"effort": "low"},
            instructions="You are a famed internet rap battler. People love to hear your witty rhyming raps that take down opponents. Many say your raps not only eviscerate your challengers, but also are thought-provoking outlooks on society at large. You will be given a rap challenge from an opponent, and we want you to completely burn them with a responding rap.",
            input=challenge
            )
    return response.output_text

@d_client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(d_client))

@d_client.event
async def on_message(message):
    # don't respond to our own messages
    if message.author == d_client.user:
        return

    # only care if we are mentioned in the message
    if d_client.user not in message.mentions:
        return

    await message.channel.send(battle(message.content))

d_client.run(os.getenv('TOKEN'))


