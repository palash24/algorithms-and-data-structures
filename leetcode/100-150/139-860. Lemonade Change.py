# 860. Lemonade Change
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        five, ten = 0, 0
        for i in bills:
            if i == 5: five += 1
            elif i == 10 and five > 0:
                ten += 1
                five -= 1
            elif i == 20 and five > 0 and ten > 0:                
                five -= 1
                ten -= 1
            elif i == 20 and five >= 3:
                five -= 3
            else: return False

        return True