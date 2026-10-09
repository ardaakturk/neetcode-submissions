from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        seen_in_row: dict[int, set] = defaultdict(set)
        seen_in_col: dict[int, set] = defaultdict(set)
        seen_in_box: dict[tuple, set] = defaultdict(set)

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if num in seen_in_row[i]:
                    print("Found duplicate in the same row")
                    return False
                if num in seen_in_col[j]:
                    print("Found duplicate in the same col")
                    return False
                if num in seen_in_box[(i // 3, j // 3)]:
                    print("Found duplicate in the same sub-box")
                    return False

                seen_in_row[i].add(num)
                seen_in_col[j].add(num)
                seen_in_box[(i // 3, j // 3)].add(num)

        return True