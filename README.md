# comp9321-assignment1

**Overview**
In this assignment, you will be given some ‘real experience’ on your week 1-2 lecture content. You are
asked to make some CRUD(create,read,update and delete) operations to the data-set which we provided.
After finish this assignment you should have some idea about how to do data ingestion,cleansing and
manipulation on a small-size data-set(less than 5MB). In this assignment, we will work on the data
which from Barcelona.


**Tasks**
Question 0.
(0 mark)

Download the zip file a1.zip which contain a python code template a1.py and a few csv files: Do not
change the file name.

Noted:
• For assessment reason, printed data in table rows should be separated by one single space;
• Some inconsistent names in files don’t need to be changed in this assignment(e.g. Sant Martı́
and Sant Marti, also Horta-Guinardó and Horta-Guinardo, ”Meridiana” and ”Av Meridiana”);
• Names like ARAGÓ shall be converted to Aragó ;
• Names in dataset may be in BLOCK LETTERS(Upper cased) or lower cased, they should be
corrected to Title Style, except for “la”, “de”, “d 0 ” and “l 0 ”. e.g. “El Camp de l 0 Arpa Del Clot” ;
• Multiple street values shall not be changed and be kept as it is;
• For Q2 - Q5, invalid data like “Unknown”, “–” shall be removed;
• In Q4, you need only match by hour, day, month and district names of stations and accidents;
You can assume all data are in the same year; Accident outside the range of air stations can be
ignored;
• Sample testing for Q1 and Q3 is updated; We are planning an update sample testing and release
a less buggy version for Q4 part 1,2;
• Human review will be involved in terms of final marking for this assignment, which means some
formatting disagreement in the sample auto testing will still be marked right.
