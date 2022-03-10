

def de_morgans(course_code, prof_name, time_slot):    
    if not course_code and not prof_name and not time_slot:
        print('Must contain a search parameter')
        return

    if not (course_code or prof_name or time_slot):
        print('Must contain a search parameter')
        return

    print(f'Searching with {[course_code, prof_name, time_slot]}')
    
if __name__ == '__main__':
    de_morgans('','','')
    de_morgans('COMP1501','','')

    