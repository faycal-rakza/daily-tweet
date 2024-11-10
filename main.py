#!/usr/bin/env python
# -*- coding: utf-8 -*-

import authentication
import os
from dotenv import load_dotenv

load_dotenv()

tweet_text = os.getenv('TWEET_TEXT')


def tweet():
    try:
        client = authentication.client

        client.create_tweet(
            text=tweet_text
        )
        print("Tweeted!")
    except Exception as e:
        print("An error occurred")
        print(e)


tweet()
