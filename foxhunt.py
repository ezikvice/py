import os
import random

def clear():
  os.system('clear')

def get_N(mn=2,mx=8):
  while True:
    try:
      N=int(input('введите количество строк:\n'))
      if(mn>N or N>mx):
        raise ValueError
      return N
    except ValueError as err:
      clear()
      print('введите целое число от {} до {}'.format(mn, mx))

clear()
N=get_N()

def myPrint(field):
  for i in range(0,N):
    for k in range(0,N):
      print(field[i*N+k], end=' ')
    print()
  print()

def printField(field):
  clear()
  myPrint(field)  

field = []
mines = N//2
for i in range(mines):
	field.append(1)
for i in range(N**2-mines):
  field.append(0)

random.shuffle(field)
#printField(field)

b = []
for i in range(len(field)):
  row = i//N
  col = i%N
  if(field[i]==1):
    b.append('X')
#    print('b[{}][{}]=X'.format(row, col))
  else:
    vertSum = field[col:len(field):N].count(1)
    horSum = field[row*N:(row+1)*N:1].count(1)
    b.append(vertSum + horSum)
#    print('b[{}][{}]={}+{}, from {} to {}'.format(row, col, horSum, vertSum, row*N, (row+1)*N ))
#printField(b)

c=[x for x in '¤'*N**2]
printField(c)

myPrint(field)

def getField():
  while True:
    try:
#      clear()
      s = input('введите строку, столбец:\n')
      inputField = s.split()
      for i in range(len(inputField)):
        inputField[i] = int(inputField[i])
        if(0>inputField[i] or N<=inputField[i]):
          raise ValueError
      return inputField
    except ValueError as error:
      printField(c)
      print('''введите два числа, разделенных 
      	пробелами, меньше {}'''.format(N))
      continue
      
def printVictory():
  print('''    ################
    # УРА! ПОБЕДА! #
    ################
    	
    	''')        
      
      
#### основной цикл
GAMEOVER = False
while not GAMEOVER:
  if(c.count('¤')==mines):
    GAMEOVER = True
    clear()
    printVictory()
    continue
  row, col = getField()
  i = row*N+col # индекс в списке
  c[i]=b[i]
  if(field[i] == 1):
    GAMEOVER = True
    clear()
    printField(c)
    print('''На поле [{}][{}] была мина.
     гамовер'''.format(row, col))
  else:
    clear()
    printField(c)
    print('Количество мин: {}'.format(b[i]))
    
