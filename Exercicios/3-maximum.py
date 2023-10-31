# 321. CREATE MAXIMUM NUMBER - HARD
# https://leetcode.com/problems/create-maximum-number/

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        # Função para obter o número máximo de 'k' dígitos de uma lista 'nums'
        def getMaxSingle(nums, k):
            # pilha para rastrear os dígitos selecionados 
            stack = []

            # Número de dígitos a serem removidos para obter 'k' dígitos 
            to_pop = len(nums) - k  
            for num in nums:
                while to_pop > 0 and stack and num > stack[-1]:
                    stack.pop()
                    to_pop -= 1
                stack.append(num)  # Adiciona o dígito atual à pilha
            return stack[:k]  # Retorna os 'k' dígitos selecionados

        # mescla duas listas mantendo a ordem relativa
        def merge(arr1, arr2):
            res = []  
            while arr1 or arr2:
                if arr1 > arr2:
                    res.append(arr1[0])  
                    arr1 = arr1[1:] 
                else:
                    res.append(arr2[0])  
                    arr2 = arr2[1:]  
            return res 
        
        result = []  
       
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            max1 = getMaxSingle(nums1, i)  # maiores digitos de nums1
            max2 = getMaxSingle(nums2, k - i)  # maiores digitos nums2
            combined = merge(max1, max2)  
            result = max(result, combined) 

        return result 

# # Example usage:
# solution = Solution()

# # Example 1
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# print(solution.maxNumber(nums1, nums2, k))  # Output: [9, 8, 6, 5, 3]

# # Example 2
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# print(solution.maxNumber(nums1, nums2, k))  # Output: [6, 7, 6, 0, 4]
