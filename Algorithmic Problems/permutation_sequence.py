class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorial(n):
            fac = 1
            for i in range(1, n+1):
                fac *= i
            return fac

        count = 0
        stack = []
        stack.extend([str(i) for i in range(n, 0, -1)])
        while stack:
            curr_perm = stack.pop()
            if len(curr_perm) == n:
                count += 1
            else:
                val = factorial(n - len(curr_perm))
                if (val + count) < k:
                    count += val
                else:
                    stack.extend([curr_perm + str(i)
                                  for i in range(n, 0, -1) if str(i) not in curr_perm])
            if count == k:
                return curr_perm
