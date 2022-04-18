import random
def create_password():
    lower    ="abcdefghijklmnopqrstuvwxyz"
    upper    ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number   = "0123456789"
    symbol   = "}{[]()*/;:_-#!@$£%¢&^~=+§\|><,."
    length   = int(input('Você quer uma senha com quantas letras'))  
    especial = str(input("Deseja incluir caracteres especiais? Sim/Não"))
    if especial =="Sim" or "SIM":
      all = lower+upper+symbol+number
      password = "".join(random.sample(all, length))
      print(password)
    else:
      x = lower + upper
      password = "".join(random.sample(x, length)) 
      print(password)

      
create_password()
