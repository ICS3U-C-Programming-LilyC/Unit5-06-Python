#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Dec/6/2023
# This program gets a decimal from the user
# along with how many decimal places they
# would like to round to and rounds their number accordingly.


# Using round_decimal function to round decimal.
def round_decimal(num_array, dec_places):
    num_array[0] = num_array[0] * (10**dec_places)
    num_array[0] += 0.5
    num_array[0] = int(num_array[0])
    num_array[0] = num_array[0] / (10**dec_places)


def main():
    # Explaining my program to the user.
    print(
        "This program will round your decimal to the number of decimal places of your choice."
    )

    # Declaring list.
    number_user = []

    # Getting user input for decimal and number of decimal places.
    dec_num_as_string = input("Enter a decimal number: ")
    dec_place_as_string = input("Enter a number of decimal places: ")

    # Using a try catch to catch any errors.
    try:
        # Converting the decimal entered from a string to a float.
        # Converting the number of decimal places to round to as an integer.
        dec_num_as_float = float(dec_num_as_string)
        dec_places_as_int = int(dec_place_as_string)

        # Adding the user's input to the list.
        number_user.append(dec_num_as_float)

        # Using an if statement to check if the number entered for decimal places is
        # negative.
        if dec_places_as_int < 0 or dec_num_as_float < 0:
            print(
                "This is a negative integer. Please use positive integers only."
                )

        # Else the integer of decimal places is greater than 0.
        else:
            # Calling function to round the number.
            round_decimal(number_user, dec_places_as_int)

            # Printing the rounded number.
            print("Your rounded number is {}".format(number_user[0]))

        # Catching any errors.
    except:
        print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
