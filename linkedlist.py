class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linkedlist:
    def __init__(self):
        self.head = None

    def insertbegin(self, data):
        node = Node(data, self.head)
        self.head = node

    def insertend(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insertVals(self, data_list):
        for data in data_list:
            self.insertend(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count = count+1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("index out of range")

        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count = count + 1

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return

        itr = self.head
        linkedstring = ''
        while itr:
            linkedstring = linkedstring + str(itr.data) + '--->'
            itr = itr.next

        print(linkedstring)


class Queue:
    def __init__(self):
        self.head = None

    def insert(self, node):
        node = Node(node, self.head)
        self.head = None

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count = count+1
            itr = itr.next

        return count

    def pop(self):
        itr = self.head
        count = 0
        index = self.get_length()
        while itr:
            if count == index-1:
                itr = itr.next


ll = linkedlist()
ll.insertbegin("karachi")
ll.insertbegin("dubai")
ll.insertbegin("chicago")
ll.insertbegin("Florida")
ll.insertend("Newyork")
ll.insertVals(["London", "hongkomg", "tokyo", "Sydney"])
ll.print()
print(ll.get_length())
ll.remove_at(4)
print("removing ", 4)
ll.print()
ll.get_length()
