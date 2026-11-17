input("Set a bit - OR turns it ON. press Enter")
print("  5=",bin(5)[2:])
print("  5 | 2 =", 5 | 2,"binary: ", bin(5 | 2)[2:])

input("Zero a bit - AND turns it off. press enter ")
print("  7 =", bin(7)[2:])
print("  7 & 5 =", 7 & 5,"binary: ", bin(7 & 5)[2:])

n = int(input("Enter a number(try 4 or 6): "))
guess = input("Is it a power of 2 (Yes/No): ")
input("Power of 2 - only one bit is ON.  Press Enter")
if n > 0 and (n &(n-1)) == 0:
    print(" ", n,"Binary", bin(n)[2:],"power of 2 your guess",guess)
else:
    print(" ", n,"binary:", bin(n)[2:],"not a power of 2 your guess", guess)
