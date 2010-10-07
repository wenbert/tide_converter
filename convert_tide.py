import os, sys

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

adjustment = raw_input("Adjust how many hours? (1 or 2) >")

adjustment = int(adjustment)

if os.path.exists(input_file):
    output_file = raw_input("Enter the filename of the output file: ")

start_line = 8 #you can edit this


error = False
try:
    new_file = open(output_file, 'w')
    new_file.truncate()
    print "Creating file %s ....." % output_file
    
    i = 0 #line/row counter
    day_counter = 1 #counter for minus 1 day
    minute_counter = 0 #0, 10, 20, 30, 40, 50
    start = 0
    trigger_start = False
    
    for line in open(input_file, 'r'):
        
        #remove unnessarcy text in the line
        line = line.replace("."," ")
        line = line.replace(":"," ")
        line = line.replace("\t"," ")
        line = line.replace("\r\n","")
        
        pieces = line.split(" ");
        
        day = int(pieces[0])
        month = int(pieces[1])
        year = int(pieces[2])
        hour = int(pieces[3])
        minutes = int(pieces[4])
        tide = float(pieces[5])
        
        if i < 6 and adjustment == 1:
            day = day - 1
            #print "------------------------------"
        
        if i < 12 and adjustment == 2:
            day = day - 1
            #print "------------------------------"
            
        if i > 0 and i % 144 == 0:
            print "------------------------------"
            trigger_start = True
        
        # for succeeding days
        if trigger_start:
            print "##############################"
            start = start + 1
            day = day - 1
        
        if start > 5 and adjustment == 1:
            start = 0
            trigger_start = False
        elif start > 11 and adjustment == 2:
            start = 0
            trigger_start = False
        
        print month, day, year, hour, minute_counter, tide, " start: ", start
        
        #reset minute_counter
        if minute_counter >= 50:
            minute_counter = 00
        else:
            minute_counter = minute_counter + 10
        
        #output in screen and write to file
        #print "%s %s %s %s %s" % (pieces[1], pieces[0], pieces[2], pieces[3], pieces[4]),
        #print month, day, year, hour, minutes, tide
        #new_file.write("%s %s %s %s %s %s" % (month, day, year, hour, minutes, tide))
            
        i = i + 1
        
    new_file.close()
    
except:
    print "Unexpected error",  sys.exc_info()[0]

raw_input("Press enter to exit")