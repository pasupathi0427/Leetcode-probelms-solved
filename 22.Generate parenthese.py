class Solution:
    def generateParenthesis(self, n: int) :
        #using recursion
        def generateValidParenthesis(list1,start,o,close):
            list2=[]
            if ( start==2*n):
                list2.append("".join(list1))
                return list2
                
            if (o< n):
                list1[start]="("
                list2.extend(generateValidParenthesis(list1,start+1,o+1,close))
                
            if (close < o):
                list1[start]=")"
                list2.extend(generateValidParenthesis(list1,start+1,o,close+1))
                
            return list2
                
        return generateValidParenthesis(['']*(2*n),0,0,0)
            
            
            
        