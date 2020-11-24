def primary():
  import math

  f = open("input.txt")
       
  input = f.readlines()
  f.close()

  total=[]
  for i in input:
    y = (math.floor(int(i)/3))-2
    z= 0
    while y > 0: # 
      print('y=', y)
      z += y
      y = (math.floor(y/3))-2
      print('z=', z)


   
    total.append(z)

  print(total)
  result = sum(total)
  print(result)
if __name__== "__main__":
  primary()