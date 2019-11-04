if __name__ == '__main__':
    for n in range(2, 100):
        for x in range(2, int(n / 2) + 1):
            if n % x == 0:
                break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')
