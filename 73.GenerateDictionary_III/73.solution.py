
def generateDictionary(nn):
    if len(nn)==0:
        return {}
    return {nn[0]:generateDictionary(nn[1:])}

nn = input().split()

print(generateDictionary(nn))

