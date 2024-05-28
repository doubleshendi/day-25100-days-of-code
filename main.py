#def pinpicker(number):
  #import random
  #pin = ""
  #or i in range(number):
  #  pin += str(random.randint(0,9))
 # return pin

#mypin = pinpicker(4)
#print(mypin)

import random

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

print( bcolors.HEADER, " CHARECTER STAT GENERATOR " + bcolors.ENDC)
print()
warrior = input("Name your warrior: ")
def rolldice(roll):
  
  rollResult = random.randint(1,roll)
  
  return rollResult
print( "Your health is " + bcolors.OKBLUE, rolldice(6)*rolldice(8), "hp")

