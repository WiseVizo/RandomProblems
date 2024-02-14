#Given an array of N non-negative integers arr[] representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# source -> https://www.geeksforgeeks.org/trapping-rain-water/

# myArr = [2, 0,0, 0, 2]
myArr = [3, 0, 2, 0, 4]

def CountWaterBlocks(arr):
    """
    arr -> array of int representing an elevation map 
    returns -> int 
    """

    startBlockHeight = False
    endBlockHeight = False
    totalWaterBlocks = 0
    waterBlockCount = 0
    for block in arr:
        if not startBlockHeight and block!=0:
            startBlockHeight = block
            print("s: ",startBlockHeight)
            continue
        if not endBlockHeight and block!=0:
            endBlockHeight = block
            print("e: ",endBlockHeight)
            if endBlockHeight > startBlockHeight:
                waterBlockCount *= startBlockHeight
            else:
                waterBlockCount *= endBlockHeight
            startBlockHeight = endBlockHeight
            endBlockHeight = False
            print("w: ", waterBlockCount)
            totalWaterBlocks += waterBlockCount
            waterBlockCount = 0
            print("tw: ", totalWaterBlocks)
            print("new: ",startBlockHeight)
            continue
        if block == 0 and startBlockHeight and not endBlockHeight:
            waterBlockCount += 1

    return totalWaterBlocks

print(f'WaterBlocksCount: {CountWaterBlocks(myArr)}')
# umm i was going to make a class for water block for storing its height and index in arr togethere and this code can't calculate water blocks correctly if Start > end < next end