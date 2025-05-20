def plusMinus(arr):
    # Write your code here
    posCount=0
    negCount=0
    zeroCount=0
    for i in arr:
        if i>0:
            posCount+=1
        elif i<0:
            negCount+=1
        else:
            zeroCount+=1
    posRatio = posCount/len(arr)
    negRatio = negCount/len(arr)
    zeroRatio = zeroCount/len(arr)
        
    print(posRatio)
    print(negRatio)
    print(zeroRatio)