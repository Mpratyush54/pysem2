
def printinfinity(fromno , tono):
    if(fromno<tono):
        print(fromno)
        return printinfinity(fromno+1, tono)
printinfinity(50,100)