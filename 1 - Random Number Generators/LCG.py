'''
Craig Langford

This is a basic Linear Congruential Generator which creates pseudo-random numbers
based on the equation X_(n+1) = (aX_n + c) (mod m) utilizing seed values from the
time.
'''

from time import gmtime, strftime

# Second convert date and time into usable values

day = int(strftime("%d"))
month = int(strftime("%m")) # month is a number this time
year = int(strftime("%Y"))
hour = int(strftime("%H"))
minute = int(strftime("%M"))
second = int(strftime("%S"))

m = year   # > 0
a = year - day    # 0 < a < m
c = year - day - month - hour   # 0 <= c < m
x_0 = year - day - month - hour - minute - second # 0 <= x_0 < m

x_new = (a*x_0 + c) % m

print x_new
