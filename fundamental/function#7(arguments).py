def net_price(price, discount =0, tax = 0.08):
    return price * (1-discount) * (1+tax)

print(f"The price is: ${net_price(500,0.3)}")

import time
# default argument
def countTime(end, start=0):
    for second in range(start, end+1):
        print(second)
        time.sleep(1)
    print("Time up!")

countTime(10)

# keyword argument
def greeting(greet, title, firstName, lastName):
    print(f"{greet}, {title}.{firstName}{lastName}")

greeting("Hello", firstName="Jhon", lastName="James", title="Mr")

def phoneNumber(country, area, first, last):
    return f"+{country}({area})-{first}-{last}"

myNumber = phoneNumber(country=1, area=650, first=456, last=7890)
print(myNumber)

# arbitrary argument, *args

def sum(*args):
    sum=0
    for arg in argus:
        sum += arg
    return sum
print(sum(7, 9, 10, 21))

def displayName(*args):
    for arg in args:
        print(arg, end=" ")
displayName("Jin", "Yu", "Cloud", "Underraining", "Liu", "VI")

# arbitrary argument, **kwargs

def displayAddress(**kwargs):
    for key, value in kwargs.items():  # for key in kwargs.keys():    for value in kwargs.values():
        print(f"{key}: {value}")
displayAddress(street="Gold",
               city="New York",
               state="New York",
               zip=11000)

def shipping(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping("Jin", "Yu", "Cloud", "Underraining", "Liu", "VI",
         street="Gold",
         city="New York",
         state="New York",
         zip=11000)
