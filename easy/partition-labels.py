from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # get the last characters of each
        last_index_chars = { char: index for index, char in enumerate(S)}
        anchor, last = 0, 0
        partitions = []
        for index, char in enumerate(S):
            last = max(last, last_index_chars[char])
            if index == last:
                partitions.append(index - anchor + 1)
                anchor = index + 1

        return partitions


if __name__ == "__main__":
    sol = Solution()
    print(sol.partitionLabels("ababcbacadefegdehijhklij"))
    # print(sol.partitionLabels("abcadefdgh"))


