# sharp_reader.py
This is a simple python script to read out the *.csv files created from sharphound.ps1

# Requirements:
- python3 +
- Only takes one *.csv argument

# Usage:

 python3 sharp_reader.py <file.csv>

 ./sharp_reader.py <file.csv>
 
# Example:
Run:

./sharp_reader.py group_memberships.csv                                    

Output:

[+] Make sure that you are running Python3.x.x

[+] This function only takes *.csv files

[+] Accessing values from group_memberships.csv

[+]

[+] Header row for group_memberships.csv:

"GroupName","AccountName","AccountType"


[+] Values for group_memberships.csv:

Domain Users@agents.spy,"Administrator@agents.spy","user"

Group Policy Creator Owners@agents.spy,"Administrator@agents.spy","user"

Domain Admins@agents.spy,"Administrator@agents.spy","user"

Enterprise Admins@agents.spy,"Administrator@agents.spy","user"

(Remaining Output Omitted)...
 
# Example (filtering result):
Extracting Users from *Admins* using bash pipes (Debian Linux)

Run:

./sharp_reader.py group_memberships.csv | grep Admins | grep user | sort -u

Output:

Domain Admins@agents.spy,"fleiter@agents.spy","user"

Enterprise Admins@agents.spy,"Administrator@agents.spy","user"

Enterprise Admins@agents.spy,"fleiter@agents.spy","user"

Schema Admins@agents.spy,"Administrator@agents.spy","user"

(Remaining Output Omitted)...
