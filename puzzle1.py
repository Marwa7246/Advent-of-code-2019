def primary():
  import math

  f = open("input.txt")
       
  input = f.readlines()
  f.close()

  total=[]
  for i in input:
    y = (math.floor(int(i)/3))-2
    # print(y)
    total.append(y)

  print(total)
  result = sum(total)
  print(result)
if __name__== "__main__":
  primary()