print ('4etnie ili ne4etnie?')
varAnsw = input()
i = 0
if varAnsw == 'ne':
	for i in range(1,21,2):
		print (i, end=',')
if varAnsw == '4et':
	for i in range(0,21,2):
		print (i, end=',')
	
