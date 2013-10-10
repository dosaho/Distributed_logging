#! /usr/bin/env python2

import log_client 
from user import User
import logging




def function1():
    log_client.log_info(user ,'componentA.a')

def function2():
    log_client.log_warning(user, 'componentA.b', 'format_error')

def function3():
    log_client.log_error(user, 'componentB.a')


user = User('test_name', 'add_question')


log_client.log_info(user ,'componentA.a')
log_client.log_warning(user, 'componentA.b', 'format_error')
log_client.log_error(user, 'componentB.a')


function1()
function2()
function3()


