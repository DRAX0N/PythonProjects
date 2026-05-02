def minion_game(string):
    # your code goes here
    text = string.lower()
    consonants = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")
    vowels = ("a", "e", "i", "o", "u")
    kevin_score = 0
    stuart_score = 0

    for n in range(0, len(text)):
        if text[n] in consonants:
            stuart_score += len(text[n::])
        elif text[n] in vowels:
            kevin_score += len(text[n::])
    
    if kevin_score > stuart_score:
        print("Kevin " + str(kevin_score))
    elif stuart_score > kevin_score:
        print("Stuart " + str(stuart_score))
    else:
        print("Draw")

    ## your code goes here
    #text = string.lower()
    #vowels = "aeiou"
    #kevin_score = 0
    #stuart_score = 0
#
    #for n in range(len(text)):
    #    if text[n] in vowels:
    #        kevin_score += len(text) - n
    #    else:
    #        stuart_score += len(text) - n
    #
    #if kevin_score > stuart_score:
    #    print(f"Kevin {kevin_score}")
    #elif stuart_score > kevin_score:
    #    print(f"Stuart {stuart_score}")
    #else:
    #    print("Draw")
    

if __name__ == '__main__':
    #s = input()
    s = 'BANANA'
    minion_game(s)