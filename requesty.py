#!/usr/bin/python3
import requests

def main():
    # HTTP GET the dataset
    satellites = requests.get("http://www.celestrak.com/NORAD/elements/active.txt")

    # the data was returned as a single string
    # split the data across "\r\n" boundaries
    satellites = satellites.text.split("\r\n")

    # create a list to store satellite names in
    satellitenames = []

    # create a counter for looping across lines
    linecount = 0
    # loop through the lines within the txt file
    for satellite in satellites:
        # if this is true than the line is divisible by 3
        if linecount%3 == 0:
            # remove whitespace from around human name
            satellite = satellite.strip()
            # the very last line is empty and always is added to the list
            # to prevent this, we only add the name if it is not blank
            if satellite is not "":
                # add satellite names to our list of names
                satellitenames.append(satellite)
        # increase the counter by 1
        linecount += 1


    # display the list of satellites
    print(satellitenames)
    # display some stats
    print(f"\nThe number of satellites tracked is {len(satellitenames)}")
    new_names = []
    for name in satellitenames:
        new_names.append(f"{name}\n")

    with open("satellites_names.txt", "w") as fi:
        #fi.write(str(satellitenames))
        fi.writelines(new_names)



if __name__ == "__main__":
    main()

