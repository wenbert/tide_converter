import os, sys, datetime, calendar

class Converter(object):
    
    def __init__(self):
        self.adjustment = 0
        self.input_file = ""
        self.output_file = ""
        self.new_file = "" #handler for the output_file
        self.start_line = 8 #starting line for the raw file
        self.minute_counter = 0
        
        self.day = 0
        self.month = 0
        self.year = 0
        self.hour = 0
        self.minutes = 0
        self.tide = 0.0
        
    def process_file(self):
        i = 0
        raw_count = 0
        minute_counter = 0 #0, 10, 20, 30, 40, 50
        trigger_start = False #flag for start of succeeding days
        start = 0 #will count up to 5 for 1hour adjustment and 11 for 2hours adjustment
        start_line = self.start_line
        input_file = self.input_file
        adjustment = self.adjustment
        
        for line in open(input_file, 'r'):
            if raw_count >= start_line:
                #remove unwated characters in the line
                line = line.replace(".", " ") #replace with space
                line = line.replace(":", " ") #replace with space
                line = line.replace("\t", " ") #replace with space
                line = line.replace("\r\r","") #replace with nothing
                
                pieces = line.split(" ")
                
                self.day = int(pieces[0])
                self.month = int(pieces[1])
                self.year = int(pieces[2])
                self.hour = int(pieces[3])
                self.minutes = int(pieces[4])
                self.tide = float(pieces[5]) * 0.01 #convert tide to meters
                
                #check for the first day of the month bug
                if i < 6 and adjustment == 1:
                    self.day -= 1
                    self.hour -= 1
                    self.check_hour_of_day()
                    self.check_day_of_month()
                        
                #check for the first day of the month bug
                #for 2 hour adjustment
                if i < 12 and adjustment == 2:
                    for n in range(0, 2): #do twice
                        self.day -= 1
                        self.hour -= 1
                        self.check_hour_of_day()
                        self.check_day_of_month()                
                        
                #if after the 2nd day / succeeding days
                #144 lines == 1 day (with 10 minutes for 24 hours)
                if i > 0 and i % 144 == 0:
                    trigger_start = True
                    
                #check for trigger_start
                if trigger_start:
                    start += 1
                    self.day -= 1
                    self.check_day_of_month()
                    
                if start > 5 and adjustment == 1:
                    start = 0
                    trigger_start = False
                elif start > 11 and adjustment == 2:
                    start = 0
                    trigger_start = False
                else:
                    pass
                
                #reset minute_counter
                #wa nakoy sure ani nga part!!!!
                if self.minute_counter >= 50:
                    self.minute_counter = 0
                else:
                    self.minute_counter += 10
                
                self.write_to_file()
                
                i += 1
                
            raw_count += 1
        
    def write_to_file(self):
        self.new_file.write("%02d %02d %d %02d %02d %07.2f\n" % (self.month, self.day, self.year, self.hour, self.minutes, self.tide))
        
    def set_input_file(self,input_file):
        """
        set_input_file(output_file)
            Sets the input_file
        """
        self.input_file = input_file
        
    def set_output_file(self,output_file):
        """
        set_output_file(output_file)
            Sets the output_file
        """
        self.output_file = output_file
        self.new_file = open(output_file, 'w')
        self.new_file.truncate()
        
    def set_adjustment(self,adjustment):
        """
        set_adjustment(adjustment)
            Sets adjusment
        """
        self.adjustment = adjustment
    
    def check_hour_of_day(self):
        """
        check_hour_of_day():
            Check if the hour is -1. If -1, set to 23 and if -2, set to 22
        """
        self.hour = 24 + self.hour
    
    def check_day_of_month(self):
        """
        check_day_of_month()
            Checks if the day is "0". If "0", set it to the last day of the
            previous month
        """
        if self.day == 0:
        #return calendar.monthrange(year, month)[1]
            self.day = calendar.monthrange(self.year, self.month)[1]
            self.month -= 1
            
    def close(self):
        self.new_file.close()