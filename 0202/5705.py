# 
# @param nums int整型一维数组 
# @param target int整型 
# @return int整型
#
class Solution:
    def search(self , nums: List[int], target: int) -> int:
        # write code here
        l = 0 
        r = len(nums) -1 
        # 从数组首位开始，直到二者相遇
        while l <= r :
            m =  int ((l + r)/2)
            if nums[m] == target :
                return m 
            # 进入右区间，l 增大
            if nums[m] < target :  
                l = m + 1  
            else: 
                r = m - 1 

        return -1 