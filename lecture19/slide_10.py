f_obj = open('lecture19/word_list.txt', 'r') 
for iteration in range(3):
    f_obj.seek(0)
    more_contents = f_obj.read()
    print('Iteration', iteration)
    print(more_contents)
f_obj.close()