import os

"""
input_file:         your tide input file
output_file:        the name of the output file
"""
print "Tide Format Converter"
print "CTRL + C to exit"

input_file = raw_input("Enter the location of file you want to convert: ")

while not os.path.exists(input_file):
    print "'%s' not found." % input_file
    input_file = raw_input("Please enter again the filename you want to convert: ")

if os.path.exists(input_file):
    output_file = raw_input("Enter the filename of the output file: ")

start_line = 8 #you can edit this

i = 0;
error = False
try:
    new_file = open(output_file, 'w')
    new_file.truncate()
    print "Creating file %s ....." % output_file
    
    for line in open(input_file, 'r'):  
        if i >= start_line: #start reading at specified linen number
            
            #remove unnessarcy text in the line
            line = line.replace("."," ")
            line = line.replace("\t"," ")
            line = line.replace("\r","")
            
            #split the line
            pieces = line.split(" ");
            
            #output in screen and write to file
            #print "%s %s %s %s %s" % (pieces[1], pieces[0], pieces[2], pieces[3], pieces[4]),
            new_file.write("%s %s %s %s %s" % (pieces[1], pieces[0], pieces[2], pieces[3], pieces[4]))
    
        i = i + 1
        
    new_file.close()
    print "-------------------------------------------------------------"
    print "Time zone is GMT + 1 hour in the Winter Time"
    print "and GMT + 2 hours in the Summer Time (daylight saving time)."
    
except:
    print "Unexpected error"

raw_input("Press enter to exit")