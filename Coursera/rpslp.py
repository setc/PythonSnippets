# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# TODO: I'm pretty sure the two helper functions could be
# done in a more elegant way by using a dicionary. But alas,
# I have to type all this in the last hours before the
# deadline, so tried and true answers should be enough
# for now.
import random


def number_to_name(number):
    """
    Takes a number and returns the assigned name.
    """

    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print("Wrong input, number goes from 0 to 4")


def name_to_number(name):
    """
    Takes a the name and returns its assigned number.
    """
    #This function is so similar to the former that I
    #wonder if there is one way to not to repeat myself
    #Decorators, mabye?
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print("""Wrong input, valid strings are:
                 rock, Spock, paper, lizard, scissors""")


def rpsls(name):
    """
    This function takes the choice of the player for
    rock, paper, scissors, lizard, Spock and compare
    it with a choice made by the computer at random.
    """

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(5)

    # compute difference of player_number and comp_number modulo five
    result = (player_number - comp_number) % 5

    # use if/elif/else to determine winner
    if result == 1 or result == 2:
        winner = "Player wins!"
    elif result == 3 or result == 4:
        winner = "Computer wins!"
    elif result == 0:
        winner = "Player and computer tie!"

    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)

    # print results
    print("")
    print("Player chooses " + name)
    print("Computer chooses " + comp_name)
    print(winner)

# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# And that's all.
# NOTE: The format method for strings doesn't work in code skulptor.
# A pity.
