try:
    f_obj = open('lecture19/output.txt', 'w') # 'w' means open in 'write' mode
    for num in range(20):
        f_obj.write(f'line {num}\n')
        # f_obj.write(num) # runtime error
    f_obj.close()
    print('Successfully wrote output')
except Exception as e:
    print('Could not write to output')
    print(e)