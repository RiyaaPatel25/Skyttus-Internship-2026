#Write a program to calculate the diffrence between two dates

from datetime import date 

d1 = date(2026,1,2)
d2 = date(2026,2,2)

diff = d2 - d1
print("Difference in days : " ,diff.days)