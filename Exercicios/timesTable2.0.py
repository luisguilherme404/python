import random
import time

while True:

    try:
        num = random.randint(1, 10)

        print('Number provided: {:^5}'.format(num))

        for i in range(0, 13):
            mult = num * i

            print(f'{num} x {i} = {mult}')

        time.sleep(3)

    except KeyboardInterrupt:
        break