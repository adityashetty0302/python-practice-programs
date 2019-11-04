"""

Created by aditya on 25/12/18 at 2:03 PM

"""


class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """

        if self.next == None:
            return False
        else:
            return True



first = Song("Hello")
second = Song("Eye of the tiger")

first.next_song(second);
second.next_song(first);

print(first.is_repeating_playlist())