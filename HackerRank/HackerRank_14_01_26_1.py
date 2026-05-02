def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    sub_s = []
    solution = []
    for i in range(0, n, k):
        sub_s.append(string[i:i+k])

    for word in sub_s:
        mylist = list(set(word))
        result = {}
        anwser = ""
        for l in mylist:
          for n in range(len(word)):
              if l == word[n]:
                  result[l] = n
                  break      
        final = sorted(result.items(), key=lambda x: x[1])
        for key, value in final:
            anwser += key
        solution.append(anwser)
    for word in solution:
        print(word)

if __name__ == '__main__':
    #string, k = input(), int(input())
    string, k = 'AABCAAADA',3
    merge_the_tools(string, k)
