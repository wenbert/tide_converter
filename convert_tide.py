import os, sys, datetime, calendar

"""
input_file:         your tide input file
output_file:        the name of the output file
"""

def check_day_of_month(year, month):
    return calendar.monthrange(year,month)[1]
    
print "Tide Format Converter"
print "CTRL + C to exit"

input_file = raw_input("Enter the location of file you want to convert > ")

while not os.path.exists(input_file):
    print "'%s' not found." % input_file
    input_file = raw_input("Please enter again the filename you want to convert > ")

#adjustment must be set to either 1 or 2
#if 1, we move back the minute column by 60 minutes
#if 2, we move back the minute column by 120 minutes
adjustment = 0
while True:
    adjustment = raw_input("Adjust how many hours? (1 or 2) > ")
    adjustment = int(adjustment)
    if adjustment == 1 or adjustment == 2: break

if os.path.exists(input_file):
    output_file = raw_input("Enter the filename of the output file > ")

try:
    new_file = open(output_file, 'w')
    new_file.truncate()
    print "Creating file %s ....." % output_file
    
    i = 0 #line/row counter
    raw_count = 0 #line counter including the header
    minute_counter = 0 #0, 10, 20, 30, 40, 50
    start = 0
    trigger_start = False
    start_line = 8 #starting line for the raw file
    
    for line in open(input_file, 'r'):
        
        #only process if "i" is greater than equal to the 8th line
        if raw_count >= start_line:
            
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
            tide = float(pieces[5])*0.01
            
            #check for first day of month bug here
            if i < 6 and adjustment == 1:
                day -= 1
                if day == 0:
                    day = check_day_of_month(year, month)
                    month -= 1
            
            #check for first day of month bug here
            if i < 12 and adjustment == 2:
                day -= 1
                if day == 0:
                    day = check_day_of_month(year, month)
                    month -= 1
                
            if i > 0 and i % 144 == 0:
                trigger_start = True
            
            # for succeeding days
            if trigger_start:
                start = start + 1
                day -= 1
                if day == 0:
                    day = check_day_of_month(year, month)
                    month -= 1
            
            if start > 5 and adjustment == 1:
                start = 0
                trigger_start = False
            elif start > 11 and adjustment == 2:
                start = 0
                trigger_start = False
            
            #reset minute_counter
            if minute_counter >= 50:
                minute_counter = 0
            else:
                minute_counter += 10
            
            #new_file.write("%02d %02d %d %02d %02d %07.2f\n" % (month, day, year, hour, minutes, tide))
            new_file.write("%02d %02d %d %02d %02d %07.2f\n" % (month, day, year, hour, minute_counter, tide))
            
            i += 1
            
        raw_count += 1
        
    new_file.close()
    print "Conversion successful. The new file is: ", output_file
    
except:
    print "Unexpected error",  sys.exc_info()[0]

raw_input("Press enter to exit")