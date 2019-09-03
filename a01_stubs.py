######################################################################
# Author: Micheala Jackson      TODO: Change this to your name
# Username: jacksonmic            TODO: Change this to your username
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
# TODO Ask user for their birth year

my_input = int(input('what is your birth year?'))
print(my_input)



# TODO Check the year using if conditionals, and print the correct animal for that year.
# See the a01_pets.py for examples
if my_input == int(1996):
  print("Your chinese zodiac is a rat")
if my_input == int(1997):
   print("Your chinese zodiac is an ox")
if my_input == int(1998):
   print("Your chinese zodiac is a tiger")
if my_input == int(1995):
   print("Your zodiac is a pig")
if my_input == int(1994):
   print("Your zodiac is a dog")
if my_input == int(1993):
   print("Your zodiac is rooster")
if my_input == int(1992):
   print("Your zodiac is a monkey")
if my_input == int(1991):
    print("Your zodiac is a goat")
if my_input == int(1990):
    print("Your zodiac is a horse")
if my_input == int(1989):
    print("Your zodiac is a snake")
if my_input == int(1988):
    print("Your zodiac is a dragon")
######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year


# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year


######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between
