def jump(nums):
        n =len(nums)-1
        # i = -1
        # jumps = 0
        # while i < n and n>1:
        #     if nums[i] == 0:
        #         i+=1
        #     if (nums[i] + i) < n:
        #         i+=nums[i]
        #         jumps+=1
        #     else:
        #         i+=1
        # return jumps
        l=r=0
        jump =0
        while r<n:
            farthest = 0
            for i in range(l,r+1):
                farhtest = max(farthest,i + nums[i])
            l = r+1
            r = farthest
            jump +=1
        return jump
nums = [2,3,0,1,4]
print(jump(nums))