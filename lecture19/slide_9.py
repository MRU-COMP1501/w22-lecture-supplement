f_obj = open('lecture19/word_list.txt', 'r') 
contents = f_obj.read() 
valid_words = contents.split('\n')
f_obj.close()
print(valid_words)