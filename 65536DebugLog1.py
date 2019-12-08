# -*- coding: utf-8 -*-

import random
import struct

memoryPtr = 0;


fileMemory = []
while memoryPtr < 65536:
  if memoryPtr < 16:
    temp = random.randint(32,126)
    fileMemory.append(temp)
  elif memoryPtr < 128:
    temp = 0x00
    fileMemory.append(temp)
  elif memoryPtr == 128:
    temp = 0x0E
    fileMemory.append(temp)
    temp = 0x10
    fileMemory.append(temp)
    memoryPtr += 1
  elif memoryPtr < 144:
    temp = 0x00
    fileMemory.append(temp)
  elif memoryPtr == 144:
    temp = 0x07
    fileMemory.append(temp)
    temp = 0xE1
    fileMemory.append(temp)
    temp = random.randint(1,13)
    fileMemory.append(temp)
    temp = random.randint(1,28)
    fileMemory.append(temp)
    temp = 0x10
    fileMemory.append(temp)
    temp = random.randint(0,24)
    fileMemory.append(temp)
    temp = random.randint(0,60)
    fileMemory.append(temp)
    temp = random.randint(0,60)
    fileMemory.append(temp)
    memoryPtr += 7
  elif memoryPtr < 160:
    temp = 0x00
    fileMemory.append(temp)
  elif memoryPtr == 160:
    temp = 0x07
    fileMemory.append(temp)
    temp = 0xE2
    fileMemory.append(temp)
    temp = random.randint(1,13)
    fileMemory.append(temp)
    temp = random.randint(1,28)
    fileMemory.append(temp)
    temp = 0x10
    fileMemory.append(temp)
    temp = random.randint(0,24)
    fileMemory.append(temp)
    temp = random.randint(0,60)
    fileMemory.append(temp)
    temp = random.randint(0,60)
    fileMemory.append(temp)
    memoryPtr += 7
  elif memoryPtr < 176:
    temp = 0x00
    fileMemory.append(temp)
  elif memoryPtr == 176:
    temp = 0x00
    fileMemory.append(temp)
    temp = 0x00
    fileMemory.append(temp)
    temp = 0x03
    fileMemory.append(temp)
    temp = 0x80
    fileMemory.append(temp)
    memoryPtr += 3
  elif memoryPtr < 256:
    temp = 0x00
    fileMemory.append(temp)
  else:
    temp = random.randint(0,255)
    fileMemory.append(temp)
    if memoryPtr % 2 == 1 and memoryPtr > 40000:
      if random.randint(0,2000) > 1957:
        break
  memoryPtr+=1;

with open("text.txt","wb") as fout:
  for x in fileMemory:
    fout.write(struct.pack("B",x))
