def door_print(N,M):
    i = 1
    j = 1
    dash = '-'
    pattern = '.|.'
    welcome = 'WELCOME'
    while j < N+1:
        if j == (N//2)+1:
            print(dash*((M-len(welcome))//2) + welcome + dash*((M-len(welcome))//2))
        elif j > (N//2)+1:
            print(dash*((M - (len(pattern)*(2*N-i)))//2) + pattern*(2*N-i) + dash*((M - (len(pattern)*(2*N-i)))//2))
        else:
            print(dash*((M - (len(pattern)*i))//2) + pattern*i + dash*((M - (len(pattern)*i))//2))
        i += 2
        j += 1


if __name__ == '__main__':
    N, M = 9, 27
    door_print(N, M)
