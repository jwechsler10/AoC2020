

'''
X: 1, Y: 1, Trees: 90
X: 3, Y: 1, Trees: 244
X: 5, Y: 1, Trees: 97
X: 7, Y: 1, Trees: 92
X: 1, Y: 2, Trees: 48
Total Trees:  9406609920
'''

def main():
    #totalRows = 30
    #totalColumns = 322
    # totalRows = 65
    # totalColumns = 10
    treesEncountered = 0

    #currentRow = 0
    #currentColumn = 0

    with open('input.txt', 'r') as input:
        pattern = [[char for char in line.strip()] for line in input]

#    print(pattern)
    col = 0
    for row in pattern[1:]:
        col += 3
        if row[col%len(row)] == "#":
            treesEncountered += 1
    # while currentColumn < totalColumns and currentRow < totalRows:
    #     #print("position before equals ({}, {}) at {}".format(currentColumn, currentRow, pattern[currentColumn][currentRow]))

    #     currentColumn += 1
    #     currentRow += 3

    #     #print("current row is {}".format(currentRow))

    #     if pattern[currentColumn][currentRow%len(pattern[currentColumn])] == "#":
    #         treesEncountered += 1
        
    #     #if currentRow >= totalRows:
    #         #print("x is greater than 30, too far right... Moving back to 0")
    #         #currentRow = currentRow % totalRows
    #     #print("position now is ({}, {}) at {}".format(currentColumn, currentRow, pattern[currentColumn][currentRow]))

    
    print(treesEncountered)


if __name__ == "__main__":
    main()