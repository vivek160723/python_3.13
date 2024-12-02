class Counter:
    count = 0

    @classmethod
    def create_object(cls):
        cls.count += 1
        print("Total objects created:", cls.count)
        return cls()


# Example usage
obj1 = Counter.create_object()  # Create first object
obj2 = Counter.create_object()  # Create second object
obj3 = Counter.create_object()  # Create third object
