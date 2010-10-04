from sys import argv
import os

script, input_file, output_file = argv
"""
input_file:         your tide input file
output_file:        the name of the output file
"""
print "Tide Format Converter"
print "CTRL + C to exit"

#input_file = raw_input("Enter the location of file you want to convert: ")
#output_file = raw_input("Enter the filename of the output file: ")

start_line = 8 #you can edit this

i = 0;
error = False
cwd = os.getcwd()
try:
    new_file = open(output_file, 'w')
    new_file.truncate()
    print "Creating file:", output_file, 
    
    for line in open(input_file, 'r'):  
        if i >= start_line: #start reading at specified linen number
            
            #remove unnessarcy text in the line
            line = line.replace("."," ")
            line = line.replace("\t"," ")
            line = line.replace("\r","")
            
            #split the line
            pieces = line.split(" ");
    
            #add :00 in the time
            pieces[3] = pieces[3]+":00"
            
            #output in screen and write to file
            #print "%s %s %s %s %s" % (pieces[1], pieces[0], pieces[2], pieces[3], pieces[4]),
            new_file.write("%s %s %s %s %s" % (pieces[1], pieces[0], pieces[2], pieces[3], pieces[4]))
    
        i = i + 1
        
    new_file.close()
    print "-------------------------------------------------------------"
    print "Time zone is GMT + 1 hour in the Winter Time"
    print "and GMT + 2 hours in the Summer Time (daylight saving time)."
    
except IOError as (errno, strerror):
    print "I/O error({0}): {1}".format(errno, strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

raw_input("Press enter to exit")