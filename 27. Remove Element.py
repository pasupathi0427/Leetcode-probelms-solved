def removeElement( nums, val):
    index=0
    for i in range(1,len(nums)):
        if nums[i]!=val:
            nums[index]=nums[i]
            index+=1

    return index


   
