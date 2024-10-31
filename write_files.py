# Write files

def new_ways():
    with open('wasteland.txt', mode='wt', encoding='utf-8') as fout:
        # print(type(fout))
        fout.write('When are we going to win?\n')
        fout.write('Tomorrow?\n')
        fout.write('okay\n')

    # Open the file to read it
    with open('wasteland.txt', mode='rt', encoding='utf-8') as fin:
        for line in fin:
            print(line)


def old_ways():
    fout = open('wasteland.txt', mode='wt', encoding='utf-8')
    # print(type(fout))
    fout.write('When are we going to win?\n')
    fout.write('Tomorrow?\n')
    fout.write('okay\n')
    fout.close()  # DO NOT FORGET THIS LINE
    # Open the file to read it
    fin = open('wasteland.txt', mode='rt', encoding='utf-8')
    for line in fin:
        print(line)
    fin.close()  # DO NOT FORGET THIS LINE

# Starting Point
# Program "Driver"


def main():
    old_ways()
    new_ways()


if __name__ == '__main__':
    # Call main function
    main()
