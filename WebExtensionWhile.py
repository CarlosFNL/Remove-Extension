def extension(string):
    index = len(string)-1
    out = False
    while out == False:
        if string[index]== ".":
            out = True
        else:
            index-=1
    return print("The extension of", string,"is equal to:",string[index:len(string)])
word = "hola.com"
example = ["hola.com","oye.rgb","como.lgt"]
print(extension(word))
def extensionSitios(example):
    for i,word in enumerate(example):
        extension(word)
print(extensionSitios(example))