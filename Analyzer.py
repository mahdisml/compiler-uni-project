class Analyzer:
    rawData = ""
    correctedData = ""
    tokens = []
    state = 0
    stack = ""

    # identifier letter
    # identifier digit
    # number
    # reserved word
    # symbol
    # string
    # meta statement

    # states =
    # 1: digit
    # 2:  # or '/'
    # 3: "
    # 4: all
    # 5: number

    def get_from_file(self, path):
        f = open(path, "r")
        self.rawData = str(f.read())
        f.close()

    def get_from_string(self, text):
        self.rawData = text

    def correcting(self):
        self.correctedData = self.rawData.replace(" ", "")
        self.correctedData = list(self.correctedData)

    def dfa(self, char):
        if self.state == 0:
            if char[0].isnumeric():
                self.state = 1
                return 0
            elif char[0] == "#" or (char[0] == "/" and char[1] == "/"):
                self.state = 2
                if char[0] == "#":
                    return 1
                else:
                    return 2
            elif char[0] in "\"":
                self.state = 3
                return 1
            else:
                self.state = 4
                return 0
        elif self.state == 1:
            if char[0].isnumeric():
                self.state = 1
                self.stack = self.stack + str(char[0])
            else:
                self.state = 0
                if len(self.stack) > 0:
                    self.tokens.append(["number", self.stack])
                else:
                    self.tokens.append(["identifier digit", self.stack])
                self.stack = ""
                return 0
        elif self.state == 2:
            if char[0] in "\n":
                self.state = 0
                self.tokens.append(["meta statement", self.stack])
                self.stack = ""
                return 1

            else:
                self.state = 2
                self.stack = self.stack + str(char[0])
        elif self.state == 3:
            if char[0] in "\"":
                self.state = 0
                self.tokens.append(["string", self.stack])
                self.stack = ""
            else:
                self.state = 3
                self.stack = self.stack + str(char[0])
        elif self.state == 4:
            if len(char) > 2 and char[0] + char[1] in "if":
                self.tokens.append(["reserved word", char[0] + char[1]])
                self.state = 0
                return 2
            if len(char) > 3 and char[0] + char[1] + char[2] in "int":
                self.tokens.append(["reserved word", char[0] + char[1] + char[2]])
                self.state = 0
                return 3
            if len(char) > 4 and char[0] + char[1] + char[2] + char[3] in "void read":
                self.tokens.append(["reserved word", char[0] + char[1] + char[2] + char[3]])
                self.state = 0
                return 4
            if len(char) > 5 and char[0] + char[1] + char[2] + char[3] + char[4] in "while write print break":
                self.tokens.append(["reserved word", char[0] + char[1] + char[2] + char[3] + char[4]])
                self.state = 0
                return 5
            if len(char) > 6 and char[0] + char[1] + char[2] + char[3] + char[4] + char[5] in "return binary":
                self.tokens.append(["reserved word", char[0] + char[1] + char[2] + char[3] + char[4] + char[5]])
                self.state = 0
                return 6
            if len(char) > 7 and char[0] + char[1] + char[2] + char[3] + char[4] + char[5] + char[6] in "decimal":
                self.tokens.append(["reserved word", char[0] + char[1] + char[2] + char[3] + char[4] + char[5] + char[6]])
                self.state = 0
                return 7
            if len(char) > 8 and char[0] + char[1] + char[2] + char[3] + char[4] + char[5] + char[6] + char[7] in "continue":
                self.tokens.append(["reserved word", char[0] + char[1] + char[2] + char[3] + char[4] + char[5] + char[6] + char[7]])
                self.state = 0
                return 8
            if len(char) > 1 and char[0] + char[1] in "( ) { } [ ] , ; + - * / == != > >= < <= = && ||":
                self.tokens.append(["symbol", char[0] + char[1]])
                self.state = 0
                return 2
            elif char[0] in "( ) { } [ ] , ; + - * / == != > >= < <= = && ||":
                self.tokens.append(["symbol", char[0]])
                self.state = 0
            elif char[0] == "#" or (char[0] == "/" and char[1] == "/"):
                self.state = 2
                return 2
            elif char[0] in "\"":
                self.state = 3
                return 1
            elif char[0].isnumeric():
                self.state = 1
                return 0
            else:
                self.tokens.append(["identifier letter", char[0]])
        else:
            print("ERROR : UNEXPECTED STATE")
        return 1

    def analyzing(self, text):
        temp = text
        for i in range(self.dfa(temp)):
            temp.pop(0)
        if len(temp) == 0:
            print("THE END")
        else:
            self.analyzing(temp)

    def analyze(self):
        self.correcting()
        temp = self.correctedData.copy()
        self.analyzing(temp)

    def save(self):
        f = open("2.txt", "w+")
        f.write(str(self.tokens))
        f.close()
        print("wrote in 2.txt")

    def show(self):
        print(str(self.tokens))
