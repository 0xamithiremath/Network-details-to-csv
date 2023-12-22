import re
import csv

# Define a regular expression pattern to match interface information
pattern = r'(\S+) is (\S+), line protocol is (\S+)[\s\S]+?(\d+) packets input, (\d+) bytes[\s\S]+?(\d+) packets output, (\d+) bytes'

# Initialize a list to store interface data
interfaces_data = []

# Read the output from the "show interfaces" command (replace this with your actual output)
with open('show_interfaces_output.txt', 'r') as file:
    output = file.read()

# Find all matches of the pattern in the output
matches = re.findall(pattern, output)

# Process each match and extract relevant data
for match in matches:
    interface = match[0]
    status = match[1]
    line_protocol = match[2]
    input_packets = match[3]
    input_bytes = match[4]
    output_packets = match[5]
    output_bytes = match[6]
    
    # Append the data to the interfaces_data list
    interfaces_data.append([interface, status, line_protocol, input_packets, input_bytes, output_packets, output_bytes])

# Define the CSV file name
csv_filename = 'interfaces_data.csv'

# Write the data to a CSV file
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the header row
    csv_writer.writerow(['Interface', 'Status', 'Line Protocol', 'Input Packets', 'Input Bytes', 'Output Packets', 'Output Bytes'])
    
    # Write the interface data
    csv_writer.writerows(interfaces_data)

print(f'Data has been exported to {csv_filename}')
