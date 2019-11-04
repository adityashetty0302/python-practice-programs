"""

Created by aditya on 25/12/18 at 12:32 PM

"""


class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        new_path = str(new_path)
        og_path = str(self.current_path)

        if '..' in new_path:
            og_path_split = og_path.rsplit('/', 1)
            og_path = og_path_split[0]
            new_path = new_path.lstrip('..')
            new_path_split = new_path.split('/')
            for i in new_path_split:
                if i:
                    og_path += '/' + i

            self.current_path = og_path

        else:

            og_path += '/' + new_path
            self.current_path = og_path


path = Path('/a/b/c/d')
path.cd('x')
print(path.current_path)
