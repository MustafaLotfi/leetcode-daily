class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        specific_lets = []
        specific_lets_num = []
        for let in arr:
            if let not in specific_lets:
                specific_lets.append(let)
                specific_lets_num.append(1)

            else:
                let_ind = specific_lets.index(let)
                specific_lets_num[let_ind] += 1
        
        distinct_lets = []
        for i in range(len(specific_lets_num)):
            if specific_lets_num[i] == 1:
                distinct_lets.append(specific_lets[i])

        if k > len(distinct_lets):
            return ""
        else:
            return distinct_lets[k-1]
        
