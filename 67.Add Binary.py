def addBinary(self, a: str, b: str) -> str:
    a=int(a,2)  #converts binary string to decimal value
    b=int(b,2)

    c=a+b
    bin_sum=bin(c)

    return bin_sum[2:]
        