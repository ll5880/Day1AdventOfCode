
def calibrate(inputfile: str):
    list = []
    calvalue = ""
    # open input file
    file = open(inputfile, "r")
    # read line by line
    for line in file:
        # finds the 1st digit in the line
        # could be a letter
        for char in line:
            if char.isdigit():
                calvalue += char
                break
        # reverse the line
        line = line[::-1]

        # finds the 2nd digit in the line
        for char in line:
            if char.isdigit():
                calvalue += char
                break

        # puts the calvalue in the list
        list.append(calvalue)
        calvalue = ""

    # loop through the list and add all the values together
    answer = 0
    for value in list:
        answer += int(value)

    print(answer)


def main():
    calibrate("input.txt")
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
