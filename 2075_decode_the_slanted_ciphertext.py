class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:

        if rows == 1:
            return encodedText

        word_by_rows = len(encodedText) // rows
        print(word_by_rows)

        matrix = [[]] * rows

        k = 0
        for i in range(rows):
            row = []
            for j in range(word_by_rows):
                row.append(encodedText[k])
                k += 1
            matrix[i] = row

        ans = ""

        for col in range(word_by_rows):
            i, j = 0, col

            while i < rows and j < word_by_rows:
                ans += matrix[i][j]
                i += 1
                j += 1

        return ans.rstrip()


print(Solution().decodeCiphertext("iveo    eed   l te   olc", 4))  # "i love leetcode"

print(Solution().decodeCiphertext(" b  ac", 2))
