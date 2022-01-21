from cmath import log


log_file = open("um-server-01.txt") #accessing data from the txt file to use in python


def sales_reports(log_file): #creating a function
    for line in log_file: #establishinga  for loop to go through each line of the txt file
        line = line.rstrip() #stripping the whitespace out of the line so the /n is not included in the output
        day = line[0:3] #storing the value of the day into a variable
        if day == "Mon": #if statement checking if the day is Tuesday
            print(line) #printing each line of data that has Tuesday as the day

def ten_melons(log_file):
    for line in log_file:
        line=line.rstrip()
        values = line.split(" ")
        melons_number = float(values[2])
        if melons_number >= 10:
            print(values)


ten_melons(log_file)

# sales_reports(log_file) #invoking the function, passing through the txt file
