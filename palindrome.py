"""

Created by aditya on 25/12/18 at 1:36 PM

"""


class Palindrome:

    @staticmethod
    def is_palindrome(word):
        word = str(word).lower()
        word_rev = word[::-1]
        word_rev = word_rev.lower()
        if word == word_rev:
            return True
        else:
            return False


print(Palindrome.is_palindrome('Deleveled'))
