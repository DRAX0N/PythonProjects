def print_formatted(number):
    # your code goes here
    for n in generator(number):
        n8 = oct(n)[2:]
        n16 = hex(n)[2:].upper()
        nBin = bin(n)[2:]
        
        print(str(n) + " " + str(n8) + " " + str(n16) + " " + str(nBin))
    
def generator(number):
    i = 1
    while i < number+1:
        yield i
        i += 1

if __name__ == '__main__':
    n = 17
    print_formatted(n)