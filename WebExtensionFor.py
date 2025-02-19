def extension(string):
    index = 0
    for i, letter in enumerate(string): 
        if letter== ".":
            index = i
    return print("The extension of", string,"is equal to",string[index:len(string)])
word = "hola.com"
example = ["hola.com","oye.rgb","como.lgt"]
print(extension(word))
def extensionList(example):
    for i,word in enumerate(example):
        extension(word)
print(extensionList(example))