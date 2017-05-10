# Forsta
All of these are steps to a bottom up approach that eventually gets to democratization of database SME knowledge, and maybe even semantic querying of databases. At the end of the day, giving people to go into a fucked sideways SAP or other transactional system to ask questions without having to go to an analyst, data architect, solution architect, or other professional. Cutting out the middleman, and make people/companies data usable.

#Plan
The intent was to create something with the following features by 3/31/2017:

1. Read in logs
2. Define that tables are related (just tables, not columns)
3. Output this information into a format that can be consumed by a reporting tool (csv?).

After that first initial release of the MVP, the next step would be to do the following by 4/20/2017 (hehehe):

1. Create the solution so that it can be installed as a .exe
2. Create a website that links to the solution and allows users to download/request info.
3. Setup a way for people to pay/donate money (whatever we decide to do).
With that, I think that will be enough for a minimum viable product. The user would download the tool, hit the database logs with said tool, then WHAM! What tables are related to what tables.

Future:

1. Define how the tables are links (what is the SQL joining on?)
2. Define common calculations?
3. Automated way of finding where these queries are used (reporting field to database calculation)?