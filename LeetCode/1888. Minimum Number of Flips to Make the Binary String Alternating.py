"""
1888. Minimum Number of Flips to Make the Binary String Alternating
Medium
Topics
premium lock icon
Companies
Hint
You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
 

Example 1:

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating.
Example 3:

Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
"""

    
#Bruteforce
#class Solution:
#    def minFlips(self, s: str) -> int:
#        min_all = []
#
#        s_len = len(s)
#        if s_len == 1:
#            return 0
#
#        #s preparation   
#        i = 0     
#        while i < s_len:
#            i+=1 
#            #if s[-1] == "0":
#            #    s = s[-1]+s[:-1] 
#       
#            #if s[0] != s[-1]:
#            #    s = s[1:]+s[0]
#            
#            s = s[1:]+s[0]
#            mina = 0  #"01"
#            minb = 0  #"10"
#            for n in range(s_len):
#                #A
#                if (n%2 == 1 and s[n] == "1") or (n%2 == 0 and s[n] == "0"):
#                    pass
#                else:
#                    mina += 1
#                #B
#                if ((n+1)%2 == 1 and s[n] == "1") or ((n+1)%2 == 0 and s[n] == "0"):
#                    pass
#                else:
#                    minb += 1
#            min_all.append(mina)
#            min_all.append(minb)
#
#        return min(min_all)
    
#optimal
class Solution:
    def minFlips(self, s: str) -> int:
        mina = []  #"01"
        minb = [] #"10"
        s_len_org = len(s)
        print(s_len_org)
        s = s + s #adding all possible slides for type 1 operation
        s_len = len(s)

        difa = [0]*s_len
        difb = [0]*s_len
        for n in range(s_len):
            #A
            if (n%2 == 1 and s[n] == "1") or (n%2 == 0 and s[n] == "0"):
                pass
            else:
                difa[n] = 1
            #B
            if ((n+1)%2 == 1 and s[n] == "1") or ((n+1)%2 == 0 and s[n] == "0"):
                pass
            else:
                difb[n] = 1
        print(difa)
        print(difb)
        r = s_len_org
        for l in range(s_len_org):
            print(difb[l:r])
            mina.append(sum(difa[l:r]))
            minb.append(sum(difb[l:r]))
            r +=1
        print(mina)
        print(minb)


        return min(min(mina),min(minb))
class Solution:
    def minFlips(self, s: str) -> int:
        minall = []  #"01" #"10"
        #minb = [] 
        s_len_org = len(s)
        s = s + s #adding all possible slides for type 1 operation
        s_len = len(s)
        if s[0] == "0":
            difa = [0]*s_len
        else:
            difb = [0]*s_len
        for n in range(s_len):
            if s[0] == "0":
                #A
                if (n%2 == 1 and s[n] == "1") or (n%2 == 0 and s[n] == "0"):
                    pass
                else:
                    difa[n] = 1
            else:
                #B
                if ((n+1)%2 == 1 and s[n] == "1") or ((n+1)%2 == 0 and s[n] == "0"):
                    pass
                else:
                    difb[n] = 1
        #print(difa)
        #print(difb)
        r = s_len_org
        for l in range(s_len_org):
            if s[0] == "0":
                minall.append(sum(difa[l:r]))
            else:
                minall.append(sum(difb[l:r]))
                
            r +=1
        #print(minall)
        return min(minall)
    
class Solution:
    def minFlips(self, s: str) -> int:
        minall = []  #"01" #"10"
        #minb = [] 
        s_len_org = len(s)
        s = s + s #adding all possible slides for type 1 operation
        s_len = len(s)

        difa = [0]*s_len
        difb = [0]*s_len

        for n in range(s_len):
            #A
            if (n%2 == 1 and s[n] == "1") or (n%2 == 0 and s[n] == "0"):
                pass
            else:
                difa[n] = 1
            #B
            if ((n+1)%2 == 1 and s[n] == "1") or ((n+1)%2 == 0 and s[n] == "0"):
                pass
            else:
                difb[n] = 1
        
        #print([int(x) for x in s])
        #print("")
        print(difa)
        print(difb)
        l = 0
        r = 0
        temp_suma = 0
        temp_sumb = 0
        #print(r)
        while l<s_len_org:
        #for l in range(s_len_org):
            
            temp_suma += difa[r]
            temp_sumb += difb[r]
            if r>=s_len_org:
                temp_suma -= difa[l]
                temp_sumb -= difb[l]
                l += 1
            if r>=s_len_org-1:
                minall.append(temp_suma)
                minall.append(temp_sumb)  

            r += 1

        return min(minall)
    
if __name__ == '__main__':
    s = "010"
    #s = "111000" #2
    #s = "010" #0
    #s = "1110" #1
    #s = "01001001101" #2
    s = "01000110010100000" #5
    #s = "01001001101"
    new = Solution()
    print(new.minFlips(s))