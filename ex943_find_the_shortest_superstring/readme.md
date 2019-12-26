Given a list of strings, the superstring can be constructed such that each string is a substring of it.
To get the shortest supersting, we may consider the ordering in which adjacent strings overlap for some characters

create a table:
Each row/column represents each string
Each element represents the number of overlapping characters between the column string and row string.
For example, A('gcta', 'ctaagt') = 3

After constructing the table, we begin with the pair with the greatest overlapping, then append the string one by one to maximize the overlapping.

Multiple paths may be present. 

