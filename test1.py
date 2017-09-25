def matxRound(M, decPts=4):
	for i in range(len(M)):
		for j in range(len(M[i])):
			M[i][j] = round(float(M[i][j]), 4)
			j += 1
	i += 1
	return M

I = [[1,0,0,0],
    [0,1.012345,0,0],
    [0,0,1,0],
    [0,0,0,1]]


print matxRound(I, decPts=4)

# i, j = 0

# for i in range(len(I)):
# 	for j in range(len(I[i])):
# 		I[i][j] = round(float(I[i][j]), 4)
# 		j += 1
# 	i += 1

# print I

# I[0] = [4]

# L = [[1,1],[1,1],[1,1],[1,1]]

# for i in range(len(L)):
# 	for j in range(len(L[i])):
# 		L[i][j] = round(float(2), 2)
# 		j += 1
# 	j += 1
# # L[0][0] = 2
# print L