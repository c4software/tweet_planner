# -*- coding: utf-8 -*-
import argparse
import logging
import tweepy

from secrets import consumer_key, consumer_secret, access_token, access_token_secret


parser = argparse.ArgumentParser(description="Tweet planner")

parser.add_argument('-i', '--init', action='store_true', help='Init the « queue » tweets databases.')
parser.add_argument('--debug', action='store_true', help='Debug mode')
parser.add_argument('-a', '--add', help="Add a new tweet to the « queue ».")
args = parser.parse_args()

if args.debug:
    logging.basicConfig(level=logging.DEBUG)

def send_tweet():
    logging.debug("Send Tweet")
    twitter_api = tweeter_auth()

def tweeter_auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

def add_queue():
    logging.debug("Add tweet to queue")
    pass

def init_queue():
    logging.debug("Init queue")
    open("waiting.txt", 'a').close()

if __name__ == '__main__':
    try:
        if args.init:
            init_queue()
        elif args.add:
            add_queue()
        else:
            send_tweet()
    except tweepy.error.TweepError as e:
        print("Twitter error: {0}".format(e))
    except Exception as e:
        print("Error: {0}".format(e))
