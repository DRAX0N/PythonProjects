"""
1320. Minimum Distance to Type a Word Using Two Fingers
Hard
Topics
premium lock icon
Companies
Hint

You have a keyboard layout as shown above in the X-Y plane, where each English uppercase letter is located at some coordinate.

For example, the letter 'A' is located at coordinate (0, 0), the letter 'B' is located at coordinate (0, 1), the letter 'P' is located at coordinate (2, 3) and the letter 'Z' is located at coordinate (4, 1).
Given the string word, return the minimum total distance to type such string using only two fingers.

The distance between coordinates (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|.

Note that the initial positions of your two fingers are considered free so do not count towards your total distance, also your two fingers do not have to start at the first letter or the first two letters.

 

Example 1:

Input: word = "CAKE"
Output: 3
Explanation: Using two fingers, one optimal way to type "CAKE" is: 
Finger 1 on letter 'C' -> cost = 0 
Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2 
Finger 2 on letter 'K' -> cost = 0 
Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1 
Total distance = 3
Example 2:

Input: word = "HAPPY"
Output: 6
Explanation: Using two fingers, one optimal way to type "HAPPY" is:
Finger 1 on letter 'H' -> cost = 0
Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
Finger 2 on letter 'P' -> cost = 0
Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
Total distance = 6
 

Constraints:

2 <= word.length <= 300
word consists of uppercase English letters.
"""
letter_table = [["A", "B", "C", "D", "E", "F"],
                ["G", "H", "I", "J", "K", "L"],
                ["M", "N", "O", "P", "Q", "R"],
                ["S", "T", "U", "V", "W", "X"],
                ["Y", "Z"]]
class Solution:
    def minimumDistance(self, word: str) -> int:

        # ------------------------------------------
        # FUNKCJA ODLEGŁOŚCI
        # ------------------------------------------
        def dist(a, b):
            # Jeśli któryś palec nie ma jeszcze pozycji (26),
            # pierwsze przyłożenie jest DARMOWE → koszt 0
            if a == 26 or b == 26:
                return 0
            # Manhattan distance na siatce 6 kolumn
            # a // 6 = wiersz, a % 6 = kolumna
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        # ------------------------------------------
        # INICJALIZACJA DP
        # ------------------------------------------
        INF = float('inf')

        # dp[f1][f2] = minimalny łączny koszt do tej pory
        # f1, f2 ∈ 0-25 (litera) lub 26 (nie użyty jeszcze)
        # Rozmiar: 27×27
        dp = [[INF] * 27 for _ in range(27)]

        # Stan startowy: oba palce bez pozycji, koszt = 0
        dp[26][26] = 0

        # ------------------------------------------
        # ITERACJA PO LITERACH
        # ------------------------------------------
        for ch in word:
            # Zamień literę na indeks 0-25
            c = ord(ch) - ord('A')

            # Nowa tabela DP po wpisaniu tej litery
            # Zerujemy - wszystkie nowe stany zaczynają od INF
            new_dp = [[INF] * 27 for _ in range(27)]

            for f1 in range(27):
                for f2 in range(27):
                    # Pomiń nieosiągalne stany
                    if dp[f1][f2] == INF:
                        continue
                    cost = dp[f1][f2]

                    # OPCJA 1: Palec 1 przesuwa się do c, palec 2 stoi
                    d = dist(f1, c)
                    # Po ruchu: f1 jest teraz na c, f2 bez zmian
                    if cost + d < new_dp[c][f2]:
                        new_dp[c][f2] = cost + d

                    # OPCJA 2: Palec 2 przesuwa się do c, palec 1 stoi
                    d = dist(f2, c)
                    # Po ruchu: f1 bez zmian, f2 jest teraz na c
                    if cost + d < new_dp[f1][c]:
                        new_dp[f1][c] = cost + d

            # Zaktualizuj dp dla następnej litery
            dp = new_dp

        # ------------------------------------------
        # WYNIK
        # ------------------------------------------
        # Znajdź minimalny koszt spośród wszystkich
        # końcowych ustawień palców
        return min(
            dp[f1][f2]
            for f1 in range(27)
            for f2 in range(27)
            if dp[f1][f2] < INF
        )
    
        
if __name__ == "__main__":
    s = Solution()
    print(s.minimumDistance("CAKE")) # 3
    print(s.minimumDistance("HAPPY")) # 6