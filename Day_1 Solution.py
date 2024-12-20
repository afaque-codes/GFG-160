  // Day 1 / 160

  //https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/second-largest3735
class Solution:
    def getSecondLargest(self, numbers):
        if len(numbers) < 2:
            return -1  
        highest = second_highest = -1
        for current_number in numbers:
            if current_number > highest:
                second_highest, highest = highest, current_number
            elif current_number > second_highest and current_number < highest:
                second_highest = current_number
        return second_highest 
