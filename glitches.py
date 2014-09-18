from read_file import read_file
import random
import os


def delete_files_in_folder(path="test_folder"):
    folder = path
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception, e:
            print e


def glitch_1(output_path="test_folder"):
    files = read_file(output_path, "/Users/arashsaidi/Desktop/eagles/1.jpg", True)
    f = files[0]
    new_f = files[1]

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


def glitch_2(output_path="test_folder"):
    files = read_file(output_path, "/Users/arashsaidi/Documents/pictures/jesuses/1.jpg", True)
    f = files[0]
    new_f = files[1]

    count = 0
    p_line = ""

    for line in f:
        temp = line

        if count > 5 and random.randint(0, 10) > 9:
            if random.randint(0, 10) > 8:
                temp *= 3
            elif len(temp) > random.randint(0, len(temp)):
                temp += temp
            else:
                temp += p_line

        new_f.write(temp)
        count += 1

        p_line = line * random.randint(0, 10)


def run():
    delete_files_in_folder()
    for i in range(20):
        glitch_2()


run()