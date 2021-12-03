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

  inputrange = list(range(0, 100))

  print(inputrange)

  # print(integerarr)
  for j in inputrange:
    for k in inputrange:
      integerarr=[]
      for i in inarr:
        i=int(i)
        integerarr.append(i)
      integerarr[1] = j
      integerarr[2] = k
      i = 0
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
      if integerarr[0] == 19690720:
        print(integerarr[0], integerarr[1], integerarr[2], 100 * integerarr[1] + integerarr[2])
        break
      

if __name__== "__main__":
  primary()