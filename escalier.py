# -*- coding: utf-8 -*-

chiffre = int(input("entre un chiffre "))
i=0
while i<=chiffre :
  b = (chiffre-i)*(" ")
  d = i*("#")
  print(b+d)
  i = i+1

print("tu peux monter maintenant")
