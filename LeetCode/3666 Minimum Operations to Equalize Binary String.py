"""
3666. Minimum Operations to Equalize Binary String
Hard
Topics
premium lock icon
Companies
Hint
You are given a binary string s, and an integer k.

In one operation, you must choose exactly k different indices and flip each '0' to '1' and each '1' to '0'.

Return the minimum number of operations required to make all characters in the string equal to '1'. If it is not possible, return -1.

 

Example 1:

Input: s = "110", k = 1

Output: 1

Explanation:

There is one '0' in s.
Since k = 1, we can flip it directly in one operation.
Example 2:

Input: s = "0101", k = 3

Output: 2

Explanation:

One optimal set of operations choosing k = 3 indices in each operation is:

Operation 1: Flip indices [0, 1, 3]. s changes from "0101" to "1000".
Operation 2: Flip indices [1, 2, 3]. s changes from "1000" to "1111".
Thus, the minimum number of operations is 2.

Example 3:

Input: s = "101", k = 2

Output: -1

Explanation:

Since k = 2 and s has only one '0', it is impossible to flip exactly k indices to make all '1'. Hence, the answer is -1.

 

Constraints:

1 <= s.length <= 10​​​​​​​5
s[i] is either '0' or '1'.
1 <= k <= s.length
"""

#class Solution:
#    def minOperations(self, s: str, k: int) -> int:
#        #print(s)
#        counter = 0
#        old_z = zero_count = s.count("0")
#        one_count = s.count("1")
#
#        if zero_count % k == 0:
#            return zero_count//k
#
#        if one_count == len(s):
#            return 0
#        
#        if k == len(s):
#            return -1
#
#        while one_count != len(s):
#            print("==========================================================")
#            #print("zero: " + str(zero_count) + " | " + "one: " + str(one_count))
#            print("old_zero: " + str(old_z))
#            #if one_count > zero_count:
#            #     zero_count -= k
#            curr_z = zero_count
#            curr_o = one_count
#            op = [0, 0, 0, 0, 0, 0]
#            for i in range(k):
#                print("///////")
#                print("zero: " + str(zero_count) + " | " + "one: " + str(one_count))
#                if one_count == zero_count and op[0] < curr_o:
#                    print("OP 1")
#                    op[0] += 1
#                    zero_count += 1
#                    one_count -= 1
#                elif one_count == zero_count and op[1] < curr_z:
#                    print("OP 2")
#                    op[1] += 1
#                    zero_count -= 1
#                    one_count += 1
#                elif one_count > zero_count and one_count > 0 and op[2] < curr_o:
#                    print("OP 3")
#                    op[2] += 1
#                    zero_count += 1
#                    one_count -= 1
#                elif one_count < zero_count and zero_count > 0 and op[3] < curr_z:
#                    print("OP 4")
#                    op[3] += 1
#                    zero_count -= 1
#                    one_count += 1
#                elif one_count > 0 and zero_count == 0 and op[4] < curr_o:
#                    print("OP 5")
#                    op[4] += 1
#                    zero_count += 1
#                    one_count -= 1
#                elif zero_count > 0 and one_count == 0 and op[5] < curr_z:
#                    print("OP 6")
#                    op[5] += 1
#                    zero_count -= 1
#                    one_count += 1
#                else:
#                    print("DUPA")
#
#            print("zero: " + str(zero_count) + " | " + "one: " + str(one_count))
#            counter += 1
#
#            if s.count("1") == len(s):
#                return counter
#  
#            if k==zero_count:
#                counter += 1
#                return counter 
#                 
#            if old_z == zero_count:
#                return -1
#            
#            old_z = zero_count
#

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count('0')
        if z == 0:
            return 0

        if k == n:
            return 1 if z == n else -1

        # If k is even, parity of zeros can't change -> must start with even zeros to reach 0
        if (k % 2 == 0) and (z % 2 == 1):
            return -1

        o = n - z

        def ok(t: int) -> bool:
            total = t * k
            # parity condition: total ≡ z (mod 2)
            if (total & 1) != (z & 1):
                return False

            oddMax = t if (t & 1) else (t - 1)      # largest odd <= t
            evenMax = (t - 1) if (t & 1) else t     # largest even <= t
            if oddMax < 1:
                return False

            L = max(z, total - o * evenMax)
            R = min(z * oddMax, total)
            if L > R:
                return False

            # need F0 parity == z parity
            if (L & 1) != (z & 1):
                L += 1
            return L <= R

        # lower bound ceil(z/k)
        t = (z + k - 1) // k
        if t < 1:
            t = 1

        upper = 2 * n + 5

        if k % 2 == 1:
            # need t parity == z parity
            if (t & 1) != (z & 1):
                t += 1
            while t <= upper:
                if ok(t):
                    return t
                t += 2
        else:
            while t <= upper:
                if ok(t):
                    return t
                t += 1

        return -1
            

if __name__ == '__main__':
    s = "110"   # output: 1
    k = 1

    #s = "0101"  # output: 2
    #k = 3

    #s = "101"   # output: -1
    #k = 2

    s == "000"
    k = 2
    
    #s = "0000"
    #k = 3

    s = "11010"
    k = 4

    new = Solution()
    print(new.minOperations(s,k))