from copy import deepcopy
tf=[]
tmp=[]

#x=deepcopy(n)
ans=[]
class Solution:
    def chk(r,c,n):
        global tmp 
        for i in range(n):
                if(tmp[i][c]=='Q'):
                        return False
        for i in range(n):
                if(tmp[r][i]=='Q'):
                        return False
        i=r
        j=c
        while(i>=0 and j>=0):
                if(tmp[i][j]=='Q'):
                        return False
                i-=1
                j-=1
        i=r
        j=c
        while(i>=0 and j<n):
                if(tmp[i][j]=='Q'):
                        return False
                i-=1
                j+=1
        return True
    def f(x,r,n):
        global tmp
        global ans 
        if(x==0):
                t=deepcopy(tmp)
                ans.append(t)
                return
        for i in range(n):
                if(Solution.chk(r,i,n)):
                        tmp[r][i]='Q'
                        Solution.f(x-1,r+1,n)
                        tmp[r][i]='.'
        return
    def solveNQueens(n):
        global tmp
        global tf
        global ans
        for i in range(n):
            for j in range(n):
                tf.append('.')
            tmp.append(tf)
            tf=[]
        Solution.f(n,0,n)
        k=[]
        s=[]
        t=''
        for i in ans: 
            for j in i:
                for m in j:
                    t=t+m
                s.append(t)
                t=''    
            k.append(s)
            s=[]
        return k
print(Solution.solveNQueens(12))
