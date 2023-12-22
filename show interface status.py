import re
import csv

# Sample "show interface status" output
show_interface_status_output = """
Port      Name               Status       Vlan       Duplex  Speed Type
Gi1/0/1   Server-1           connected    10         full   1000 1000BaseTX
Gi1/0/2   PC-1               notconnect   20         auto   auto No Gbic
Gi1/0/3   Printer-1          connected    30         full   1000 1000BaseTX
Gi1/0/4   PC-2               connected    20         full   1000 1000BaseTX
"""

# Create a list to hold the extracted data
data = []

# Parse the output using regular expressions
for line in show_interface_status_output.strip().split('\n')[2:]:
    parts = re.split(r'\s+', line.strip())
    if len(parts) == 7:
        port, name, status, vlan, duplex, speed, port_type = parts
        data.append([port, name, status, vlan, duplex, speed, port_type])

# Define the CSV file name
csv_filename = 'interface_status.csv'

# Write the data to a CSV file
with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write the header
    csv_writer.writerow(['Port', 'Name', 'Status', 'Vlan', 'Duplex', 'Speed', 'Type'])
    # Write the data rows
    csv_writer.writerows(data)

print(f'Data has been exported to {csv_filename}')
