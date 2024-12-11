class InvalidAgeException(Exception):
    pass

def check_value(value):
    if value < 18:
        raise InvalidAgeException("For 18+ only!!")
    else:
        print("U Are Good to Go")

try:
    num=int(input("Enter u Age:"))
    check_value(num)
except InvalidAgeException as e:
    print(e)

