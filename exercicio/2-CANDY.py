# 135. CANDY - HARD
# https://leetcode.com/problems/candy/

class Solution(object):
    def candy(self, ratings):
            n = len(ratings)
            if n <= 1:
                return n

            # 1 bala para cada crianca
            candies = [1] * n

            for i in range(1, n):
                if ratings[i] > ratings[i - 1]:
                    candies[i] = candies[i - 1] + 1

            for i in range(n - 2, -1, -1):
                if ratings[i] > ratings[i + 1]:
                    candies[i] = max(candies[i], candies[i + 1] + 1)

            # faz a escolha local
            # nos fors considera as classificacoes dos vizinhos 
            # vai ajustando a classificacao

            return sum(candies)

# ratings = [1,2,1]
# test = Solution()
# test.candy(ratings)