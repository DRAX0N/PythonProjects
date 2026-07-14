"""
1301. Number of Paths with Max Score
Hard
Topics
premium lock icon
Companies
Hint
You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.

You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.

In case there is no path, return [0, 0].

 

Example 1:

Input: board = ["E23","2X2","12S"]
Output: [7,1]
Example 2:

Input: board = ["E12","1X1","21S"]
Output: [4,2]
Example 3:

Input: board = ["E11","XXX","11S"]
Output: [0,0]
 

Constraints:

2 <= board.length == board[i].length <= 100
"""

class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)

        score = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]

        score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or ways[i][j] == 0:
                    continue

                for ni, nj in ((i - 1, j), (i, j - 1), (i - 1, j - 1)):
                    if ni < 0 or nj < 0 or board[ni][nj] == 'X':
                        continue

                    add = 0 if board[ni][nj] in ('E', 'S') else int(board[ni][nj])
                    new_score = score[i][j] + add

                    if new_score > score[ni][nj]:
                        score[ni][nj] = new_score
                        ways[ni][nj] = ways[i][j]
                    elif new_score == score[ni][nj]:
                        ways[ni][nj] = (ways[ni][nj] + ways[i][j]) % MOD

        if ways[0][0] == 0:
            return [0, 0]
        return [score[0][0], ways[0][0] % MOD]

if __name__ == "__main__":
    board = ["E23","2X2","12S"]
    print(Solution().pathsWithMaxScore(board))  # Output: [7, 1]
    board = ["E12","1X1","21S"]
    print(Solution().pathsWithMaxScore(board))  # Output: [4,2]
    board = ["E11","XXX","11S"]
print(Solution().pathsWithMaxScore(board))  # Output: [0, 0]