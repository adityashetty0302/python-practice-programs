def prime(num):
    for element in range(2, num):
        if num % element == 0:
            return False
    # print('yes', num)
    return True
