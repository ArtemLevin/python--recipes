def nameTheFile(myString: str) -> str:
    myString =''.join(i.title() for i in myString.split(' '))
    return myString

print(nameTheFile('Sorting a list of dictionaries by a common dictionary'))