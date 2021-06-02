from typing import List


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        dim = len(A)

        def shift_and_count(x_shift, y_shift, mat, ref):
            overlap = 0
            for ref_row, mat_row in enumerate(range(y_shift, dim)):
                for ref_col, mat_col in enumerate(range(x_shift, dim)):
                    if mat[mat_row][mat_col] == 1 and mat[mat_row][mat_col] == ref[ref_row][ref_col]:
                        overlap += 1
            return overlap

        max_overlap = 0

        for y_shift in range(0, dim):
            for x_shift in range(0, dim):
                max_overlap = max(max_overlap, shift_and_count(x_shift, y_shift, A, B))
                max_overlap = max(max_overlap, shift_and_count(x_shift, y_shift, B, A))

        return max_overlap



