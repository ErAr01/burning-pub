import time

counter = 0
users = 0


def main_funct(peak_one):
    global counter, users

    t = 60 / peak_one
    counter += t
    users += 1
    time.sleep(t)
    return [counter, users]


if __name__ == '__main__':
    while counter <= 60:
        print(main_funct(50))
