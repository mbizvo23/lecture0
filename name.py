#name = input()
#print(f" My name is {name}")
#x=int(input("Enter a number: "))
#if x>0:
#    print("X is positive")
#elif x < 0:
 #   print("X is negative")
#else:
 #   print(" X is equal to zero")
def square(x):
    return x*x
def main():
    for i in range(10):
        print("{} squared is {}".format(i,square(i)))

if __name__=="__main__":
    main()

