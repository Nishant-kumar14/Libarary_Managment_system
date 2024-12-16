print("                                    Welcome To Skill Circle Library Managmeant System                               ")
print("Press 1 for 101 Book Info")
print("Press 2 for 102 Book Info")
print("Press 3 for 103 Book Info")
print("Press 4 for 104 Book Info")
print("Press 5 for 105 Book Info")


def happy():
    book=int(input("Select Your Book"))
    if(book==1):
        print("Book Title : Project Hail Mary")
        print("Book Author : Andy Weir")
        print("Book Price : $18.99")
        print("Book Launch Date : May 4, 2021")
        print("Book Description : A lone astronaut must save Earth from disaster in this gripping tale of science, survival, and humanity from the author of The Martian.")
    elif(book==2):
        print("Book Title : The Midnight Library")
        print("Book Author : Matt Haig")
        print("Book Price : $13.49")
        print("Book Launch Date : September 29, 2020")
        print("Book Description : Between life and death lies the Midnight Library, where every book represents a life you could have lived. A heartwarming exploration of regret, hope, and second chances.") 
    elif(book==3):
        print("Book Title : Atomic Habits")
        print("Book Author : James Clear")
        print("Book Price : $16.20")
        print("Book Launch Date :  October 16, 2018")
        print("Book Description : A practical guide to building good habits and breaking bad ones, offering insights into how tiny changes can lead to remarkable results.")
    elif(book==4):
        print("Book Title : Daisy Jones & The Six")
        print("Book Author : Taylor Jenkins Reid")
        print("Book Price :  $14.99")
        print("Book Launch Date :  March 5, 2019")
        print("Book Description : A novel about the rise and fall of a fictional 1970s rock band, told through a series of interviews. The story reveals the drama, love, and heartbreak behind the music.")
    elif(book==5):
        print("Book Title : Circe")
        print("Book Author : Madeline Miller")
        print("Book Price :  $15.90")
        print("Book Launch Date :   April 10, 2018")
        print("Book Description : A reimagining of Greek mythology, this novel follows the life of Circe, a goddess with a mortal’s voice, as she finds her strength and defies the gods.")
    else:
        print("invalid Number press")
    choose=int(input("press 1 for continue or 2 for exit"))
    if choose==1:
            print("continue")
            choose=happy()
    elif choose==2:
            print("Thank you for Visiting SCLMS")
    else:
        print("invalid Number press")
happy()
