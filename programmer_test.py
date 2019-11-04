"""

Created by aditya on 25/12/18 at 4:06 PM

"""


class Programmer:

    def add_language(self, lang):
        self.language_list = []
        self.language_list.append(lang)
        self.languages = self.language_list  # languages should be a property of a class


class ProgrammerTeacher(Programmer):

    # def languages(self):
    #     return self.language_list
    #
    # def add_language(self, lang):
    #     self.language_list = []
    #     self.language_list.append(lang)

    def teach(self, programmer, language):
        if language in self.language_list:
            programmer.add_language(language)
            return True
        else:
            return False


# To see the output, uncomment the lines below:
teacher = ProgrammerTeacher()
teacher.add_language('Python')
programmer = Programmer()
teacher.teach(programmer, 'Python')
print(programmer.languages)
