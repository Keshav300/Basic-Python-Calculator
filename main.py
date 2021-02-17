# Funtions to calculate
def add(a1, a2):
  ao = a1 + a2
  return ao

def sub(s1, s2):
  so = s1 - s2
  return so

def div(d1, d2):
  if(d2 == 0):
    print("You cannot divide by 0")
    return
  do = d1 / d2
  return do

def mult(m1, m2):
  mo = m1 * m2
  return mo

def po(p1, p2):
  pofo = p1 ** p2
  return pofo

def choices():
  print("multiply, divide, subtract, add or po (power of)")

# for example if you see d1, d2 those are the numbers to divide
# if you are dividing by a zero, you will get an error so this program catches it before it gets logged as an error
# do is division output so that is the way you get the output
# the return give the value of the do making it possible for the user to recive the info
# also the return with no values after it will just stop the program

#ui
choices()
type = input("")
c = ["multiply", "divide", "subtract", "add", "po"]

#anti -err
while(type not in c):
  print("That is not a choice, please choose from:")
  choices()
  type = input("")

#more userinterface (chosing the numbers)
num1 = str(input("What is your first number? "))
num2 = str(input("What is your second number?"))

#decimal converter
if("." in num1):
  num1 = float(num1)

else:
  num1 = int(num1)

if("." in num2):
  num2 = float(num2)

else:
  num2 = int(num2)

#output
if(type == "multiply"):
  num = mult(num1, num2)

elif(type == "divide"):
  num = div(num1, num2)

elif(type == "add"):
  num = add(num1, num2)

elif(type == "subtract"):
  num = sub(num1, num2)

elif(type == "po"):
  num = po(num1, num2)

#finalized output
print("Your final number is ", str(num))
