zero      = "+[]"
zeroth    = "[+[]]"
openPar   = "["
closePar  = "]" + zeroth
undefined = "[]" + zeroth
zeroStr   = openPar + zero + closePar

class Digit:
    cache = {}
    def __call__(self, char):
        if not char in self.cache:
            dig = int(char)
            self.cache[char] = openPar + ("++" + openPar) * dig + zero + closePar * dig + closePar
        return self.cache[char]
digit = Digit()

e    = openPar + "[]+" + undefined + closePar + "[" + digit(3) + "]"
dot  = openPar + "[]+" + openPar + "+" + openPar + "[]+" + "+".join([digit(1), digit(1), e, digit(1), zeroStr, zeroStr]) + closePar * 3 + "[" + digit(1) + "]"
neg  = openPar + "[]+" + openPar + "+" + openPar + "+".join([dot] + [zeroStr] * 6 + [digit(1)]) + closePar * 3 + "[" + digit(2) + "]"

def convert(num):
    num = str(num)
    out = ["[]"]
    for char in num:
        if char.isdigit():
            out.append(digit(char))
        elif char == ".":
            out.append(dot)
        elif char == "-":
            out.append(neg)
            
    return "+[" + "+".join(iter(out)) + "]"

if __name__ == "__main__":
    while True:
        out = convert(input("Your Number: "))
        print(out)
    
            
            
