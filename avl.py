from node import Node

class AVL:
    def __init__(self):
        self.root = None
        
    #Put rotate left and rotate right in their own functions
    
    def rotateLeft(self, node):
        curr = node.right
        node.right = curr.left
        curr.parent = node.parent
        node.parent = curr
        curr.left = node
        return curr
        
        
    def rotateRight(self, node):
        curr = node.left
        node.left = curr.right
        curr.parent = node.parent
        node.parent = curr
        curr.right = node
        return curr
    
    
    def balance(self, node):
        currBF = self.heightNode(node.right) - self.heightNode(node.left)
        
        if currBF > 1:
            rightBF = self.heightNode(node.right.right) - self.heightNode(node.right.left)
            if rightBF < 0:
                node.right = self.rotateRight(node.right)
                node = self.rotateLeft(node)
            elif rightBF > 0:
                node = self.rotateLeft(node)
            
        elif currBF < -1:
            leftBF = self.heightNode(node.left.right) - self.heightNode(node.left.left)
            if leftBF < 0:
                node = self.rotateRight(node)
            elif leftBF > 0:
                node.left = self.rotateLeft(node.left)
                node = self.rotateRight(node)

        self.root = node

        return node


        
    def add(self, value):
        curr = self.root
        if curr is None:
            self.root = Node(value)
        else:
            self.root = self.addRecursive(curr, value)

        return self

    def addRecursive(self, curr, value):
        # Add if value is less than value
        if value < curr.value:
            if curr.left is None:
                curr.left = Node(value)
                curr.left.parent = curr
            else:
                self.addRecursive(curr.left, value)
                
                curr = self.balance(curr)

        # Add if value is greater than value
        elif value > curr.value:
            if curr.right is None:
                curr.right = Node(value)
                curr.right.parent = curr
            else:
                self.addRecursive(curr.right, value)
                curr = self.balance(curr)
                
        return curr
   
   
   

    def remove(self, value):
        if self.root is None:
            return self
        if self.root.value == value:
            if self.root.left is None and self.root.right is None:
                self.root = None
            
            elif self.root is not None and self.root.left is not None and self.root.right is None:
                self.root = self.root.left
                
            elif self.root is not None and self.root.left is None and self.root.right is not None:
                self.root = self.root.right
                
            elif self.root is not None and self.root.left is not None and self.root.right is not None:
                temp = self.root.right
                self.root = self.root.left
                self.attachRight(temp, self.root)
                
        else:# calling remove recursive

            self.removeRecursive(value, self.root)
            self.root = self.balance(self.root)

        pass
        return self

    def attachRight(self, temp, curr):
        if curr.right is None:
            curr.right = temp
            temp.parent = curr
            
        elif curr.right is not None:
            self.attachRight(temp, curr.right)

    def removeRecursive(self, value, curr):
        if value == curr.value:
            self.removeComplete(value, curr)
            curr = self.balance(curr)
            
        elif value < curr.value:
            if curr.left is None:
                return self
            
            elif curr.left is not None:
                self.removeRecursive(value, curr.left)
                curr = self.balance(curr)
                
        elif value > curr.value:
            if curr.right is None:
                return self
            
            elif curr.right is not None:
                self.removeRecursive(value, curr.right)
                curr = self.balance(curr)

    def removeComplete(self, value, curr):
        if curr.left is None and curr.right is None:
            if curr.parent.value < curr.value:
                curr.parent.right = None
            elif curr.parent.value > curr.value:
                curr.parent.left = None
            
        elif curr.left is not None and curr.right is None:
            temp = curr.left
            curr.value = curr.left.value
            curr.right = curr.left.right
            curr.left = temp.left
            if curr.left is not None:
                curr.left.parent = curr
            
            
        elif curr.left is None and curr.right is not None:
            temp = curr.right
            curr.value = curr.right.value
            curr.right = curr.right.right
            curr.left = temp.left
            if curr.right is not None:
                curr.right.parent = curr
            pass
        
        elif curr.left is not None and curr.right is not None:
            temp = curr.right
            curr.value = curr.left.value
            curr.right = curr.left.right
            curr.left = curr.left.left
            
            self.attachRight(temp, curr)
            if curr.right is not None:
                curr.right.parent = curr
            if curr.left is not None:
                curr.left.parent = curr

   
   

    def contains(self, value):
        if self.root is None:
            return False
        else:
            return self.containsRecursive(value, self.root)

    def containsRecursive(self, value, curr):
        if curr is None:
            return False
        if curr.value == value:
            return True
        elif curr != value:
            if value < curr.value:
                return self.containsRecursive(value, curr.left)

            elif value > curr.value:
                return self.containsRecursive(value, curr.right)

   
   

    def size(self):
        if self.root is None:
            return 0
        elif self.root.left is None and self.root.right is not None:
            return self.sizeRecursive(self.root.right) + 1
        elif self.root.left is not None and self.root.right is None:
            return self.sizeRecursive(self.root.left) + 1
        else:
            return self.sizeRecursive(self.root.left) + self.sizeRecursive(self.root.right) + 1

    def sizeRecursive(self, curr):
        if curr is None:
            return 0
        elif curr.left is None and curr.right is not None:
            return self.sizeRecursive(curr.right) + 1
        elif curr.left is not None and curr.right is None:
            return self.sizeRecursive(curr.left) + 1
        else:
            return self.sizeRecursive(curr.left) + self.sizeRecursive(curr.right) + 1

   
   

    def asList(self):
        val = []
        if self.root is None:
            return val
        else:
            self.aslistRecursive(self.root, val)
            return val

    def aslistRecursive(self, curr, val):
        if curr is not None:
            val.append(curr.value)
            self.aslistRecursive(curr.left, val)
            self.aslistRecursive(curr.right, val)


    def heightNode(self, curr):
        if curr is None:
            return 0
        else:
            return max(self.heightNode(curr.left), self.heightNode(curr.right)) + 1


    def height(self):
        curr = self.root
        if curr is None:
            return 0
        else:
            return max(self.heightRecursive(curr.left), self.heightRecursive(curr.right)) + 1

    def heightRecursive(self, curr):
         if curr is None:
             return 0
         else:
             return max(self.heightRecursive(curr.left), self.heightRecursive(curr.right)) + 1




#avl = AVL().add(5).add(6).add(2).add(1).add(3).add(7).add(4).remove(7)

#avl = AVL().add(1).add(3).add(2)
avl = AVL().add(1).add(2).add(3).add(4).add(5)

print(avl.asList())
print(avl.size())
#print(avl.height())