# sharphound_csv_reader.py
This is a simple python script to read out the *.csv files created from sharphound.ps1

# Requires:
- python3 +
- Only takes one *.csv argument

# Usage:

 python3 sharphound_csv_reader.py <file.csv>

 ./sharphound_csv_reader.py <file.csv>
 
# Example of extracting Users from *Admins* using bash pipes

./sharphound_csv_reader.py group_memberships.csv | grep Admins | grep user | sort -u

Output:

Domain Admins@agents.spy,"Administrator@agents.spy","user"
Domain Admins@agents.spy,"fleiter@agents.spy","user"
Domain Admins@agents.spy,"SQLService@agents.spy","user"
Enterprise Admins@agents.spy,"Administrator@agents.spy","user"
Enterprise Admins@agents.spy,"fleiter@agents.spy","user"
Enterprise Admins@agents.spy,"SQLService@agents.spy","user"
Schema Admins@agents.spy,"Administrator@agents.spy","user"
Schema Admins@agents.spy,"fleiter@agents.spy","user"
Schema Admins@agents.spy,"SQLService@agents.spy","user"
