from converter import Converter
import os, sys

input_file = raw_input("Enter the location of file you want to convert > ")
while not os.path.exists(input_file):
    print "'%s' not found. " % input_file
    input_file = raw_input("Please enter again the filename you want to convert > ")

while True:
    adjustment = raw_input("Adjust how many hours? (1 or 2) > ")
    adjustment = int(adjustment)
    if adjustment == 1 or adjustment == 2: break

if os.path.exists(input_file):
    output_file = raw_input("Enter the filename of the output file > ")
else:
    pass

try:
    tide = Converter()
    tide.set_input_file(input_file)
    tide.set_adjustment(adjustment)
    tide.set_output_file(output_file)
    tide.process_file()
    tide.close()
except:
    print "Unexpected error", sys.exc_info()

print "Conversion successful. The new file is: ", output_file
raw_input("Press enter to exit")