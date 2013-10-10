import dlogging

user = {'user_name': 'test1', 'uuid': 1234}


def function1():
    c = dlogging.getLogger('storage.1')
    c.debug()
    c.info('20', extra=user)
    c.warning('30', extra=user)
    c.error('40', extra=user)
    c.critical('50', extra=user)


def function2():
    d = dlogging.getLogger('network.comp_1.sub_comp_1')
    d.debug('10', extra=user)
    d.info('20', extra=user)
    d.warning('30', extra=user)
    d.error('40', extra=user)
    d.critical('50', extra=user)


def function3():
    e = dlogging.getLogger('machine.comp_1.sub_comp_1.test1')
    e.debug('10')
    e.info('20')
    e.warning('30')
    e.error('40')
    e.critical('50')


def function4():
    f = dlogging.getLogger()
    f.debug('10')
    f.info('20')
    f.warning('30')
    f.error('40')
    f.critical('50')


def function5():
    c = dlogging.getLogger('storage')
    c.debug('10', extra=user)
    c.info('20', extra=user)
    c.warning('30', extra=user)
    c.error('40', extra=user)
    c.critical('50', extra=user)


function1()
#function2()
#function3()
#function4()
#function5()
