def read_elements():
    try:
        f_obj = open('lecture19/elements.txt', 'r')
        result = []
        for line in f_obj:
            result.append(line.split())
        f_obj.close()
        return result
    except OSError as e:
        print(e)

print(read_elements())