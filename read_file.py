import os
import random

file_count = 0


def read_file(folder, filename, new_file_each_run=False):
    global file_count

    f = open(filename, 'rb')

    if not os.path.exists(folder):
        os.makedirs(folder)

    if new_file_each_run:
        base_name = folder + '/' + 'copy_' + str(random.randint(99999, 9999999999999999)) + '_' + os.path.basename(
            f.name)
    else:
        base_name = folder + '/' + 'copy_' + str(file_count) + '_' + os.path.basename(f.name)

    new_f = open(base_name, 'w+')
    file_count += 1

    return [f, new_f]