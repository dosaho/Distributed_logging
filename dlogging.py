#! /usr/bin/env python2
import yaml
import sys
import pika
import uuid
import os
import logging
import inspect

key = 'logmaster'
rabbitmq_host = 'localhost'


class getLogger:

    def __init__(self, component_name='root'):
        self.component_name = component_name

    def debug(self, message=None, extra=None):

        self.f = inspect.currentframe()
        self.f = self.f.f_back
        self.co = self.f.f_code

        msg = self.get_code_msg(message, self.component_name, extra, 'debug', self.f, self.co)
        self.send_msg(msg)

    def info(self, message=None, extra=None):
        self.f = inspect.currentframe()
        self.f = self.f.f_back
        self.co = self.f.f_code

        msg = self.get_code_msg(message, self.component_name, extra, 'info', self.f, self.co)
        self.send_msg(msg)

    def warning(self, message=None, extra=None):
        self.f = inspect.currentframe()
        self.f = self.f.f_back
        self.co = self.f.f_code

        msg = self.get_code_msg(message, self.component_name, extra, 'warning', self.f, self.co)
        self.send_msg(msg)

    def error(self, message=None, extra=None):
        self.f = inspect.currentframe()
        self.f = self.f.f_back
        self.co = self.f.f_code

        msg = self.get_code_msg(message, self.component_name, extra, 'error', self.f, self.co)
        self.send_msg(msg)

    def critical(self, message=None, extra=None):
        self.f = inspect.currentframe()
        self.f = self.f.f_back
        self.co = self.f.f_code

        msg = self.get_code_msg(message, self.component_name, extra, 'critical', self.f, self.co)
        self.send_msg(msg)

    def send_msg(self, msg):
        self.conn_param = pika.ConnectionParameters(host=rabbitmq_host)
        self.connection = pika.BlockingConnection(self.conn_param)
        self.channel = self.connection.channel()
        msg = yaml.dump(msg)
        print msg
        self.channel.basic_publish(exchange='logservice', routing_key=key, body=msg)
        #self.channel.close()

    def get_code_msg(self, message, component, extra, type, frame, code_info):

        msg = {'component': component,
               'type': type,
               'linenu': inspect.getlineno(frame),
               'file': code_info.co_filename,
               'func': code_info.co_name,
               'message': message}
        if extra is not None:
            msg.update(extra)
        else:
            extra = {'user_name': 'No define', 'uuid': 'No define'}
            msg.update(extra)

        print msg
        return msg


class FileHandler:

    def __init__(self, file_path=None):
        print file_path
        if file_path is None:
            self.Handler = logging.FileHandler('/var/log/d_logging.log')
        else:
            self.Handler = logging.FileHandler(file_path)

    def setFormatter(self, formatter):
        self.Handler.setFormatter(formatter)

    def setLevel(self, level):
        self.Handler.setLevel(level)
