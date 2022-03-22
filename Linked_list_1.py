from pdb import line_prefix


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class linked_list:
    def __init__(self):
        self.head=None

    def add_begin(self,value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def add_end(self,value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next=new_node

    def display(self):
        if self.head is None:
            print('head -> None')
        else:
            print('Head',end=' -> ')
            current_node = self.head
            print(str(current_node.value),end=' -> ')
            while current_node.next is not None:
                current_node = current_node.next
                print(str(current_node.value),end=' -> ')
            print('None')

if __name__ == '__main__':
    My_list = linked_list()
    My_list.display()
    My_list.add_end(5)
    My_list.add_begin(2)
    My_list.display()
