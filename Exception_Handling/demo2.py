def function(num):
    try:
        if num % 2 == 0:
            raise ValueError("The number is even!")
        else:
            print("Oh nooo! The number is odd!")
    except ValueError as e:
        print(f"Exception caught: {e}")
function(4)
function(3)
