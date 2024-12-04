#Malachi Roker
#CSD325-T203
#12/3/2024
#100 Bottles of Beer

#Function for user input
def main():
    bottles = int(input("Please, enter number of bottles: "))
    countdown(bottles)
    print("Time to buy more bottles of beer!")

#While loop to count down
def countdown(bottles):
    while bottles > 0:
        #Check if the number of bottles is 1 and adjust lyrics accordingly
        if bottles == 1:
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
            print("Take one down and pass it around, 0 bottles of beer on the wall.")
        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down and pass it around, {bottles - 1} bottle(s) of beer on the wall.")
        bottles -= 1

#main() function calls the countdown() function and prints the reminder to buy more beer
if __name__ == "__main__":
    main()
    