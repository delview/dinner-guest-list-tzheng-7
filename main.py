'''This program will take user input about dinner guests and print invitations for each person'''

# Create empty list
guest_list = []

# Greet user
username = input("\nHello! Hope you're having a great day <3\n\nWhat's your name?\n\n> ").strip().title()

# Ask user for # of guests they want to invite
num_of_guests = int(input(f"\nNice to meet you, {username}! How many guests would you like invitations to be generated for? \
(Please enter a valid whole number) \n\n> ").strip())

# Create loop that'll add names to list till max #
max_num_of_guests = num_of_guests # Track # of guests added

while max_num_of_guests > 0: # While max isn't reached yet
    new_guest = input("\nPlease enter the name of the person you would like to invite.\n\n> ").title().strip()
    guest_list.append(new_guest) # Add guest to list
    max_num_of_guests -= 1 # Track # of guests added

# Print invitation for each person
for i in range(len(guest_list)):
    guest_list.sort() # Print invites in aphabetical order
    print(f"\n\n--------------------------------------------------------------------------------------------------------------\
----------------------------------------\nYou're Invited!\n\nDear {guest_list[i]},\n\nI would love for you to join me for a \
delightful evening of good food and great company. Let’s share a meal and make some wonderful memories together.\n\nPlease let \
me know if you can make it. I look forward to seeing you there!\n\nWarmly,\n\n{username}\n--------------------------------------\
----------------------------------------------------------------------------------------------------------------")

# Ask user if they want to replace someone
replace = input("\nWould you like to replace anyone? [Y]es/[N]o\n\n> ").strip().lower()

# If yes, ask user for name of guest they want to replace & whom they want to replace them w
while replace == 'y':
    replaced_guest = input("\nPlease enter the name of the person you would like to replace.\n\n> ").title().strip()
    if replaced_guest in guest_list:
        guest_list.remove(replaced_guest)
        newguest = input(f"\nPlease enter the name of the person you would like to invite instead of {replaced_guest}.\n\n> ")\
            .title().strip()
        guest_list.append(newguest)
        for i in range(len(guest_list)): # Regenerate invitations
            guest_list.sort() # Print invites in aphabetical order
            print(f"\n\n--------------------------------------------------------------------------------------------------------------\
----------------------------------------\nYou're Invited!\n\nDear {guest_list[i]},\n\nI would love for you to join me for a \
delightful evening of good food and great company. Let’s share a meal and make some wonderful memories together.\n\nPlease let \
me know if you can make it. I look forward to seeing you there!\n\nWarmly,\n\n{username}\n--------------------------------------\
----------------------------------------------------------------------------------------------------------------")
        replace = input("\nWould you like to replace anyone? [Y]es/[N]o\n\n> ").strip().lower()
    else:
        print("\nSorry, that person is not on the list.")

# If no, exit program
while replace == 'n':
    print("\nHave a nice day <3\n")
    break