# CastorVH
TCO Hackathon

The code contains a webscraper.py file containing code for parsing universities in United States from 
http://web3.ncaa.org/directory/memberList?type=12&division=I

The dependencies for executing the code are mentioned in dependencies.txt and can be installed using pip.
The code was executed on Mac OS X, Ubuntu System.

The results parsed from webscraper.py are stored in MSSQL Server 2017 database.

Before executing the code, you need to execute the webscraper.sql file to create the Db Schema.
Then you need to pass database username and password provide the necessary for MS SQL Server while executing webscraper.py as cmmand line arguments "python3 webscraper.py <username> <password>".

