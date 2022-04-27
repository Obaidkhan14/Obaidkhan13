import discord

from discord.ext import commands

import asyncio

import time

import random

import math

debug = False

random.seed()

f = open("login.txt",mode='r')

loginDetails = {}

for line in f.readlines():

    if '=' in line:

        tokens = line.split('=')

        loginDetails[tokens[0]] = tokens[1].rstrip()

version = "0.9.9"
