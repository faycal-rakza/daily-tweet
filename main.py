#!/usr/bin/env python
# -*- coding: utf-8 -*-

import authentication

text = "Hello, World!"


def tweet():
    try:
        client = authentication.client

        client.create_tweet(
            text="text"
        )
        print("Tweeted!")
    except Exception as e:
        print("An error occurred")
        print(e)


tweet()
