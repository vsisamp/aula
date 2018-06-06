def primo(n):
    for k in range(2, int(n/2)):
        if n % k == 0:
            return False
    return True

n = primo(int(input('coloque o valor ')))


main()