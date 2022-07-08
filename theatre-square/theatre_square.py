def theatre_square(n, m,a):
   
    square = n * m
    one_flagstone = a * a
    check_n=-1
    check_m= -1
    count = 0

    if square% one_flagstone == 0:
        return square/ one_flagstone
    else:
        while check_n != 0:
            if n == a:
                check_n = 0
            elif n- a >0:
                n =n- a
                count += 1
            else:
                count += 1
                check_n = 0
        while check_m != 0:
            if m ==a:
                check_m = 0
            elif m- a >0:
                m =m- a
                count += 1
            else:
                count += 1
                check_m =0

        return count