class solution:
    def twosum(self,nums:list[int],target:int)->list[int]:
        dict={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in dict:
                return [dict[complement],i]
            dict[num]=i
        return[]
