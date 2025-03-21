import csv
import pendulum

"""
This script reads the summary_precip_data.csv file and prints the gage_id, event_date, event_time, and 
event_duration for each row.

Precipitation data were generated using the Walnut Gulch Experimental Watershed (WGEW) DAP site: 
(https://www.tucson.ars.ag.gov/dap/).

The following query data were used to generate the precipitation data:
Gages: 1-5,7-72,74,76,79-83,87-92,100-109,181-184,186,384,398-428
For the period 1/1/2000 to 12/31/2025
For all months
Summary output
Text format

The resulting output was saved as summary_precip_data_raw.csv


Notes:
event duration is in minutes

event depth is in inches

was initially converting the duration values from strings to integers, but that was causing an error because 
some values in the input data set were floats and it is not clear if floats are possible or not.

"""

with open("data/summary_precip_data.csv", "r") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    next(reader, None)  # skip the headers   
    for row in reader:
        gage_id = row[0]
        event_date_str = row[1]        
        event_time_str = row[2]
        event_date_time_str = f"{event_date_str}T{event_time_str}"
        event_date_time_obj = pendulum.from_format(event_date_time_str, "M/D/YYYYTHH:mm")
        event_duration = float(row[3])
        event_depth = float(row[4])
        print(gage_id, event_depth)

