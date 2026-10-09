class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        n = len(board)

        # Check each row first - O(n^2)
        for row in board: # O(n)
            seen_nums_in_row = set()
            for num in row: # O(n)
                if num == ".":
                    continue
                if num in seen_nums_in_row: # O(1)
                    print("Row check failed!")
                    return False
                seen_nums_in_row.add(num) # O(1)

        print("Row check passed!")


        # Check each column - O(n^2)
        for i in range(n):
            seen_nums_in_col = set()
            for j in range(n):
                num = board[j][i]
                if num == ".":
                    continue
                if num in seen_nums_in_col:
                    print("Column check failed!")
                    return False
                seen_nums_in_col.add(num)
                print(seen_nums_in_col)

        print("Column check passed!")

        # Check 3x3 sub-boxes - O(n^2)
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                seen_nums_in_subbox = set()
                # i and j are at the top-left corner of the sub-box.
                for m in range(3):
                    for n in range(3):
                        num = board[i+m][j+n]
                        if num == ".":
                            continue
                        if num in seen_nums_in_subbox:
                            print("Sub-box check failed!")
                            return False
                        seen_nums_in_subbox.add(num)
        print("Sub-box check passed!")

        return True