import re
import pyperclip


# string = """function easeInOutQuad(x: number): number {
# return x < 0.5 ? 2 * x * x : 1 - pow(-2 * x + 2, 2) / 2;
# }""".replace("\n", '')
string = pyperclip.paste().replace("\n", '').replace("\r", '')

functionName = re.findall(r"function (.*?)\(", string)[0]
functionName = functionName[0].upper() + functionName[1:]

mathBody = re.findall(r"return (.*?);", string)[0]
mathBody = mathBody.replace("sin", "math.sin")\
                    .replace("cos", "math.cos")\
                    .replace("PI", "math.pi")\
                    .replace("pow", "math.pow")\
                    .replace("sqrt", "math.sqrt")\
                    .replace("===", "==")
        # .replace("sin", "math.sin")\
        # .replace("sin", "math.sin")\
        # .replace("sin", "math.sin")\

pyperclip.copy(mathBody)


while ":" in mathBody:
    triExp = re.findall(r"(.*?)\?(.*?):(.*?)$", mathBody)[0]

    mathBody = f"""{triExp[1].strip()} if {triExp[0].strip()} else {triExp[2].strip()}"""
result = f"""

class {functionName}(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return {mathBody}
        else:
            return self.target     
"""

print(result)

with open("ef.py", "a") as f:
    f.write(result)

