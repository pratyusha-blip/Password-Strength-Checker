password=input('Enter Password')
has_upper= False
has_lower= False
has_digit= False
has_special= False

for i in password:
  if i.isupper():
    has_upper= True
  elif i.islower():
    has_lower= True
  elif i.isdigit():
    has_digit= True
  else:
    has_special= True

  score=0
if len(password)>=8:
    score+=1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_special:
    score += 1

if score <= 2:
    print("Weak Password")
elif score <= 4:
    print("Medium Password")
else:
    print("Strong Password")