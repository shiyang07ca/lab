from threading import Thread
from random import randint
from time import sleep

# Sleep a random number of seconds (between 1 and 5)

cnt = 0
lst = [1] * 20000000


def add():
    global cnt

    sleep(randint(1, 5) / 1000)
    for _ in range(100000):
        # cnt += 1
        cnt = cnt + 1
        # lst.append(1)
        lst.pop()


def main():
    print(f'before: {cnt}')

    threads = []

    for i in range(100):
        t = Thread(target=add)
        t.start()
        # t.join()
        threads.append(t)

    for thread in threads:
        thread.join()

    print(f'after: {cnt}')
    print(f'after: {len(lst)}')


if __name__ == '__main__':
    main()
