class Passport:

    def __init__(self, birthYear, issueYear, expirationYear, height, hairColor, eyeColor, passportId, countryId=None):
        self.birthYear = birthYear
        self.issueYear = issueYear
        self.expirationYear = expirationYear
        self.height = height
        self.hairColor = hairColor
        self.eyeColor = eyeColor
        self.passportId = passportId
        self.countryId = countryId
    
    def __str__(self):
        return "birthYear: " + str(self.birthYear)  + " issueYear: " + str(self.issueYear) + " expirationYear: " + str(self.expirationYear) + " height: " + str(self.height) + " hairColor: " + str(self.hairColor) + " eyeColor: " + str(self.eyeColor) + " passportID: " + str(self.passportId) + " countryID: " + str(self.countryId)
    
    def isValid(self):
        if not self.validateBirthYear():
            return False 
        if not self.validateIssueYear():
            return False
        if not self.validateExpirationYear():
            return False
        if not self.validateHeight():
            return False
        if not self.validateHairColor():
            return False
        if not self.validateEyeColor():
            return False
        if not self.validatePassportId():
            return False

        return True

    def validateBirthYear(self):
        if self.birthYear is None or (int(self.birthYear) < 1920 or int(self.birthYear) > 2002) or len(self.birthYear) != 4:
            print("invalid birthYear is " + str(self.birthYear))
            return False 
        return True
    
    def validateIssueYear(self):
        if self.issueYear is None or (int(self.issueYear) < 2010 or int(self.issueYear) > 2020) or len(self.issueYear) != 4:
            print("invalid issue year is " + str(self.issueYear))
            return False
        return True
    
    def validateExpirationYear(self):
        if self.expirationYear is None or (int(self.expirationYear) < 2020 or int(self.expirationYear) > 2030) or len(self.expirationYear) != 4:
            print("invalid expiration year is " + str(self.expirationYear))
            return False
        return True
    
    def validateHeight(self):
        if self.height is None or (not self.height.endswith("in") and not self.height.endswith("cm")):
            print("invalid height is " + str(self.height))
            return False
        if self.height.endswith("in"):
            rawHeight = int(self.height.split("in")[0])
            if rawHeight < 59 or rawHeight > 76:
                print("invalid height is " + str(rawHeight))
                return False
        if self.height.endswith("cm"):
            rawHeight = int(self.height.split("cm")[0])
            if rawHeight < 150 or rawHeight > 193:
                print("invalid height is " + str(rawHeight))
                return False
        return True
    
    def validateEyeColor(self):
        validEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if self.eyeColor is None or self.eyeColor not in validEyeColors:
            print("invalid eye color is " + str(self.eyeColor))
            return False
        return True
    
    def validatePassportId(self):
        if self.passportId is None or len(self.passportId) != 9 or not self.passportId.isnumeric():
            print("invalid passport ID is " + str(self.passportId))
            return False
        return True
    
    def validateHairColor(self):
        validChars = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if self.hairColor is None or (not self.hairColor.startswith("#") and len(self.hairColor) != 7):
            for char in str(self.hairColor):
                if char not in validChars:
                    print("invalid hair color is " + str(self.hairColor))
                    return False
            print("invalid hair color is " + str(self.hairColor))
            return False
        return True
        

def validatePassports(passports):
    validPassports = 0

    for passport in passports:
        passportFields = passport.split(" ")
        birthYear = None
        issueYear = None
        expirationYear = None
        height = None
        hairColor = None
        eyeColor = None
        passportId = None
        countryId = None
        for field in passportFields:
            values = field.split(":")
            key = values[0]
            value = values[1]
            if key == "byr":
                birthYear = value
            if key == "iyr":
                issueYear = value
            if key == "eyr":
                expirationYear = value 
            if key == "hgt":
                height = value
            if key == "hcl":
                hairColor = value
            if key == "ecl":
                eyeColor = value
            if key == "pid":
                passportId = value 
            if key == "cid":
                countryId = value
                
        passportObj = Passport(birthYear, issueYear, expirationYear, height, hairColor, eyeColor, passportId, countryId)
        if passportObj.isValid():
            validPassports += 1
    
    return validPassports
                

def main():

    passports = []
    passport = ''

    with open('input.txt', 'r') as input:
        split = input.read().splitlines()

    for i in range(len(split)):

        if split[i] == '':
            passports.append(passport.strip())
            passport = ''
        if ' ' in split[i]:
            passport += split[i].strip() + ' '
        else:
            passport += split[i].strip() + ' '
        if i == len(split) - 1:
            passports.append(passport.strip())

    print("Number of valid passports: {} ".format(validatePassports(passports)))

if __name__ == "__main__":
    main()