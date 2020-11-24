def primary():
  import math

  f = open("input2.txt")
       
  input = f.readlines()
  f.close()
  word = input[0]
  inarr = word.split(',')
  integerarr=[]
  for i in inarr:
    i=int(i)
    integerarr.append(i)

  # print(integerarr)
  integerarr[1] = 12
  integerarr[2] = 2
  # print(integerarr)

  test = [1,9,10,3,2,3,11,0,99,30,40,50]
  i = 0
  # while i < len(test):
  #   if test[i] == 1:
  #     test[test[i+3]] = test[test[i+1]] + test[test[i+2]]
  #   elif test[i] == 2:
  #     test[test[i+3]] = test[test[i+1]] * test[test[i+2]]
  #   elif test[i] == 99:
  #     break
  #   else:
  #     print('error')
  #     break
  #   i += 4  

  while i < len(integerarr):
    if integerarr[i] == 1:
      integerarr[integerarr[i+3]] = integerarr[integerarr[i+1]] + integerarr[integerarr[i+2]]
    elif integerarr[i] == 2:
      integerarr[integerarr[i+3]] = integerarr[integerarr[i+1]] * integerarr[integerarr[i+2]]
    elif integerarr[i] == 99:
      break
    else:
      print('error')
      break
    i += 4  
  
  print(integerarr[0])

if __name__== "__main__":
  primary()