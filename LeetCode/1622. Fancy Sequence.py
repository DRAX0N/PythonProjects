"""
1622. Fancy Sequence
Hard
Topics
premium lock icon
Companies
Hint
Write an API that generates fancy sequences using the append, addAll, and multAll operations.

Implement the Fancy class:

Fancy() Initializes the object with an empty sequence.
void append(val) Appends an integer val to the end of the sequence.
void addAll(inc) Increments all existing values in the sequence by an integer inc.
void multAll(m) Multiplies all existing values in the sequence by an integer m.
int getIndex(idx) Gets the current value at index idx (0-indexed) of the sequence modulo 109 + 7. If the index is greater or equal than the length of the sequence, return -1.
 

Example 1:

Input
["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
Output
[null, null, null, null, null, 10, null, null, null, 26, 34, 20]

Explanation
Fancy fancy = new Fancy();
fancy.append(2);   // fancy sequence: [2]
fancy.addAll(3);   // fancy sequence: [2+3] -> [5]
fancy.append(7);   // fancy sequence: [5, 7]
fancy.multAll(2);  // fancy sequence: [5*2, 7*2] -> [10, 14]
fancy.getIndex(0); // return 10
fancy.addAll(3);   // fancy sequence: [10+3, 14+3] -> [13, 17]
fancy.append(10);  // fancy sequence: [13, 17, 10]
fancy.multAll(2);  // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
fancy.getIndex(0); // return 26
fancy.getIndex(1); // return 34
fancy.getIndex(2); // return 20
 

Constraints:

1 <= val, inc, m <= 100
0 <= idx <= 105
At most 105 calls total will be made to append, addAll, multAll, and getIndex.

"""

class Fancy:

    def __init__(self):
        self.sequence = []
        self.length = 0

    def append(self, val: int) -> None:
        self.sequence.append(val)
        self.length = len(self.sequence)

    def addAll(self, inc: int) -> None:
        for i in range(self.length):
            self.sequence[i] += inc

    def multAll(self, m: int) -> None:
        for i in range(self.length):
            self.sequence[i] *= m  

    def getIndex(self, idx: int) -> int:
        MODULO = 10**9 + 7
        if idx >= self.length:
            return -1
        else:
            return self.sequence[idx] % MODULO
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
class Fancy:

    def __init__(self):
        self.sequence = []
        self.length = 0
        self.action = []

    def append(self, val: int) -> None:
        self.sequence.append(val)
        self.length = len(self.sequence)

    def addAll(self, inc: int) -> None:
        last_index = self.length - 1
        self.action.append([0,inc,last_index])

    def multAll(self, m: int) -> None:
        last_index = self.length - 1
        self.action.append([1,m,last_index])

    def getIndex(self, idx: int) -> int:
        MODULO = 10**9 + 7
        if idx >= self.length:
            return -1
        else:
            res = self.sequence[idx]
            for action in self.action:
                if action[0] == 0 and idx<=action[2]:
                    res += action[1]
                elif action[0] == 1 and idx<=action[2]:
                    res *= action[1]
            return res % MODULO
        
class Fancy:

    def __init__(self):
        self.sequence = []
        self.length = 0
        self.action = []

    def append(self, val: int) -> None:
        self.sequence.append(val)
        self.length = len(self.sequence)

    def addAll(self, inc: int) -> None:
        last_index = self.length - 1
        self.action.append([0,inc,last_index])

    def multAll(self, m: int) -> None:
        last_index = self.length - 1
        self.action.append([1,m,last_index])

    def getIndex(self, idx: int) -> int:
        MODULO = 10**9 + 7
        if idx >= self.length:
            return -1
        else:
            res = self.sequence[idx]
            for action in self.action:
                if action[0] == 0 and idx<=action[2]:
                    res += action[1]
                elif action[0] == 1 and idx<=action[2]:
                    res *= action[1]
            return res % MODULO
        
class Fancy:
    MOD = 10**9 + 7

    def __init__(self):
        self.sequence = []
        self.mul = 1
        self.add = 0

    def append(self, val: int) -> None:
        inv_mul = pow(self.mul, self.MOD - 2, self.MOD)
        base_val = (val - self.add) % self.MOD
        base_val = (base_val * inv_mul) % self.MOD
        self.sequence.append(base_val)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.sequence):
            return -1
        return (self.sequence[idx] * self.mul + self.add) % self.MOD



MOD = 10**9 + 7

class Fancy:

    def __init__(self):
        self.arr = []
        self.add = 0
        self.mul = 1

    def append(self, val: int) -> None:
        res = ((val - self.add) * pow(self.mul, -1, MOD)) % MOD
        self.arr.append(res)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % MOD
        self.add = (self.add * m) % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr): return -1
        return (self.arr[idx] * self.mul + self.add) % MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx) 
if __name__ == "__main__":
    fancy = Fancy()
    fancy.append(2)   # fancy sequence: [2]
    fancy.addAll(3)   # fancy sequence: [2+3] -> [5]
    fancy.append(7)   # fancy sequence: [5, 7]
    fancy.multAll(2)  # fancy sequence: [5*2, 7*2] -> [10, 14]
    print(fancy.getIndex(0)) # return 10
    fancy.addAll(3)   # fancy sequence: [10+3, 14+3] -> [13, 17]
    fancy.append(10)  # fancy sequence: [13, 17, 10]
    fancy.multAll(2)  # fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
    print(fancy.getIndex(0)) # return 26
    print(fancy.getIndex(1)) # return 34
    print(fancy.getIndex(2)) # return 20