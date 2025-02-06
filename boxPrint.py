message = "Hello World in a frame"
doodadMessage = message.split()
thingForSpaces="*********"
print("*********")
replay=0
lengthOfWord=len(thingForSpaces)

for i in doodadMessage:
  thingyWordLen=len(i)
  if thingyWordLen<lengthOfWord:
    numSpaceAdd=lengthOfWord-thingyWordLen
    rounds=0
    while rounds < numSpaceAdd:
      i=i+" "
      rounds+=1
  print("*"+doodadMessage[replay]+"*")
  replay+=1
print("*********")
