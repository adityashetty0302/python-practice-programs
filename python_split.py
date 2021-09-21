# a.split('ab')
def split(input, x=None):
    if not x:
        return [input]
    x_len = len(x)
    result = []
    skip = []
    start = 0
    end = 0
    counter = 0
    for elem in range(0, len(input)):
        if x == input[elem : elem + x_len]:
            skip.append(counter)
        counter += 1
    # print(skip)
    for end in skip:
        result.append(input[start:end])
        start = end + x_len
    result.append(input[start:])
    result = [q for q in result if q]
    return result


print(split("ab #babab", " #"))  # ['ab', "babab"]
print(split("abbabab", "a"))  # ['bb', 'b', 'b']
print(split("aaaa"))  # ['aaaa']
