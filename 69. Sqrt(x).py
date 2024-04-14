def mySqrt(self, x: int) -> int:
    low=2
    right=(x //2 )
    res=0

    if x==0 or x==1:
        return x

    while(low<=right):
        mid=low+(right-low)//2

        if mid==x //mid:
            return mid

        elif mid < x//mid:
            low = mid + 1
            

        else:
            right=mid-1

    return right

    