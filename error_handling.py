# x: int = None
# try: # try the dangerous code
#     x: int = int(input("enter a number: "))
# except: # protection net. catch the error
#     #do NOT crash.
#     #there was an error.
#     #handle the error.
#     print(f"{x} is not a valid number!")
# print (x)

height: float = 0
while True:
    try:
        height: float = float(input("enter height: "))
        if not 1.4 <= height<= 3.0:
            raise ValueError
        break
    except:
        print(f"{height} is not a valid height")

print ("success!")