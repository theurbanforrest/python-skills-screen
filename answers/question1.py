def question_1(my_arr):
    counter = 0
    for x in my_arr:

        # confirm type int, else error
        if not type(x) is int:
            raise TypeError("Error - only ints allowed")

        # convert to str, check length.  If even (i.e. divide by 2, remainder is 0) then counter += 1, else next
        int_as_str = str(x)
        length = len(int_as_str)
        if(length % 2) == 0:
            counter += 1

    # print user-friendly result + return output
    print("Number of ints in your array w/ an even number of digits: " + str(counter))
    return counter