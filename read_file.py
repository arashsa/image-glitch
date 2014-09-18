import os
import random

file_count = 0


def read_file(folder, filename):
    global file_count

    f = open(filename, 'rb')

    if not os.path.exists(folder):
        os.makedirs(folder)

    base_name = folder + '/' + 'copy_' + str(file_count) + '_' + os.path.basename(f.name)
    new_f = open(base_name, 'w+')
    file_count += 1

    count = 0
    for line in f:
        temp = line

        if count > 20 and count % 20 == 0 and random.randint(1, 10) > 9:
            if random.randint(1, 10) < 8:
                temp += temp
            else:
                temp = temp[random.randint(0, len(temp)):random.randint(0, len(temp))]

        new_f.write(temp)
        count += 1


for i in range(30):
    read_file('birds_1', '/Users/arashsaidi/Desktop/eagles/12.jpg')