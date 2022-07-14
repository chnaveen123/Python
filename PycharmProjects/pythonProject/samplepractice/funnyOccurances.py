def extractSecreteMessage(str,sub):
    str = str.replace(sub,"")
    return str.strip()
str = input("")
sub = input("")
print(extractSecreteMessage(str,sub))