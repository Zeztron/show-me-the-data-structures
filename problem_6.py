class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    set_list = set()
    current_node = llist_1.head

    while current_node:
        set_list.add(current_node.value)
        current_node = current_node.next
    
    current_node = llist_2.head

    while current_node:
        set_list.add(current_node.value)
        current_node = current_node.next
    
    union_list = LinkedList()
    for num in set_list:
        union_list.append(num)
    
    return union_list

def intersection(llist_1, llist_2):
    
    first_set = set()
    current_node = llist_1.head

    while current_node:
        first_set.add(current_node.value)
        current_node = current_node.next
    
    second_set = set()
    current_node = llist_2.head

    while current_node:
        second_set.add(current_node.value)
        current_node = current_node.next
    
    temp_list = sorted([first_set, second_set], key=len)
    third_set = set()

    for list1 in temp_list[0]:
        if list1 in temp_list[1]:
            third_set.add(list1)

    intersection_list = LinkedList()
    for num in third_set:
        intersection_list.append(num)
    
    return intersection_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
