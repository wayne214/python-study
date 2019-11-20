from typing import List

# 格雷码
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        for i in range(1 << n):
            res.append((i >> 1)^ i)
        return res

obj = Solution()
print(obj.grayCode(3))