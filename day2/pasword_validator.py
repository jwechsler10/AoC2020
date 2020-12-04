import string

def main():

    inputFile = open('input.txt', 'r')
    validPasswords = 0

    for line in inputFile:
        charCount = 0
        splitLine = line.split(":")
        hyphenSplit = line.split("-")
        spaceSplit = hyphenSplit[1].split(" ")
        lowerBound = int(hyphenSplit[0].strip())
        chartoContain = splitLine[0][len(splitLine[0]) - 1]
        upperBound = int(spaceSplit[0].strip())
        password = spaceSplit[2].strip()

        ##################### validation for first

        # print("line {} password {} needs to contain {} at least {} time(s) and at most {} time(s)".format(line, password, chartoContain, lowerBound, upperBound))

        # for char in password:
        #     if char == chartoContain:
        #         charCount += 1
        # if charCount >= lowerBound and charCount <= upperBound:
        #     validPasswords += 1 

        ###################### validation for second

        firstIndex = lowerBound - 1 
        secondIndex = upperBound - 1

        print("line {} password {} needs to contain {} at position {} or at position {} ".format(line, password, chartoContain, firstIndex, secondIndex))


        if (password[firstIndex] == chartoContain or password[secondIndex] == chartoContain) and (password[firstIndex] != password[secondIndex]):
            print(password)
            validPasswords += 1

    print("number of valid passwords is: {}".format(validPasswords))
        

if __name__ == "__main__":
    main()