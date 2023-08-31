'''
A linked list is a data structure in which elements, called nodes, are connected together using pointers. Each node 
contains two main components: the data it holds and a reference (or pointer) to the next node in the sequence. 
Linked lists are used to store collections of data, and they offer some advantages and disadvantages compared to other
 data structures like arrays.

Advantages of Linked Lists:

Dynamic Size: Linked lists can grow or shrink dynamically based on the number of elements they hold. 
Elements can be added or removed without the need to preallocate memory.

Memory Efficiency: Linked lists use memory efficiently because they don't require contiguous memory blocks like arrays. 
Nodes can be scattered in memory, allowing for more flexible memory allocation.

Insertions and Deletions: Insertions and deletions can be very efficient in linked lists, especially when working with 
the middle of the list. Adding or removing elements typically involves updating a few pointers, whereas in arrays,
 these operations may require shifting elements.

No Memory Wastage: Unlike arrays, linked lists don't suffer from memory wastage due to resizing. Arrays might need to 
allocate extra space to accommodate growth, but linked lists allocate memory for each node as needed.

Easy to Extend: Linked lists can be easily extended to create more complex data structures, like doubly linked lists 
(where nodes have pointers to both the next and previous nodes) and circular linked lists (where the last node points 
back to the first).

Disadvantages of Linked Lists:

Random Access: Linked lists have poor random access performance compared to arrays. Accessing an element at a specific 
index requires traversing the list from the beginning until reaching the desired node. This takes O(n) time, where n is
 the number of nodes.

Memory Overhead: Each node in a linked list requires extra memory for the data and the pointer to the next node. 
This overhead can be significant when dealing with a large number of small elements.

Complexity: Managing pointers and ensuring they are updated correctly can be complex and error-prone. 
Incorrect pointer manipulation can lead to memory leaks or incorrect behavior.

Cache Performance: Linked lists might not perform well in situations where cache performance is crucial.
 Since nodes are not guaranteed to be stored in contiguous memory locations, cache locality can be poor, impacting
   performance.

More Code Overhead: Implementing and working with linked lists often involves more code than using arrays. 
This can lead to increased development time and potential for bugs.

Linked lists are a fundamental data structure and serve as a building block for more complex structures like stacks, 
queues, and graphs. The choice between using a linked list or another data structure depends on the specific 
requirements of the problem you're trying to solve.

'''


class Node:
    def __init__(self, val,link=None):
        self.val=val
        self.link=link

node_1 = Node(10)
print(node_1.link)