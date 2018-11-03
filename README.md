# CastorVH
TCO Hackathon

The program webscraper.py file has the code for parsing universities in United States from http://web3.ncaa.org/directory/memberList?type=12&division=I

The dependencies for executing the code are mentioned in dependencies.txt and can be installed using pip.
The code was executed on Mac OS X, Ubuntu System.
The results parsed from the website are stored in MSSQL Server 2017 database.

Before executing the webscraper.py, you need to execute the querries webscraper.txt file to create the database and the table schema.
Then you need to pass username, password, server name and database name necessary for MS SQL Server while executing webscraper.py as command line arguments "python3 webscraper.py username server_name password database name".
