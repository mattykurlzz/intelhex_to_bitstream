hexFile = open('file.hex', 'r')
outputFile = open('output.bin', 'wb')

commonDataShift = 9

hexFile.readline()

line = hexFile.readline()
output_string = bytes()
prevadr = int(line[3:7], base=16)
prevLineByteLength = 0
while line:
  if(line[7:9] == '00'):
    adr = int(line[3:7], base=16)
    lineByteLength = int(line[1:3], base=16)
    if adr > prevLineByteLength + prevadr: # пропустили адрес, надо заполнить кусок нулями
      for i in range(adr - prevLineByteLength - prevadr): output_string += int(0).to_bytes(1, 'little')
    for i in range(lineByteLength):
      output_string += int(line[commonDataShift + i * 2 : commonDataShift + 2 + i * 2], base=16).to_bytes(1, 'little')

    prevadr = adr
    prevLineByteLength = lineByteLength
  elif(line[7:9] == '04'): print('next_block')
  line = hexFile.readline()
outputFile.write(output_string)
