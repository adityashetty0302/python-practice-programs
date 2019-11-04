"""

Created by aditya on 25/12/18 at 4:00 PM

"""


class Hobbies:
    @staticmethod
    def find_hobbyists(hobbies, hobby):

        names = []

        for k, v in hobbies.items():
            if hobby in v:
                names.append(k)

        return names


hobbies = {
    "John": ['Piano', 'Puzzles', 'Yoga'],
    "Adam": ['Drama', 'Fashion', 'Pets'],
    "Mary": ['Magic', 'Pets', 'Reading']
}

print(Hobbies.find_hobbyists(hobbies, 'Yoga'));
