class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    # Add a node at the front
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Add a node after a given node
    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("given node must be in link list")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Add a node at the end
    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = new_node

    # search elemnet in link list
    def search_ele(self,key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node.next
        return False

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

link_li = LinkList()
link_li.push(12)
link_li.push(63)
link_li.push(11)
link_li.append(56)
link_li.append(88)
link_li.append(36)
link_li.append(25)
link_li.append(22)
link_li.append(14)
link_li.insert_after(link_li.head.next,99)
link_li.print_list()
print(link_li.search_ele(66))


