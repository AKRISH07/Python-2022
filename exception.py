try:
    num = 10/0
    print(num)
except:
    print("Can't Divide by 0")

finally:
    print("Finally Block")
