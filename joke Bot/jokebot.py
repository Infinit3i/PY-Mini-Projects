import discord
import random

client = discord.Client()
TOKEN = "<YOUR TOKEN HERE>"

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("?hello"):
        await message.channel.send("Hello!")

    if message.content.startswith("?dadjoke" and "?dj"):
        dadJokes = [
        "What time did the man go to the dentist? Tooth hurt-y.",
        "Did you hear about the guy who invented Lifesavers? They say he made a mint.",
        "A ham sandwich walks into a bar and orders a beer. Bartender says, 'Sorry we don't serve food here.'",
        "Whenever the cashier at the grocery store asks my dad if he would like the milk in a bag he replies, 'No, just leave it in the carton!'",
        "Why do chicken coops only have two doors? Because if they had four, they would be chicken sedans!",
        "Me: Dad, make me a sandwich! Dad Poof, You’re a sandwich!'",
        "Why did the Clydesdale give the pony a glass of water? Because he was a little horse!",
        "Me: 'Hey, I was thinking…' My dad: 'I thought I smelled something burning.'",
        "How do you make a Kleenex dance? Put a little boogie in it!",
        "Whenever we drive past a graveyard my dad says, 'Do you know why I can’t be buried there?' And we all say, 'Why not?' And he says, 'Because I’m not dead yet!'",
        "Two peanuts were walking down the street. One was a salted.",
        "I used to have a job at a calendar factory but I got the sack because I took a couple of days off.",
        "How do you make holy water? You boil the hell out of it.",
        "When I went to choir practice — Dad: 'Don’t forget a bucket.' Me: 'Why?' Dad: 'To carry your tune.'",
        "Two guys walk into a bar, the third one ducks.",
        "We were getting fast food when the lady at the window said, 'Any condiments?' My dad responded, 'Compliments? You look very nice today!'",
        "A woman is on trial for beating her husband to death with his guitar collection. Judge says, 'First offender?' She says, 'No, first a Gibson! Then a Fender!'",
        "Anytime I do something smart my dad says, 'Wow, you're a fart smella...I mean smart fella!'",
        "I had a dream that I was a muffler last night. I woke up exhausted!",
        "How do you tell the difference between a frog and a horny toad? A frog says, 'Ribbit, ribbit' and a horny toad says, 'Rub it, rub it.'",
        "On all of my medical forms growing up my dad wrote 'red' for my blood type. To this day no one knows my actual blood type.",
        "What is Beethoven's favorite fruit? A ba-na-na-na.",
        "My dad’s name is Phil, and whenever I finish eating and say, 'Dad, I’m full,' he always replies, 'No, I’m full; you're Ruby.'",
        "Did you hear about the restaurant on the moon? Great food, no atmosphere.",
        "What do you call a fake noodle? An Impasta.",
        "How many apples grow on a tree? All of them.",
        "Want to hear a joke about paper? Nevermind it's tearable. ",
        "I just watched a program about beavers. It was the best dam program I've ever seen.",
        "Why did the coffee file a police report? It got mugged.",
        "How does a penguin build it's house? Igloos it together.",
        "Dad, did you get a haircut? No I got them all cut.",
        "What do you call a Mexican who has lost his car? Carlos.",
        "Dad, can you put my shoes on? No, I don't think they'll fit me.",
        "Why did the scarecrow win an award? Because he was outstanding in his field.",
        "Why don't skeletons ever go trick or treating? Because they have no body to go with.",
        "Ill call you later. Don't call me later, call me Dad.",
        "What do you call an elephant that doesn't matter? An irrelephant",
        "Want to hear a joke about construction? I'm still working on it.",
        "What do you call cheese that isn't yours? Nacho Cheese.",
        "Why couldn't the bicycle stand up by itself? It was two tired.",
        "What did the grape do when he got stepped on? He let out a little wine.",
        "I wouldn't buy anything with velcro. It's a total rip-off.",
        "The shovel was a ground-breaking invention.",
        ]

        await message.channel.send(random.choice(dadJokes))

client.run(TOKEN)
