from copy import deepcopy

n=int(input('Enter the Value of N: '))
tf=[]
tmp=[]
for i in range(n):
	for j in range(n):
		tf.append('.')
	tmp.append(tf)
	tf=[]
x=deepcopy(n)
ans=[]
def p(x):	
	for i in x:
		print(i)
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
		if(chk(r,i,n)):
			tmp[r][i]='Q'
			f(x-1,r+1,n)	
			tmp[r][i]='.'
	return


f(n,0,n)
if(ans==[]):
	print('Cant Find Answer')
else:
	print(len(ans))
	for i in ans:
		p(ans)
		print('')
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
	
print(k)


