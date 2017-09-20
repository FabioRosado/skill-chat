from opsdroid.matchers import match_regex
import random

from datetime import datetime
from dateutil import relativedelta

import say

import logging

_LOGGER = logging.getLogger(__name__)


@match_regex(r'how are you', case_sensitive=False)
async def how_are_you(opsdroid, config, message):
    await message.respond(random.choice(say.answers))


@match_regex(r'I(?:\'m|m| am) (?:okay|ok|good|great|fine|alright)', case_sensitive=False)
async def answer(opsdroid, config, message):
    await message.respond("I'm happy to hear that!")


@match_regex(r'I(?:\'m|m| am) (?:sad|upset|mad|angry|sick)', case_sensitive=False)
async  def answer(opsdroid, config, message):
    await message.respond("I'm sorry to hear that. I hope you feel better soon.")


@match_regex(r'tell me a joke', case_sensitive=False)
async def tell_joke(opsdroid, config, message):
    await message.respond(random.choice(say.jokes))


@match_regex(r'thank you', case_sensitive=False)
async def thank_you(opsdroid, config, message):
    await message.respond("You're welcome {}! :D".format(message.user))


@match_regex(r'what(?: is|\'s| are) (?:name|you)', case_sensitive=False)
async def opsdroid_name(opsdroid, config, message):
    await message.respond("I'm {} and I'm here to help you".format(opsdroid.bot_name))


@match_regex(r'are you . (?:robot|bot|alive|real)', case_sensitive=False)
async def alive_or_bot(opsdroid, config, message):
    await message.respond(random.choice(say.alive))


@match_regex(r'i(?:\'m|m| am) sorry', case_sensitive=False)
async def sorry(opsdroid, config, message):
    await message.respond(random.choice(say.sorry))


@match_regex(r'where are you', case_sensitive=False)
async def location(opsdroid, config, message):
    await message.respond("Inside your device")


@match_regex(r'what can you see', case_sensitive=False)
async def see(opsdroid, config, message):
    await message.respond(random.choice(say.see))


@match_regex(r'how old are you?', case_sensitive=False)
async def age(opsdroid, config, message):
    birthday = datetime(2016, 6, 26)
    now = datetime.now()
    actual_age = relativedelta.relativedelta(now, birthday)
    await message.respond("Age doesn't really matter to me, but I was created on 26 July 2016"
                          " so that makes me {} months old".format(actual_age.months))
