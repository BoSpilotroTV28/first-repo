message = "Hello World in a frame"
doodadMessage = message.split()
thingForSpaces="*********"
print(" ********")
replay=0
lengthOfWord=len(thingForSpaces)

for i in doodadMessage:
  thingyWordLen=len(i)
  if thingyWordLen<lengthOfWord:
    numSpaceAdd=lengthOfWord-thingyWordLen
    limit=numSpaceAdd-1
    rounds=0
    spaces=[]
    while rounds < limit:
      i=i+" "
      rounds+=1
  print("*"+i+"*")
  replay+=1
print(" ********")
