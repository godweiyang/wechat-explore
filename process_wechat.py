import sys


def main(input_filename):
    fin = open(input_filename, "r", encoding='utf8')
    fout = open("__" + input_filename, "w", encoding='utf8')

    for line in fin.readlines():
        if len(line) > 0:
            if line[0] == '<' or line[0] == '\"' or line[0] == "	":
                pass
            else:
                fout.write(line)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('[usage] <input>')