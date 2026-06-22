hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
def computepay():
    if h>40:
        a = 40*r+(h-40)*r*1.5
        return a
    else:
        b = h*r
        return b
p = computepay()
print("Pay:", p)