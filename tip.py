def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars*percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    m=""
    for i in range (1,len(d)):
        m = m+d[i]
    g=float(m)
    return g

def percent_to_float(p):
    l=""
    for i in range (0,2):
        l=l+p[i]
    z=float(l)/100
    return z

main()