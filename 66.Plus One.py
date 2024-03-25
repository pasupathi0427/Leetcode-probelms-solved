def plusOne(digits):
    str_integer=""
    for i in range(len(digits)):
        str_integer+=str(digits[i])
    
    val=int(str_integer)+1

    return [int(x) for x in str(val)] 