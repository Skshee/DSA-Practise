def timeConversion(s):
    if(s[-2:]=='PM'):
        if(s[:2]=="12"):
            return s[:-2]
        else:
            return str(int(s[:2])+12) + s[2:-2]
    elif(s[-2:]=='AM'):
        if(s[:2]=="12"):
            return "00" + s[2:-2]
        else:
            return s[:-2]