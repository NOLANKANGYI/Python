def triangles():
	first,second= [1], [1,1]
	yield first
	yield second
	while True:
		second= [1]+[second[i]+second[i+1] for i in range(len(second)-1)]+[1]
		yield second

def pascal_triangle():
	n=int(input("The height of the triangle: "))
	m=0
	results=[]
	for t in triangles():
		results.append(t)
		m=m+1
		if m==n:
			break
	return results
