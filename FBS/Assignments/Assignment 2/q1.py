# Convert the time entered in hh,min and sec into seconds.
h=int(input("Enter the hours:"))
m=int(input("Enter the minutes:"))
s=int(input("Enter the seconds:"))
h2s=h*3600
m2s=m*60
ts=h2s+m2s+s
print(f"The total time in seconds is {ts}.")