#! /usr/bin/env python2
import yaml
import sys
import pika
import uuid
import os

class User(object):

    def __init__(self, user_name, user_action):
        user_uuid = uuid.uuid1()
        self.name = user_name
        self.action = user_action
        self.uuid = user_uuid

