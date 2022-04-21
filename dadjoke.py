#!/usr/bin/env python3
# GitStoph
# Originally taken from https://gist.github.com/itsthejoker and edited for prettier print and more jokes.
########################################################################
import requests
from rich import print
import random

resp = requests.get("https://fatherhood.gov/jsonapi/node/dad_jokes")
resp2 = requests.get("https://fatherhood.gov/jsonapi/node/dad_jokes?page%5Boffset%5D=50&page%5Blimit%5D=50")
resp3 = requests.get("https://fatherhood.gov/jsonapi/node/dad_jokes?page%5Boffset%5D=150&page%5Blimit%5D=50")
jokes = resp.json()['data'] + resp2.json()['data'] + resp3.json()['data']
joke = random.choice(jokes)
if joke:
    print("[green] {0}".format(joke['attributes']['field_joke_opener']))
    print("[yellow] {0}".format(joke['attributes']['field_joke_response']))