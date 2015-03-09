# Python Data Structures

*This repository will hold example code for a number of classic data structures.*

We created a linked list method where the list knows about the first element, and each element is linked to the element behind it.

We also created a stack where an element can be added to the top of the stack, and popped from the top. But they are not linked and you can only manipulate the top of the stack.

We implemented a queue where an item is added into the queue and--contrary to a stack--are removed in the same order they're placed in. Each item is aware of the previous and next items. The list is aware of the first and last item in the list.

We revisted our previous linked list to create a double linked list. Each node of the list points at the next and previous items. The list has pointers for the first and last item of the list.

Priority Queue is a queue that adds priority to the queue items. The idea is to give each value a number that designates is priority. After the queue is made, you can look at the highest priority item, which has the lowest number, via the peek method. The pop method will remove the item with the highest priority without disturbing the order integrety of the list.

Binary Heap is a program that will build a tree of data, and prioritize it based on its value and the value of the 'child' notes below it. We used [interactivepython.org](http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html) as a reference and to assist in implementing the heap. WARNING: The tests are quite inclusive and can take a little while to run, but prove that the program can handle a load.

We have included a basic graph data structure. Our graph is capable of adding vertices/nodes, adding edges between nodes, deleting nodes and edges, reporting all connected nodes, and reporting nodes connected to it. As an inspiration, we used [this educational site](http://www.python-course.eu/graphs_python.php).

We added a graph that includes traversal. Our graph can do both depth first, and breadth first traversal. We used [the same site](http://www.python-course.eu/graphs_python.php) that assisted in our understanding and constructing of our simple graph, as well as the Fundamentals of Python Data Structures book by Kenneth A Lambert.

We have added weighted edges to our graph. Our edges() function does not return weights. Weights can be viewed in the dictionary containing the nodes and edges.

For our weighted graph, we have added two methods of solving the shortest path problem. The first method uses Dijkstra's algorithm, the second uses the Bellman Ford algorithm. Both methods are very similar. The primary benefit of the Bellman Ford algorithm is the detection of negative weight cycles. Negative weight cycles can skew path results into the negative with loops of negative weights. Our primary resources in implementing these algorithms were the [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) article and the [Bellman Ford algorithm](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) article on Wikipedia.


This repository is a collaboration between Jake Anderson and James Warren while attending the Code Fellows Python Development Accelerator in Winter 2015.