class Node:

    def __init__(self, data, kids=None):
        self.data = data
        self.kids = None
        self.dad = None
        self.cost = None
        self.set_kids(kids)

    def set_kids(self, kids):
        self.kids = set_kids()
        if self.kids != None:
            for h in self.kids:
                h.dad = self

    def get_kids(self):
        return self.get_kids()

    def get_dad(self):
        return self.dad

    def set_dad(self, dad):
        self.dad = dad

    def set_data(self, data):
        self.data = set_data()

    def get_data(self):
        return self.data

    def set_cost(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost

    def equal(self, node):
        if self.get_datos() == node.get_data():
            return True
        else:
            return False

    def in_list(self, node_list):
        in_the_list = False
        for n in node_list:
            if self.equal(n):
                in_the_list = True
        return in_the_list

    def __str__(self):
        return str(self.get_data())

x = Node("Hello World")
x.data
