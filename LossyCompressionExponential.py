import random
import struct
# # random.uniform() to generate floating point numbers from uniform distribution
# numberUniform = random.uniform(0, 100)

# # random.gauss() to generate floating point numbers from gaussian distribution
# numberGauss = random.gauss(50, 25)
# print(numberGauss)

# # random.expovariate() to generate floating point numbers from exponential distribution
# numberExpo= random.expovariate(0.025)
# print(numberExpo)

ArrayLossy = []


def LossyCompression(numberOfData):

    fullPrecisionFile= open("fullPrecisionBinary.txt", "wb")
    
    for i in range(numberOfData):
        numberUniform = random.expovariate(0.025)
        # pack the float as a binary string
        symbols = struct.pack('>f', numberUniform)
        # convert each byte to binary and join them
        binaryValue = ''.join(format(c, '08b') for c in symbols)
        ArrayLossy.append(binaryValue)
        fullPrecisionFile.write(struct.pack('f' , numberUniform))

    fullPrecisionFile.close()

    # # Open file in binary write mode
    LossyFile = open("LossyCompressionBinary.txt", "wb") 
    # # Write bytes to file
    for i in range(len(ArrayLossy)):
        binaryValue = ArrayLossy[i][:16]
        integerConversion = int(binaryValue, 2)

        LossyFile.write(struct.pack('H', integerConversion))

    LossyFile.close()
 
    with open("LossyCompressionBinary.txt", "rb") as f:
        data = f.read()
    
        # Initialize the new byte array
    floats = []

    for i in range(0, len(data), 2):
        # Read 2 bytes (16-bit integer)
        chunk = data[i:i+2]
        # Unpack as unsigned short ('H')
        integerValue = struct.unpack('H', chunk)[0]
        # Convert to 32-bit binary string, padded with 16 zeros
        paddedBinary = f"{integerValue:016b}" + "0" * 16
        # Convert the padded binary string to an integer
        integerConversion = int(paddedBinary, 2)
        # Pack the integer as a 32-bit float and unpack it
        floatValue = struct.unpack('f', struct.pack('I', integerConversion))[0]
        floats.append(floatValue)
    with open("LossyNumberAfter.txt", "w") as LossyNumberAfter:
        LossyNumberAfter.write("\n".join(map(str, floats)))

#########################################################################################

    #Outputting the conversion back into float from Full Precision
    with open("fullPrecisionBinary.txt", "rb") as f:
        data = f.read()

    num_floats = len(data) // 4  # Since each float is 4 bytes

    # Unpack all floats
    numbers = "\n".join(list(map(str,struct.unpack(f"{num_floats}f", data))))
    fullPrecisionFileNumbers= open("fullPrecisionNumbers.txt", "w")
    fullPrecisionFileNumbers.write(numbers)

    fullPrecisionFileNumbers.close()

LossyCompression(1000000)