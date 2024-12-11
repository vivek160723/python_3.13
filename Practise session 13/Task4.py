fruits = {
    "apple": 120,
    "banana": 30,
    "cherry": 250,
    "date": 300,
    "elderberry": 500
}
try:
    fruit_name = input("Enter the name of the fruit: ").lower()
    price = fruits[fruit_name]
    print(price)
except KeyError:
    print("Sorry , this fruit dont exist")