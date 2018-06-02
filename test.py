def firstNotRepeatingCharacter(s):
    tmpMap = dict()
    tmpValue = '_'
    tmpValue2 = '_'
    for i in s:
        if i in tmpMap:
            tmpMap[i] += 1
        else:
            tmpMap[i] = 1
            tmpValue2 = i
            if tmpValue == '_':
                tmpValue = i
            elif tmpMap[tmpValue] > 1:
                tmpValue = i


    if tmpMap[tmpValue] > 1:
        if tmpMap[tmpValue2] < 2:
            return tmpValue2

        return '_'

    return tmpValue


print(f"abcdba: {firstNotRepeatingCharacter('bcb')}")
