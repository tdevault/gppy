


class gptree:
    ntset = ['+', '-', '*', 'pdiv', 'psqrt', '>', '<', 'if']

    children = None

    def __init__(self):
        self.children = []

    def numChild(self):
        return 1