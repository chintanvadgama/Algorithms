# longest common subsequence between two strings
# ABCDGH and 'AEDFHR' => ADH
# Formula => If last chars are same 1+ LCS(x,y,m-1,n-1)
#		  => Else max(LCS(x,y,m-1,n),LCS(x,y,m,n-1))

def longestsubseq(x,y):
	# 1. declare array of length of x and y
	m = len(x)
	n = len(y)
	L = [ [0]*(n+1) for i in xrange(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			if i==0 and j ==0:
				L[i][j] =0
			elif x[i-1] == y[j-1]:
				L[i][j] = 1 + L[i-1][j-1]
			else:
				L[i][j] = max(L[i-1][j],L[i][j-1])
	return L[m][n]

print longestsubseq('ABCDGH','AEDFHR')