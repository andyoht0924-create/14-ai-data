def add(a, b):
    print("__name__", __name__)
    return a + b

def sub(a, b):
    print("__name__", __name__)
    return a - b

# if __name__ == "__main__"의 의미
# print("__name__", __name__)

if __name__ == "__main__":
    print(add(3, 4))
    print(sub(4, 2))