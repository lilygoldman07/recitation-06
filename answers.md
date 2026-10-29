# CMPS 2200 Recitation 06
## Answers

**Name:**Lily Goldman

Place all written answers from `recitation-06.md` here for easier grading.



- **1)** Before we implement a heap, let's consider if we just maintain
 an unordered list/sequence. 

  - **1a) (1 pt)** What is the work/span of *deleteMin*?

    The list is unordered, so the minimum could be anywhere and we have to look at all $n$ elements to find it. Comparing elements can be done in parallel as a reduce, which is a balanced tree of depth $\log n$, and once we know where the min is, removing it is $O(1)$.

    $$W(n) \in O(n), \qquad S(n) \in O(\log n)$$

  - **1b) (1 pt)** What is the work/span ofand *insert(x)*?

    There is no order to maintain, so we just stick $x$ on the end of the list. That is one step.

    $$W(n) \in O(1), \qquad S(n) \in O(1)$$

- **2a) (1 pt)** For a heap with $n$ elements, what does this imply about the depth of the associated almost-complete binary tree? 

  Every level is completely full except possibly the last one, so level $i$ holds $2^i$ nodes and the number of nodes doubles each level down. That means $n$ elements fill up about $\log_2 n$ levels.

  $$\text{depth} = \lfloor \log_2 n \rfloor \in \Theta(\log n)$$

- **2b) (1 pt)** By maintaining the heap property, where is the minimum element of
  the heap? Can we say anything about the maximum element?

  The minimum is always at the root, index 0. Every node is smaller than its children, so following that rule up from anywhere leads to the root being smallest overall.

  For the maximum, all we know is that it has to be a leaf. If it had a child, that child would have to be bigger, which would contradict it being the maximum. We cannot say *which* leaf, so finding it means checking all of them. The leaves are the last half of the list, indices $\lfloor n/2 \rfloor$ through $n-1$.

- **4a) (1 pt)** What is the work/span of *reheapUp*($x$)?

  Each swap moves the value up one level, so in the worst case it travels from a leaf all the way to the root, which is the depth of the tree. Each swap is $O(1)$, and the swaps have to happen one after another, so the span is the same as the work.

  $$W(n) \in O(\log n), \qquad S(n) \in O(\log n)$$

- **4b) (1 pt)** What is the work/span of *reheapDown*($x$)? 

  Same reasoning in the other direction: each swap moves the value down one level, so the worst case is root to leaf, which is again the depth. Comparing against both children is $O(1)$ per step, and the steps are sequential.

  $$W(n) \in O(\log n), \qquad S(n) \in O(\log n)$$

- **6) (1 pt)** What is the work and span of `heapsort`?

  There are two phases. First we do $n$ inserts, and each one is $O(\log n)$ because it calls `reheapUp`. Then we do $n$ `deleteMin`s, and each one is $O(\log n)$ because it calls `reheapDown`. That is $2n$ operations of $O(\log n)$ each.

  $$W(n) \in O(n \log n)$$

  The span is the same. Every operation changes the heap that the next one reads, so nothing can be done in parallel and the whole thing is one long sequential chain.

  $$S(n) \in O(n \log n)$$