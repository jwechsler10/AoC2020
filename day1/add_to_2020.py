def partOne(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == 2020:
                print(nums[i] * nums[j])

def partTwo(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if nums[i] + nums[j] + nums[k] == 2020:
                    print(nums[i] * nums[j] * nums[k])

def main():

    inputFile = open('input.txt', 'r')
    nums = []

    for line in inputFile:
        nums.append(int(line.strip()))   
    inputFile.close()

    partOne(nums)
    partTwo(nums)

if __name__ == "__main__":
    main()