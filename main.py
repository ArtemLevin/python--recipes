def nameTheFile(myString: str) -> str:
    myString =''.join(i.title() for i in myString.split(' '))
    return myString

print(nameTheFile('grouping records based on fields'))