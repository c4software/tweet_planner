# -*- coding: utf-8 -*-
import argparse
import logging
import tweepy
import sys
import os.path

from secrets import consumer_key, consumer_secret, access_token, access_token_secret

parser = argparse.ArgumentParser(description="Tweet planner")
parser.add_argument('-i', '--init', action='store_true', help='Init the « queue » tweets databases.')
parser.add_argument('--debug', action='store_true', help='Debug mode')
parser.add_argument('-a', '--add', help="Add a new tweet to the « queue ».")
args = parser.parse_args()

queue_file_name = queue_file_name

if args.debug:
    logging.basicConfig(level=logging.DEBUG)

def send_tweet():
    logging.debug("Send Tweet")
    twitter_api = tweeter_auth()

def tweeter_auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

def add_to_queue(text):
    logging.debug("Add tweet to queue")
    if len(text) > 140:
        logging.error("The text can’t exceed 140 characters")
        sys.exit()
    else:
        with open(queue_file_name, "a") as queue_file:
            queue_file.write(text)

def check_queue_file():
    return os.path.isfile(queue_file_name)

def init_queue():
    logging.debug("Init queue")
    open(queue_file_name, 'a').close()

if __name__ == '__main__':
    try:
        # Test if queue is present
        if not args.init and not check_queue_file():
            logging.error("To use Tweet Planner you must init the queue (use the -i flags)")
            sys.exit()

        if args.init:
            init_queue()
        elif args.add:
            add_to_queue(args.add)
        else:
            send_tweet()
    except tweepy.error.TweepError as e:
        print("Twitter error: {0}".format(e))
    except Exception as e:
        print("Error: {0}".format(e))
