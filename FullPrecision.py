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




# Open file in binary write mode
fullPrecisionFile= open("fullPrecision.txt", "wb")
 
# Write bytes to file
for i in range(10000000):
    numberUniform = random.uniform(0, 100)
    fullPrecisionFile.write(struct.pack('f' , numberUniform))
    
# Close file
fullPrecisionFile.close()


# How to read from the file and also copy down the conversion of binary to float into another file

# Open the file in binary read mode, save all binary data into data
with open("fullPrecision.txt", "rb") as f:
    data = f.read()

# Ensure we have the correct number of bytes
num_floats = len(data) // 4  # Since each float is 4 bytes

# Unpack all floats
numbers = "\n".join(list(map(str,struct.unpack(f"{num_floats}f", data))))
fullPrecisionFileNumbers= open("fullPrecisionNumbers.txt", "w")
fullPrecisionFileNumbers.write(numbers)

fullPrecisionFileNumbers.close()
