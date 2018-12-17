print("HELLO PYthon We are going to start")

mystring = "Hello"
myint: int = 10
myfloat: float = 20.0
mybool = False

if mybool:
    print("My Bool is true")
else:
    print("My Bool is false")

    if isinstance(myint, int) and myint == 10:
        print(f"My Interger Value is : %d" %myint)

    if isinstance(myfloat, float) and myfloat == 20.0:
        print("My Float value is : %f" %myfloat)

    if isinstance(mybool, bool):
        print("Hello")

        exit(0)