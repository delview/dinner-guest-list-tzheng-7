'''This program will take user input about dinner guests and print invitations for each person'''

# Create empty list
guestlist = []

# Greet user
username = input("\nHello! Hope you're having a great day <3\n\nWhat's your name?\n\n> ").strip().title()

# Ask user for # of guests they want to invite
numofguests = int(input(f"\nNice to meet you, {username}! How many guests would you like invitations to be generated for? (Please enter a valid whole number) \n\n> ").strip())

# Create loop that'll add names to list till max #
maxnumofguests = numofguests # Track # of guests added

while maxnumofguests > 0: # While max isn't reached yet
    newguest = input("\nPlease enter the name of the person you would like to invite.\n\n> ").title().strip()
    guestlist.append(newguest) # Add guest to list
    maxnumofguests -= 1 # Track # of guests added

# Print invitation for each person
for guest in guestlist:
    print(f"\n\nYou're Invited!\n\nDear {guest},\n\nI would love for you to join me for a delightful evening of good food and great company. Let’s share a meal and make some wonderful memories together.\n\nPlease let me know if you can make it. I look forward to seeing you there!\n\nWarmly,\n\n{username}\n")

# Ask user if they want to replace someone

# If yes, ask user for name of guest they want to replace & whom they want to replace them w

# Regenerate invitations

# If no, exit program