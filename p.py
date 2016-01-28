__name__ = "vutsuak"

import os

dir = 'E:\PinkFloyd\Pink Floyd'
ct = 0
list = ['E:\PinkFloyd\Pink Floyd\Pink Floyd - The Dark Side of the Moon',
        'E:\PinkFloyd\Pink Floyd\Pink Floyd Wish You Were Here']
for sub_dir in os.listdir(dir):
    sub_dir = 'E:\PinkFloyd\Pink Floyd' + '\\' + sub_dir

    for files in os.listdir(sub_dir):
        if sub_dir in list:
            files = files.lower().strip()[3:]
        else:
            files = files.lower().strip()[5:]
        filename, ext = os.path.splitext(files)
        if ext == '.mp3':
            ct += 1

print ct
