import random

class node:
    type = 0 #0 for non terminal, 1 for terminal
    value = None
    children = None

class gptree:
    NonTerminalSet = ['+', '-', '*', 'pdiv', 'psqrt', '>', '<', 'if']
    TerminalSet = ['zero', 'one', 'negone', 'ten', 'pi', '2pi', 'pone']
    Root = None

    def __init__(self, maxdepth):
        self.ramped(0, maxdepth, self.Root)

    def ramped(self, currentdepth, maxdepth, n):
        if n is None:
            n = node()
            if maxdepth == 0:
                n.value = random.choice(self.TerminalSet)
            else:
                n.value = random.choice(self.NonTerminalSet)
                while currentdepth < maxdepth:
                    for i in range(self.getArrity(self.Root)):
                        self.

    def tostring(self):

    def numChild(self, n):
        if n.children is None:
            return None
        else:
            return len(n.children)

    def getArrity(self, n):
        if n.value == '+':
            return 2
        elif n.value == '-':
            return  2
        elif n.value == '*':
            return  2
        elif n.value == 'pdiv':
            return  2
        elif n.value == 'psqrt':
            return  1
        elif n.value == '>':
            return  2
        elif n.value == '<':
            return  2
        elif n.value == 'if':
            return  3
    def count(self):
        return 0
