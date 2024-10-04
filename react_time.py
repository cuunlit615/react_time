import random
import time
import os

times = []

while True:
    input("press enter while 'go' show up\n press enter continue")
    print('START')
    t_range = random.randint(0, 3)
    time.sleep(t_range)
    print('GO!!!')
    t_start = time.time()
    record = None
    input()
    t_end = time.time()
    record_ = t_end - t_start
    times.append(record)
    times.sort()
    print('react time is %2f' % record_, 's')
    print('best time', times[0])
    input('press enter to try again')
    os.system('cls')

