#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from datetime import datetime
from time import sleep

import argparse
import requests
from pync import Notifier

from instagram_stalker.constants import *

class InstagramStalker(object):
    """InstagramStalker observes a given Instagram user's account 
    and notifies when he makes his account public"""

    def __init__(self, username, interval, play_sound, verbose):
        self.username = username
        self.interval = interval * 60
        self.play_sound = play_sound
        self.verbose = verbose

    def stalk(self):
        self._observe()

    def _observe(self):
        while 1:
            self._check()
            sleep(self.interval)

    def _check(self):
        r = requests.get(MEDIA_URL.format(self.username))
        now_str = datetime.now().strftime("%c")

        if r.status_code != 200:
            self._notify(
                    message=MESSAGE_ACCOUNT_UNAVAILABLE.format(
                now_str, self.username),
                    open_url=USER_URL.format(self.username),
                    notification_sound=NOTIFICATION_FAILURE_SOUND_NAME)
            sys.exit(0)
        else:
            data = r.json()
            items = data['items']
            if len(items) > 0:
                self._notify(
                        message=MESSAGE_ACCOUNT_PUBLIC.format(
                            now_str, self.username)
                        , open_url=USER_URL.format(self.username),
                        notification_sound=NOTIFICATION_SUCCESS_SOUND_NAME)
                sys.exit(0)
            elif self.verbose:
                print MESSAGE_ACCOUNT_PRIVATE.format(now_str, self.username)

    def _notify(self, message, open_url, notification_sound):
        options = {
                'title': NOTIFICATION_TITLE,
                'open': open_url,
        }
        if self.play_sound:
            options['sound'] = notification_sound

        Notifier.notify(message, **options)

def main():
    parser = argparse.ArgumentParser(
            description="Shows a notification when given Instagram username makes his profile public")

    parser.add_argument('username', help='Instagram user to observe')
    parser.add_argument('--interval', '-i', type=int, default=CHECK_INTERVAL, help="time interval in minutes for checking the given user's accout")
    parser.add_argument('--sound', '-s', action='store_true', help="play sound when notification pops", )
    parser.add_argument('--verbose', '-v', action='store_true', help="print logs to console when the account is still private")

    args = parser.parse_args()

    stalker = InstagramStalker(
            username=args.username,
            interval=args.interval, 
            play_sound=args.sound,
            verbose=args.verbose)
    stalker.stalk()

if __name__ == "__main__":
    main()
