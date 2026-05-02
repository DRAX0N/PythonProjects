def print_rangoli(size):
    # your code goes here
    alphabet_tuple = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    dash = "-"
    count = 2*size - 1
    n = 0
    
    while n < count:
        letter_line = ""
        if n<count/2:
            for i in range(0, 2*n + 1):
                if i == (2*n):
                    letter_line += alphabet_tuple[size-1]
                elif i > n:
                    letter_line += alphabet_tuple[size- 1 + i - 2*n] + dash
                else:
                    letter_line += alphabet_tuple[size- 1 - i] + dash

            line = (2*size-2-2*n)*dash + letter_line + (2*size-2-2*n)*dash
            print(line)
        else:
            for i in range(0, 2*(count-n-1)+1):
                if i == (2*(count-n-1)):
                    letter_line += alphabet_tuple[size-1]
                elif i > (count-n-1):
                    letter_line += alphabet_tuple[size- 1 + i - 2*((count-n-1))] + dash

                else:
                    letter_line += alphabet_tuple[size- 1 - i] + dash

            line = (2*size-2-2*(count-n-1))*dash + letter_line + (2*size-2-2*(count - n-1))*dash
            print(line)
        n += 1

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)