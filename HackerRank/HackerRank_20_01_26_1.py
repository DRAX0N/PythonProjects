#text, n = input().split()

def get_first(text):
    new_text = sorted(text)
    return new_text[0]

def perm(text,n):
    new_text = sorted(text)
    result = []
    for letter in new_text:
        workspace = new_text
        workspace.pop(letter)
        for x in range(len(new_text)):
            for i in range(n):
                
                result.append(letter + workspace[x])


        for letter2 in workspace:
            result.append(letter + letter2)



    return result



if __name__ == '__main__':
    text, n = "HACK 2".split()
    n = int(n)
    ascii = [chr(i) for i in range(97, 123)]
    print(ascii)
    #perm(text, n)
    