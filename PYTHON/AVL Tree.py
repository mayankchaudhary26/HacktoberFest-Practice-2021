# A basic AVL Tree with insert, delete functionality

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.height = 1

class AVL:
    def getHeight(self, r):
        if not r:
            return 0
        return r.height
    
    def getBalance(self, r):
        return self.getHeight(r.left) - self.getHeight(r.right)

    def insert(self, r, data):
        if not r:
            return Node(data)
        
        if data >= r.data:
            r.right = self.insert(r.right, data)
        else:
            r.left = self.insert(r.left, data)
        
        r.height = 1 + max(self.getHeight(r.right), self.getHeight(r.left))

        balance = self.getBalance(r)

        if balance > 1 and data < r.left.data:
            return self.rotateRight(r)
        if balance < -1 and data > r.right.data:
            return self.rotateLeft(r)
        if balance > 1 and data > r.left.data:
            r.left = self.rotateLeft(r.left)
            return self.rotateRight(r)
        if balance < -1 and data < r.right.data:
            r.right = self.rotateRight(r.right)
            return self.rotateLeft(r)

        return r

    def delete(self, r, data):
        if not r:
            return r

        if r.data < data:
            r.right = self.delete(r.right, data)
        elif r.data > data:
            r.left = self.delete(r.left, data)
        else:
            if not r.right:
                temp = r.left
                r.left = None
                return temp
            if not r.left:
                temp = r.right
                r.right = None
                return temp

            temp = minValNode(r.right)
            r.data = temp.data
            r.right = self.delete(r.right, temp.data)

        r.height = 1 + max(self.getHeight(r.right), self.getHeight(r.left))

        balance = self.getBalance(r)

        if balance > 1 and self.getBalance(r.left) <= 0:
            return self.rotateRight(r)
        if balance < -1 and self.getBalance(r.right) >= 0:
            return self.rotateLeft(r)
        if balance > 1 and self.getBalance(r.left) > 0:
            r.left = self.rotateLeft(r.left)
            return self.rotateRight(r)
        if balance < -1 and self.getBalance(r.right) < 0:
            r.right = self.rotateRight(r.right)
            return self.rotateLeft(r)
        
        return r

    def rotateLeft(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rotateRight(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

def minValNode(r):
    if not r:
        return r

    while r.left:
        r = r.left

    return r

def printTree90(r, level=0):
    if r:
        printTree90(r.right, level + 1)
        print('     ' * level, r.data)
        printTree90(r.left, level + 1)


if __name__ == '__main__':
    tree = AVL()
    root = None

    inp = input('Enter input: ').split(',')
    for i in inp:
        ch, n = i.split()
        if ch == 'i':
            root = tree.insert(root, int(n))
        else:
            root = tree.delete(root, int(n))
        printTree90(root)
        print(8 * '=')
