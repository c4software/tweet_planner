# -*- coding: utf-8 -*-
import sys, argparse, logging, random, datetime
import os.path
import tweepy

from secrets import consumer_key, consumer_secret, access_token, access_token_secret

parser = argparse.ArgumentParser(description="Tweet planner")
parser.add_argument('-i', '--init', action='store_true', help='Init the « queue » tweets databases.')
parser.add_argument('-d', '--debug', action='store_true', help='Debug mode')
parser.add_argument('-a', '--add', help="Add a new tweet to the « queue ».")
args = parser.parse_args()

if args.debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

def send_tweet():
    api = tweeter_auth()
    last_update = api.user_timeline(count=1)[0].created_at
    if datetime.datetime.utcnow()-datetime.timedelta(minutes=20) > last_update:
        text = get_from_queue()
        if text:
            api.update_status(status=text)
        else:
            logging.info("Nothing to tweet.")
    else:
        logging.info("Last tweet too recent.")

def tweeter_auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

def get_from_queue():
    try:
        with open("waiting.txt", "r+") as queue_file:
            queue = queue_file.readlines()
            text = random.choice(queue)
            queue.remove(text)
            queue_file.seek(0)
            queue_file.truncate()
            queue_file.writelines(queue)
            return text
    except:
        return None

def add_to_queue(text):
    logging.debug("Add tweet to queue")
    if len(text) > 140:
        logging.error("The text can’t exceed 140 characters")
        sys.exit()
    else:
        with open("waiting.txt", "a") as queue_file:
            queue_file.write("{0}\n".format(text))

def check_queue_file():
    return os.path.isfile("waiting.txt")

def init_queue():
    logging.debug("Init queue")
    open("waiting.txt", 'a').close()

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
