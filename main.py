def main():
    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the ending letter: ')
        
        if ord(start) > ord(end) or (start.isalpha() == False or end.isalpha() == False):
            print("Input error")
            continue
        else:
            break

    """
    ########################################
    Code Your Program here
    ########################################
    """
    for i in range(ord(start), ord(end)+1):
        result.append(chr(i))

    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
