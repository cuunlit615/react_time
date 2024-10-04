import random
import time

while True:
    start = input("press enter while 'go' show up\n press enter continue")
    if start == '':
        print('START')
        t_range = random.randint(0, 10)
        time.sleep(t_range)
    else:
        break

    inp = input('GO!!!')
    t_start = time.time()
    if inp == '':
        t_end = time.time()
        print('react time is ', t_end - t_start, 's')
    else:
        print('oops, wrong button')
