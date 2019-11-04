# Task 2
#
# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
#
# My name is Michele
#
# Then I would see the string:
#
#  Michele is name My
#
# shown back to me.


def str_rev(ip_str):
    words_list = ip_str.split()
    rev_words_list = words_list[::-1]
    op_str = ' '.join(rev_words_list)

    return op_str


print('Enter a long string')
input_string = str(input())
output_string = str_rev(input_string)
print(output_string)
