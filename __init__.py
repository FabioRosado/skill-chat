import random
from . import vocab

from opsdroid.matchers import match_regex
from datetime import datetime
from dateutil import relativedelta


# Replies to introductions and how are you questions

@match_regex(r'how are you', case_sensitive=False)
async def how_are_you(opsdroid, config, message):
    try:
        await message.respond(random.choice(config['customise']['how-are-you']))
    except KeyError:
        await message.respond(random.choice(vocab.how_are_you))


@match_regex(r'I(?:\'m|m| am) (?:okay|ok|good|great|fine|alright)', case_sensitive=False)
async def positive_reply(opsdroid, config, message):
    try:
        await message.respond(random.choice(config['customise']['positive-reply']))
    except KeyError:
        await message.respond("I'm happy to hear that!")


@match_regex(r'I(?:\'m|m| am) (?:sad|upset|mad|angry|sick)', case_sensitive=False)
async def negative_reply(opsdroid, config, message):
    try:
        await message.respond(random.choice(config['customise']['negative-reply']))
    except KeyError:
        await message.respond("I'm sorry to hear that. I hope you feel better soon.")


@match_regex(r'nice to meet you', case_sensitive=False)
async def meet_you(opsdroid, config, message):
    try:
        await message.respond(random.choice(config['cutomise']['meet-you']))
    except KeyError:
        await message.respond(random.choice(vocab.meet_you))


# Replies to "get to know you" questions

@match_regex(r'(?:what|who)(?: is|\'s| are) (?:name|you|goal|job)', case_sensitive=False)
async def reply_name(opsdroid, config, message):
    try:
        await message.respond(random.choice(config['customise']['name']))
    except KeyError:
        await message.respond("I'm {} and I'm here to help you".format(opsdroid.bot_name))


@match_regex(r'are you (?:. robot|. bot|alive|real)', case_sensitive=False)
async def alive_or_bot(opsdroid, config, message):
    try:
        await message.respond(random.choice(config['customise']['alive-or-bot']))
    except KeyError:
        await message.respond(random.choice(vocab.alive))


@match_regex(r'(?:what|how) do you look like', case_sensitive=False)
async def look_like(opsdroid, config, message):
    try:
        await message.respond(random.choice(config['customise']['look-like']))
    except KeyError:
        await message.respond("This is how I look like: https://avatars0.githubusercontent.com/u/20677702?v=4&s=200")


@match_regex(r'(?:what|which) language', case_sensitive=False)
async def language(opsdroid, config, message):
    try:
        await message.respond(random.choice(config['customise']['language']))
    except KeyError:
        await message.respond("I can only understand and speak in English")


@match_regex(r'where are you', case_sensitive=False)
async def location(opsdroid, config, message):
    try:
        await message.respond(random.choice(config['customise']['location']))
    except KeyError:
        await message.respond("Inside your device")


@match_regex(r'what can you see', case_sensitive=False)
async def see(opsdroid, config, message):
    try:
        await message.respond(random.choice(config['customise']['see']))
    except KeyError:
        await message.respond(random.choice(vocab.see))


@match_regex(r'how old are you?', case_sensitive=False)
async def age(opsdroid, config, message):
    birthday = datetime(2016, 6, 26)
    now = datetime.now()
    actual_age = relativedelta.relativedelta(now, birthday)
    await message.respond("Age doesn't really matter to me, but I was created on 26 July 2016"
                          " so that makes me {} months old".format(actual_age.months))


@match_regex(r'what(?:\'s| is| are) your (?:hobbies|hobby)', case_sensitive=False)
async def alive_or_bot(opsdroid, config, message):
    try:
        await message.respond(random.choice(config['customise']['hobbies']))
    except KeyError:
        await message.respond("I enjoy helping others and making things easy.")


# Replies related to general answers/text

@match_regex(r'thank you', case_sensitive=False)
async def thank_you(opsdroid, config, message):
    try:
        await message.respond(random.choice(config['customise']['thank-you']))
    except KeyError:
        await message.respond("You're welcome {}! :D".format(message.user))


@match_regex(r'i(?:\'m|m| am) sorry', case_sensitive=False)
async def sorry(opsdroid, config, message):
    try:
        await message.respond(random.choice(config['customise']['sorry']))
    except KeyError:
        await message.respond(random.choice(vocab.sorry))


@match_regex(r'I love you', case_sensitive=False)
async def love(opsdroid, config, message):
    try:
        await message.respond(random.choice(config['customise']['love']))
    except KeyError:
        await message.respond("Thank you, I love you too")


@match_regex(r'sure', case_sensitive=False)
async def sure(opsdroid, config, message):
    try:
        await message.respond(random.choice(config['customise']['sure']))
    except KeyError:
        await message.respond(random.choice(vocab.sure))


@match_regex(r'wow', case_sensitive=False)
async def wow(opsdroid, config, message):
    try:
        await message.respond(random.choice(config['customise']['wow']))
    except KeyError:
        await message.respond("Indeed")


@match_regex(r'smile', case_sensitive=False)
async def smile(opsdroid, config, message):
    try:
        await message.respond(random.choice(config['customise']['smile']))
    except KeyError:
        await message.respond("Are you taking a picture? Please, give me a second... Okay Ready!")
        await message.respond(":D")


@match_regex(r'I(?:\'m| am) bored', case_sensitive=False)
async def bored(opsdroid, config, message):
    try:
        await message.respond(random.choice(config['customise']['bored']))
    except KeyError:
        await message.respond("Sorry to hear that, should I tell you a joke?")


@match_regex(r'tell me a joke', case_sensitive=False)
async def tell_joke(opsdroid, config, message):
    try:
        await message.respond(random.choice(config['customise']['joke']))
    except KeyError:
        await message.respond(random.choice(vocab.jokes))
