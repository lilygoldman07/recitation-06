import math, time

class BinaryHeap:
    def __init__(self):
        self.H = []
        
    def __repr__(self):
        return str(self.H)

    def lchild(self, i):     
        """
        See test_lchild below.

        Params:
        i....index of node
        Returns:
        j....index of the left child of node i, or -1 if n/a
        """
        if (2*i + 1) < len(self.H):
            ## TODO
            pass
        else:
            return -1

    def rchild(self, i):
        """
        See test_rchild below.

        Params:
        i....index of node
        Returns:
        j....index of the right child of node i, or -1 if n/a
        """
        if (2*i + 2) < len(self.H):
            ## TODO
            pass
        else:
            return -1

    def parent(self, i):
        """
        See test_parent below.

        Params:
        i....index of node
        Returns:
        j....index of the parent of node i, or -1 if n/a
        """
        if i > 0:
            ## TODO 
            pass
        else:
            return 0

    def reheapUp(self, i):
        """
        Restore the heap property going upward from node i.
        Swap node i with its parent while the heap property is violated.
        See test_reheapUp.

        Params:
        i......index of the node to start with

        Returns:
        Nothing - this modifies the heap object directly.
        """
        c = i
        p = self.parent(i)
        print("reheaping  up from %d"%i)
        while ((c != 0) and (self.H[c] < self.H[p])):
            ## TODO
            pass

    # restore the heap property going downward from node i
    def reheapDown(self, i):
        """
        Restore the heap property going downward from node i.
        Swap node i with its *smaller* child while the heap property is violated.
        See test_reheapDown.

        Params:
        i......index of the node to start with

        Returns:
        Nothing - this modifies the heap object directly.
        """
        c = i
        l = self.lchild(i)
        r = self.rchild(i)
        while (l > 0 and (self.H[c] > self.H[l])) or (r > 0 and (self.H[c] > self.H[r])):
            ## TODO
            pass
        
        
    def deleteMin(self):
        """
        Remove the root node to return its value.
        Set the last element in the heap to be the root,
        then restore the heap property using reheapDown.
        See test_deleteMin.

        Returns:
        the minimum value in the heap.
        """
        m = self.H[0]
        if (len(self.H) > 1):
            ## TODO
            pass

        else:
            self.H.pop() # removes the only element left
        return m

    def insert(self, x):
        """
        Insert a new value x. To do so, append x
        to the list, then call reheapUp.
        See test_insert.

        Returns nothing.
        """
        pass

def heapsort(a):
    """
    Sort a list a by first creating a heap, then 
    iteratively removing the smallest element to
    construct the sorted list

    Params:
    a......an unsorted list

    Returns:
    sorted version of a
    """
    H = BinaryHeap()
    sorted_a = []
    ## TO DO

    return sorted_a
