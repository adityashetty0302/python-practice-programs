"""

Created by aditya on 25/12/18 at 4:35 PM

"""

import stringsnum_test


class NumbersToText:

    @staticmethod
    def numbers_to_letters(s):
        sen = ''
        d1 = {}

        for i in range(1, 27):
            d1[i] = chr(64 + i)

        split = s.split()
        for j in split:
            if '+' not in j:
                val = d1[int(j)]
                sen += val
            else:
                j_split = j.split('+')
                val = d1[int(j_split[0])]
                sen += val + ' '
                val = d1[int(j_split[1])]
                sen += val

        return sen


print(NumbersToText.numbers_to_letters('20 5 19 20+4 15 13 5'))
