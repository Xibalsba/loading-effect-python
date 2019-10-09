'''
Github: https://github.com/Xibalsba/loading-effect-python
Autor: Julio López López
Email: jl573160@gmail.com
'''
import os

KEYS = ["/","-","\\"];

def loading_effect(time):
  cont = 0
  time_2 = 1

  while(time_2 < time):
    for key in KEYS:
        os.system('clear')
        print(key)

        if cont <= 1:
          cont+=1
        else:
          cont=0
    time_2+=1
  os.system('clear')
  print("The process has been completed satisfactorily!")

loading_effect(100)
