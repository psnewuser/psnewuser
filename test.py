print("Do you need to activate this? [ Y/N]")
act=["y","Y"]
for act in act:
  print("ACTIVATED")
  if act==input():
    print("Hello World!")
    
else:
  print("DEACTIVED")
  print("PROGRAMS END")

print("GoodBye!!!")
