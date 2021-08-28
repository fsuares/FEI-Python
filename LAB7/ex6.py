def test_prime(a):
    primo = True
    for i in range(2, num):
        if i < num and primo == True:
            if num % i == 0:
                primo = False
                i = i + 1

            else:
                i = i + 1

    if primo == False:
        return False

    elif primo == True:
        return True

def main():
    a = int(input())
    test_prime(a)

main()