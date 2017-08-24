# Import the employee_data1.csv and employee_data2.csv files, which currently holds employee records like the below:
# Emp ID,Name,DOB,SSN,State
# 214,Sarah Simpson,1985-12-04,282-01-8166,Florida
# 15,Samantha Lara,1993-09-08,848-80-7526,Colorado
# 411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
# Then convert and export the data to use the following format instead:
# Emp ID,First Name,Last Name,DOB,SSN,State
# 214,Sarah,Simpson,12/04/1985,***-**-8166,FL
# 15,Samantha,Lara,09/08/1993,***-**-7526,CO
# 411,Stacy,Charles,12/20/1957,***-**-8526,PA
# In summary, the required conversions are as follows:



import os
import csv
# us_state_abbrev.py must be saved in the same folder in order to be imported
import us_state_abbrev

# declare the lists based on the final output we need
employee_id = []
first_name = []
last_name = []
dob = []
social_sec = []
state = []

csvpath = os.path.join('Raw_Data', 'employee_data2.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
        

    for row in csvreader:
        
        #skips first row so that literal string "State" is not searched for in the imported file
        if row[4] == "State":
                continue
        employee_id.append(row[0])
        
# The Name column should be split into separate First Name and Last Name columns.

        # variable space finds the space within the name
        space = row[1].find(" ")
        
        # variable first reads string before the space and appends it to list
        first = row[1][:space] 
        first_name.append(first)
        
        # variable last reads string after the spaces and appends it to the list
        last = row[1][space+1:]
        last_name.append(last)
        
# The DOB data should be re-written into DD/MM/YYYY format.
        
        # variable year takes first four numbers of the string as the year
        year = row[2][:4]
        # variable month takes the month after the year from between the hyphens
        month = row[2][5:7]
        # variable day takes the last bit of the string as the day
        day = row[2][8:]
        # list is appended in order to meet format requirements
        dob.append(month+'/'+day+'/'+year)
        
# The SSN data should be re-written such that the first five numbers are hidden from view.
        # variable new_ssn hides first five numbers behind hashes, then joins with last four and appends to scoial_sec list
        new_ssn = "###-##-"+row[3][7:]
        social_sec.append(new_ssn)
        
# The State data should be re-written as simple two-letter abbreviations.
        # variable abbrev uses string in row 4 (long state name) to call and return the abbreviation
        abbrev = us_state_abbrev.us_state_abbrev[row[4]]
        # row 4 is updated with the abbreviation
        state.append(abbrev)
        
    # zip together the lists for output in the new file       
    cleaned_csv = zip(employee_id, first_name, last_name, dob, social_sec, state)
    
    # write the header for the new file
    header = ['Employee ID','First Name','Last Name','DOB','SSN','State']
    
    # creates the output path and filename
    output = os.path.join('Export', 'boss.csv')
    
    # opens the output file to write to
    with open(output, "w") as cleaned_file:
        writer = csv.writer(cleaned_file)
        
        # writes the header
        writer.writerow(header)
        
        # writes the rows
        writer.writerows(cleaned_csv)
               
       

       

        
        