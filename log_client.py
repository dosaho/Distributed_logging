#! /usr/bin/env python2
import yaml
import sys
import pika
import uuid
import os
import logging
import inspect


class getLogger:

    def __init__(self, component_name):
        print component_name 


'''
def log_info(user, component, extra=None):
    
    f = inspect.currentframe()
    f = f.f_back
    co = f.f_code
 
    key = 'logmaster'
    conn_param = pika.ConnectionParameters(host='localhost')
    connection = pika.BlockingConnection(conn_param)
    channel = connection.channel()
    msg = {'user': user.name,
           'request': user.action,
           'uuid': user.uuid,
           'component': component,
           'extra': extra,
           'type': 'info',
           'linenu':inspect.getlineno(f),
           'file':co.co_filename,
           'func':co.co_name}
    msg = yaml.dump(msg)
    print yaml.load(msg)
    channel.basic_publish( exchange='logservice', routing_key= key, body= msg)
        
        
    
def log_warning(user, component, extra=None):
    f = inspect.currentframe()
    f = f.f_back
    co = f.f_code
    
    key = 'logmaster'
    conn_param = pika.ConnectionParameters(host='localhost')
    connection = pika.BlockingConnection(conn_param)
    channel = connection.channel()
    msg = {'user': user.name,
           'request': user.action,
           'uuid': user.uuid,
           'component': component,
           'extra': extra,
           'type': 'warning',
           'linenu':inspect.getlineno(f),
           'file':co.co_filename,
           'func':co.co_name}


    msg = yaml.dump(msg)
    print yaml.load(msg)
    channel.basic_publish( exchange='logservice', routing_key= key, body= msg)

    
def log_error(user, component, extra=None):
    f = inspect.currentframe()
    f = f.f_back
    co = f.f_code

    key = 'logmaster'
    conn_param = pika.ConnectionParameters(host='localhost')
    connection = pika.BlockingConnection(conn_param)
    channel = connection.channel()
    msg = {'user': user.name,
           'request': user.action,
           'uuid': user.uuid,
           'component': component,
           'extra': extra,
           'type': 'error',
           'linenu':inspect.getlineno(f),
           'file':co.co_filename,
           'func':co.co_name}

    msg = yaml.dump(msg)
    print yaml.load(msg)
    channel.basic_publish( exchange='logservice', routing_key= key, body= msg)
'''










""" 
       self.key = 'logmaster'
        self.conn_param = pika.ConnectionParameters(host='localhost')
        self.connection = pika.BlockingConnection(self.conn_param)
        self.channel = self.connection.channel()
        msg = {'User': user, 
               'Request': request, 
               'Component': component,
               'uuid': uuid,
               'status': status}
        msg_p = yaml.dump(msg)
        self.channel.basic_publish( exchange='logservice', routing_key= self.key, body= msg_p )
        print yaml.dump(msg)
"""




