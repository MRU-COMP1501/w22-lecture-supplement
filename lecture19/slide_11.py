def get_longest_line(f_obj):
    f_obj.seek(0)
    longest_line = ""
    for line in f_obj:
        if len(line) > len(longest_line):
            longest_line = line
    return longest_line

def open_file():
    try:
        f_obj = open('lecture19/word_list.txt', 'r') 
        return f_obj
    except OSError:
        print('Sorry, could not open that file')
        return None

f_obj = open_file()
if f_obj is not None:
    line = f_obj.readline()
    while line != '':
        print(line[0])
        line = f_obj.readline()

    print('Longest line')
    print(get_longest_line(f_obj))
    f_obj.close()