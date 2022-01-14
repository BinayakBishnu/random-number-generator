def find_largest_prime(top):
    for i in range(top, 1, -1):
        flag = 1
        print(i)
        F = [x for x in range(2, (i//2)+1)]
        print('F ', F)

        for j in F:
            if i % j == 0:
                print('Not prime')
                flag = 0
                break

        if flag == 1:
            print('Prime')
            return i

    return 1


def generate_rand(lower_limit=0, upper_limit=0):
    if upper_limit <= lower_limit:
        print("lower limit must be >= lower limit")
        return

    L = [i for i in range(lower_limit+1, upper_limit)]

    p = find_largest_prime(upper_limit-1)

    print(p)

    number1 = (((upper_limit-1)+(lower_limit+1))//2) % (upper_limit-1)

    print(number1)

    number2 = p - ((((upper_limit-1)+(lower_limit+1))//2) % p)

    print(number2)


if __name__ == '__main__':
    print('generate file')
    generate_rand(4, 16)

else:
    generate_rand(4, 16)
