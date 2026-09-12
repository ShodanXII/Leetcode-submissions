class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        current = self.head.next
        i = 0
        while current:
            if i == index:
                return current.value
            current = current.next
            i+=1
        return -1

    def insertHead(self, value: int) -> None:
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail=new_node

    def insertTail(self, value: int) -> None:
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        i = 0
        current = self.head
        while i < index and current:
            i+=1
            current = current.next
        if current and current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res
