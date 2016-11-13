import random


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

class maxOfList(object):
    def __init__(self, list=None):
        self.list = list
    def returnMax(self, node, value=0):
        if not self.list.head:
            return None
        currentMax = node.value
        if not node.next:
            return currentMax

        if currentMax < node.next.value:
            currentMax = node.next.value
        self.returnMax(self, node.next, currentMax)

def returnMax(node, currentMax=0):
    if not node:
        return None
    if not node.next:
        return currentMax
    if currentMax < node.next.value:
        currentMax = node.next.value
    return returnMax(node.next, currentMax)



list = LinkedList()
for i in range(random.randint(0,100)):
    value = random.randint(0,100000)
    print value
    list.append(Element(value))

print "++++++++++"
print returnMax(list.head, list.head.value)