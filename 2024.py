numbers = [[1,2,3], [4,5,6], [7,8,9]]
resuits=[]

for row in numbers:
    for element in row:
        if element % 2==0:
          resuits.append(element)

print("짝수인 숫자 :",resuits)
