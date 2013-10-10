#! /usr/bin/env python2
import pika
import yaml
import logging

rabbitmq_host = 'localhost'


storage_file_handler = logging.FileHandler('test_logging')
storage_file_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
logging.getLogger('storage').addHandler(storage_file_handler)
logging.getLogger('storage').setLevel(logging.DEBUG)

network_file_handler = logging.FileHandler('test_logging')
network_file_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
logging.getLogger('network').addHandler(network_file_handler)
logging.getLogger('network').setLevel(logging.INFO)

machine_file_handler = logging.FileHandler('test_logging')
machine_file_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
logging.getLogger('machine').addHandler(machine_file_handler)
logging.getLogger('machine').setLevel(logging.WARNING)

root_file_handler = logging.FileHandler('test_logging')
root_file_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
logging.getLogger('root').addHandler(root_file_handler)
logging.getLogger('root').setLevel(logging.ERROR)

class LogMaster:

    def __init__(self):
        self.masterkey = 'logmaster'
        self.key_set = set()
        self.conn_param = pika.ConnectionParameters(host=rabbitmq_host)
        self.connection = pika.SelectConnection(self.conn_param,
                                                self.on_connected)

    def serving_loop(self):
        self.connection.ioloop.start()
        print "endofloop??"

    def on_connected(self, connection):
        print "Connected to RabbitMQ!!!"
        connection.channel(self.on_channel_open)

    def on_channel_open(self, channel):
        print "Open channel in RabbitMQ!!!"
        self.channel = channel
        channel.exchange_declare(exchange='logservice', type='direct')
        channel.queue_declare(queue=self.masterkey)
        channel.queue_bind(exchange='logservice',
                           queue=self.masterkey,
                           routing_key=self.masterkey)

        channel.basic_consume(self.on_master_message,
                              queue=self.masterkey,
                              no_ack=True)

    def on_master_message(self, channel, method, header, body):
        msg = yaml.load(body)
        print msg['component']

        temp = logging.getLogger(msg['component'])
        if msg['type'] == 'debug':
            temp.debug(
                '%s %s %s %s %s %s %s %s',
                msg['component'],
                msg['type'],
                msg['file'],
                msg['func'],
                msg['linenu'],
                msg['user_name'],
                msg['uuid'],
                msg['message'])
        elif msg['type'] == 'info':
            temp.info(
                '%s %s %s %s %s %s %s %s',
                msg['component'],
                msg['type'],
                msg['file'],
                msg['func'],
                msg['linenu'],
                msg['user_name'],
                msg['uuid'],
                msg['message'])
        elif msg['type'] == 'warning':
            temp.warning(
                '%s %s %s %s %s %s %s %s',
                msg['component'],
                msg['type'],
                msg['file'],
                msg['func'],
                msg['linenu'],
                msg['user_name'],
                msg['uuid'],
                msg['message'])
        elif msg['type'] == 'error':
            temp.error(
                '%s %s %s %s %s %s %s %s',
                msg['component'],
                msg['type'],
                msg['file'],
                msg['func'],
                msg['linenu'],
                msg['user_name'],
                msg['uuid'],
                msg['message'])
        elif msg['type'] == 'critical':
            temp.critical(
                '%s %s %s %s %s %s %s %s',
                msg['component'],
                msg['type'],
                msg['file'],
                msg['func'],
                msg['linenu'],
                msg['user_name'],
                msg['uuid'],
                msg['message'])


log_master = LogMaster()
log_master.serving_loop()
