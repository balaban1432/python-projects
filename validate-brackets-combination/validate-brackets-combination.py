
combination = input('Write a string that contains only `(`, `)`, `{`, `}`, `[` and `]`: ')

def isValid(par):
    bracket_map = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    openP = {"(", "[", "{"}
    stack = [] 
    for el in par: 
        if el in openP:
            stack.append(el)
        elif el == bracket_map[stack[-1]]: 
            stack.pop()
        else:
            return False
    return stack == [] 


print(isValid(combination))
