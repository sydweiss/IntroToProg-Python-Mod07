# ------------------------------------------------- #
# Title: Assignment 07
# Description: Error Handling and Pickling
# ChangeLog: (Who, When, What)
# SWeiss,<05.31.2030>,Created Script
# ------------------------------------------------ #

import pickle
import sys

pick = ["onion", "carrot", "cucumber", "jalapeno"]
pickle.dump(pick, open("pickled", "wb"))

number = int(input("enter a number to try to see whats in my pickle jar: "))

try:
    file_to_open = "not_pickled"
    if(number % 2 == 0):
        file_to_open = "pickled"

    pickle_jar = pickle.load(open(file_to_open, "rb"))
    print(pickle_jar)
except Exception as e:
    print("You didn't pick the right number, try again next time!")

sys.exit(0)