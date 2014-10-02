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


def rename_files(path="test"):
    num = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            my_string = str(num)
            os.rename(root + os.sep + f, root + os.sep + 'img' + my_string.zfill(4) + '.jpg')
            num += 1


def glitch_1(input_path, output_path="test_folder"):
    files = read_file(output_path, input_path, True)
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


# rename_files()

def run():
    delete_files_in_folder()
    for i in range(10):
        glitch_1('95d8a678ba88f287b7cf6a5df802fcf3_1.png')


run()
rename_files('test_folder')