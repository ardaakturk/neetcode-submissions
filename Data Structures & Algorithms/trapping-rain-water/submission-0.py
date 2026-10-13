class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        max_h_left = [0] * n
        max_h_right = [0] * n

        # Find the max heights seen to the left
        curr_max = 0
        for i in range(n):
            curr_height = height[i]
            max_h_left[i] = curr_max
            curr_max = max(curr_max, curr_height)

        # Find the max heights seen to the right
        curr_max = 0
        for i in range(n-1, -1, -1):
            curr_height = height[i]
            max_h_right[i] = curr_max
            curr_max = max(curr_max, curr_height)

        # Find how much water we can trap
        trapped_water = 0
        for i, h in enumerate(height):
            if not (max_h_left[i] > h and max_h_right[i] > h):
                # Cannot trap water at this index
                continue

            trapped_water += min(max_h_left[i], max_h_right[i]) - h

        return trapped_water