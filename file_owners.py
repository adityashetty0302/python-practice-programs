"""

Created by aditya on 25/12/18 at 1:42 PM

"""


class FileOwners:

    @staticmethod
    def group_by_owners(files):
        val = list(set(list(files.values())))
        fd = {x: [] for x in val}
        for i in val:
            for k, v in files.items():
                if v == i:
                    fd[i].append(k)
        return fd


files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))
