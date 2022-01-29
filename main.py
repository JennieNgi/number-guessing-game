import random
import time

def getInput(counter, user_list):
        validated = False
        while (validated == False):
            # pass in the value of counter from main function
            num = input("Enter guess #"+ str(counter) + " between 1 and 100: ")
            # validate the input is a whole number
            if ( (num.isdigit() == False) ):
                print("***Invalid input..Please try again***") 
                # validate the number range
            elif ( (int(num) <= 0) or (int(num) > 100) ):
                print("***Invalid input..Must be in range of 1 to 100***") 
            # validate duplicate entry
            # pass in the value of user_list from main function
            # convert num to int as the element in user_list is int
            elif (int(num) in user_list):
                print("***Duplicate input..Please try again***")     
            else:
                # convert num from string to num for main() use
                num = int(num)
                # if pass the validation, stop the loop
                validated = True 
        # return num value to be used in main function
        return num

def main():
    # using the while loop to automatically restart the program 
    while(True):
        # create an empty list for storing userInput for validation
        user_list = []
        counter = 1
        # generate random number
        secretNum = random.randint(1,100)
        print(">>>>>>>>",secretNum)
        print("Number Guessing Game-------------------")
        
        while(counter < 11):
            # calling getInput()
            num = getInput(counter, user_list)
            # append the useinput to the list
            user_list.append(num)
            # print(user_list)
            if (num > secretNum):  
                print("Guess #%1s : %1s - Lower!" % (counter, num))
                print("---------------------------------------")   
                counter = counter + 1
            elif (num < secretNum):
                print("Guess #%1s : %1s - Higher!" % (counter, num))  
                print("---------------------------------------")   
                counter = counter + 1
            elif (num == secretNum):  
                print("Guess #%1s : %1s - Correct!" % (counter, num))  
                print("YOU WIN!") 
                # get out of the loop without shutting down the program
                break
    
        # the while loop will stop and print gameover message when the counter is larger than 10 attempts
        if (counter > 10):
            print("You lost and the game is over!") 
        
        time.sleep(2.0)
 
main()