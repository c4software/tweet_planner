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

def main():
    twitter_api = tweeter_auth()

def tweeter_auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

if __name__ == '__main__':
    try:
        main()
    except tweepy.error.TweepError as e:
        print("Twitter error: {0}".format(e))
    except Exception as e:
        print("Error: {0}".format(e))
