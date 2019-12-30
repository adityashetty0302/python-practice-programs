arr = [1, 3, 0, 4, 0, 8, 0, 2]
print(arr)

# count = 0
# result = []
#
# for i in arr:
#     if i != 0:
#         result.append(i)
#     else:
#         count += 1
#
# for x in range(count):
#     result.append(0)
#
# print(result)


# more shorter way

result = [nz for nz in arr if nz != 0] + [z for z in arr if z == 0]
print(result)
