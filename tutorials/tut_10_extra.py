def open_file(filename):
    """
    Opens the filename and returns the file object.
    """
    try:
        f_obj = open(filename, "r")
        return f_obj
    except OSError as err:
        print("Could not open " + filename + ", try again")
        print(err)
        return None

def read_header(f_obj):
    """
    Reads the header from the file object and returns it as a list.
    """
    f_obj.seek(0)
    header = f_obj.readline().strip().split(',')
    return header

def read_body(f_obj):
    """
    Reads the body from the file object and returns it as a list.
    """
    f_obj.seek(0)
    next(f_obj)
    body = []
    for line in f_obj:
        line = line.strip().split(',')
        body.append(line)
    return body

def find_largest_percent_change(body):
    """
    Returns the largest percent change in the CPI data.
    """
    largest = 0
    for line in body:
        try:
            percent_change = float(line[-1])
            if percent_change > largest:
                largest = percent_change
        except ValueError:
            pass
    return largest

def main():
    f_obj = open_file("cpi-alberta.csv")
    if f_obj is None:
        return
    
    header = read_header(f_obj)
    print(header)
    
    body = read_body(f_obj)
    f_obj.close()

    largest_percent_change = find_largest_percent_change(body)
    print(f'The largest percent change is {largest_percent_change}%')

if __name__ == "__main__":
    main()