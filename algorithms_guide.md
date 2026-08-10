# Essential Algorithms Every CS Student Should Know
### (Up to Associate Software / ML Developer Level)

This guide covers the most important, most frequently used, and most commonly asked algorithms in interviews and real-world software development — **classical CS algorithms plus the core algorithms behind AI/ML engineering**. Each algorithm includes:

- **Explanation** — how and why it works
- **Python Code** — clean, runnable implementation
- **Dry Run** — step-by-step trace on a sample input
- **Practical Use** — where it's actually used in the real world
- **Optimization** — how to make it faster / leaner

Final **comparison tables** of time and space complexity are included at the end of each major part.

---

## Table of Contents

1. [Searching Algorithms](#1-searching-algorithms)
   - 1.1 [Linear Search](#11-linear-search)
   - 1.2 [Binary Search](#12-binary-search)
2. [Sorting Algorithms](#2-sorting-algorithms)
   - 2.1 [Bubble Sort](#21-bubble-sort)
   - 2.2 [Selection Sort](#22-selection-sort)
   - 2.3 [Insertion Sort](#23-insertion-sort)
   - 2.4 [Merge Sort](#24-merge-sort)
   - 2.5 [Quick Sort](#25-quick-sort)
   - 2.6 [Heap Sort](#26-heap-sort)
3. [Graph Algorithms](#3-graph-algorithms)
   - 3.1 [Breadth-First Search (BFS)](#31-breadth-first-search-bfs)
   - 3.2 [Depth-First Search (DFS)](#32-depth-first-search-dfs)
   - 3.3 [Dijkstra's Algorithm](#33-dijkstras-algorithm)
4. [Dynamic Programming](#4-dynamic-programming)
   - 4.1 [Fibonacci (Memoization)](#41-fibonacci-memoization)
   - 4.2 [0/1 Knapsack](#42-01-knapsack)
   - 4.3 [Longest Common Subsequence (LCS)](#43-longest-common-subsequence-lcs)
5. [AI / ML Engineering Algorithms](#5-ai--ml-engineering-algorithms)
   - 5.1 [Gradient Descent](#51-gradient-descent)
   - 5.2 [Linear Regression](#52-linear-regression)
   - 5.3 [Logistic Regression](#53-logistic-regression)
   - 5.4 [K-Nearest Neighbors (KNN)](#54-k-nearest-neighbors-knn)
   - 5.5 [K-Means Clustering](#55-k-means-clustering)
   - 5.6 [Decision Tree](#56-decision-tree)
   - 5.7 [Naive Bayes](#57-naive-bayes)
   - 5.8 [Principal Component Analysis (PCA)](#58-principal-component-analysis-pca)
   - 5.9 [Backpropagation (Neural Networks)](#59-backpropagation-neural-networks)
6. [Master Complexity Comparison Tables](#6-master-complexity-comparison-tables)

---

## 1. Searching Algorithms

### 1.1 Linear Search

**Explanation:**
Check every element one by one from left to right until the target is found or the list ends. No assumptions about ordering are required.

**Code:**
```python
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Example
print(linear_search([5, 3, 8, 1, 9], 8))  # Output: 2
```

**Dry Run:** `arr = [5, 3, 8, 1, 9]`, `target = 8`

| Step | index | value | value == target? |
|------|-------|-------|-------------------|
| 1 | 0 | 5 | No |
| 2 | 1 | 3 | No |
| 3 | 2 | 8 | **Yes → return 2** |

**Practical Use:**
- Searching in small or unsorted datasets
- Searching linked lists (no random access)
- Used internally by simple utilities where data size is small enough that setup cost of a smarter structure isn't worth it

**Optimization:**
- If the list is sorted, switch to **Binary Search** (O(log n))
- If searches happen repeatedly, build a **hash set/dict** once for O(1) average lookups
- Add a **sentinel value** at the end to remove the bounds-check in tight loops (micro-optimization in low-level languages)

---

### 1.2 Binary Search

**Explanation:**
Works only on **sorted** arrays. Repeatedly divide the search interval in half — compare the target with the middle element, and discard the half that cannot contain the target.

**Code:**
```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example
print(binary_search([1, 3, 5, 7, 9, 11], 7))  # Output: 3
```

**Dry Run:** `arr = [1, 3, 5, 7, 9, 11]`, `target = 7`

| Step | low | high | mid | arr[mid] | Action |
|------|-----|------|-----|----------|--------|
| 1 | 0 | 5 | 2 | 5 | 5 < 7 → low = 3 |
| 2 | 3 | 5 | 4 | 9 | 9 > 7 → high = 3 |
| 3 | 3 | 3 | 3 | 7 | **Match → return 3** |

**Practical Use:**
- Searching sorted arrays/databases indexes
- `bisect` module in Python (used for maintaining sorted lists)
- Finding boundaries in "search space" problems (e.g., "smallest value that satisfies condition X" — binary search on the answer)
- Version control bisecting (`git bisect`)

**Optimization:**
- Use iterative version (shown above) instead of recursive to avoid call-stack overhead
- For repeated searches on static data, precompute once and reuse (already O(log n), hard to beat without a hash map, which trades order for O(1))
- Python's built-in `bisect.bisect_left` / `bisect_right` are C-optimized — prefer them in production code

---

## 2. Sorting Algorithms

### 2.1 Bubble Sort

**Explanation:**
Repeatedly step through the list, compare adjacent elements, and swap them if they're in the wrong order. Largest elements "bubble up" to the end each pass.

**Code:**
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:   # Optimization: stop early if already sorted
            break
    return arr

print(bubble_sort([5, 1, 4, 2, 8]))  # [1, 2, 4, 5, 8]
```

**Dry Run:** `arr = [5, 1, 4, 2, 8]`

- Pass 1: [1,5,4,2,8] → [1,4,5,2,8] → [1,4,2,5,8] → [1,4,2,5,8] (8 stays)
- Pass 2: [1,4,2,5,8] → [1,2,4,5,8]
- Pass 3: no swaps → **early exit**

**Practical Use:**
- Rarely used in production due to poor performance
- Useful for **teaching** the concept of swapping/comparison sorts
- Good for **nearly-sorted, tiny datasets** where simplicity beats speed

**Optimization:**
- The `swapped` flag (shown above) turns best case into **O(n)** for already-sorted input
- Beyond that, there's little to optimize — for real workloads, replace algorithm entirely with Merge/Quick/Tim Sort

---

### 2.2 Selection Sort

**Explanation:**
Divide the array into a sorted and unsorted part. Repeatedly find the **minimum** element from the unsorted part and move it to the end of the sorted part.

**Code:**
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([64, 25, 12, 22, 11]))  # [11, 12, 22, 25, 64]
```

**Dry Run:** `arr = [64, 25, 12, 22, 11]`

| i | Unsorted portion scanned | Min found | Array after swap |
|---|---------------------------|-----------|-------------------|
| 0 | [64,25,12,22,11] | 11 (idx 4) | [11,25,12,22,64] |
| 1 | [25,12,22,64] | 12 (idx 2) | [11,12,25,22,64] |
| 2 | [25,22,64] | 22 (idx 3) | [11,12,22,25,64] |
| 3 | [25,64] | 25 (idx 3) | [11,12,22,25,64] |

**Practical Use:**
- Situations where **memory writes are costly** — selection sort does at most O(n) swaps (unlike bubble/insertion), useful when write operations are expensive (e.g., flash memory)
- Teaching invariant-based algorithm design

**Optimization:**
- Track both min **and max** per pass ("double selection sort") to cut passes in half
- For real use, this algorithm's O(n²) comparisons can't be reduced — replace with Merge/Quick Sort for large n

---

### 2.3 Insertion Sort

**Explanation:**
Build the sorted array one element at a time — take each element and insert it into its correct position among the already-sorted elements to its left (like sorting playing cards in hand).

**Code:**
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort([12, 11, 13, 5, 6]))  # [5, 6, 11, 12, 13]
```

**Dry Run:** `arr = [12, 11, 13, 5, 6]`

| i | key | Array during shift | Result |
|---|-----|---------------------|--------|
| 1 | 11 | shift 12 right | [11,12,13,5,6] |
| 2 | 13 | no shift needed | [11,12,13,5,6] |
| 3 | 5 | shift 13,12,11 right | [5,11,12,13,6] |
| 4 | 6 | shift 13,12,11 right | [5,6,11,12,13] |

**Practical Use:**
- **Excellent for small or nearly-sorted arrays** — used as the base case inside hybrid sorts
- Python's `sort()` / `sorted()` (Timsort) switches to insertion sort for small sub-arrays (~64 elements)
- Online sorting — useful when data arrives one item at a time (e.g., streaming input)

**Optimization:**
- Use **binary search** to find the insertion point (Binary Insertion Sort) — reduces comparisons to O(log n) per element, though shifting is still O(n), so total remains O(n²) worst case but with fewer comparisons
- Combine with Merge Sort for a hybrid approach (this is essentially what **Timsort** does)

---

### 2.4 Merge Sort

**Explanation:**
A **divide-and-conquer** algorithm: split the array into halves recursively until each piece has one element, then merge the pieces back together in sorted order.

**Code:**
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
# [3, 9, 10, 27, 38, 43, 82]
```

**Dry Run:** `arr = [38, 27, 43, 3]`

- Split: [38,27] and [43,3]
- Split further: [38],[27] and [43],[3]
- Merge: [38],[27] → [27,38]  |  [43],[3] → [3,43]
- Final merge: [27,38] + [3,43] → **[3,27,38,43]**

**Practical Use:**
- **External sorting** — sorting data too large to fit in RAM (merge sorted chunks from disk)
- Stable sort needed when equal elements must preserve original order (e.g., sorting by one field after already sorting by another)
- Basis of **Timsort** (Python's/Java's built-in sort)
- Counting inversions in an array, linked list sorting

**Optimization:**
- Switch to **insertion sort** for small sub-arrays (below ~10-15 elements) to reduce recursion overhead
- Use an **in-place merge** or a reusable auxiliary buffer to cut down the O(n) extra space per merge call
- For linked lists, merge sort can be done truly in-place (O(1) extra space) since no random access/array copying is needed

---

### 2.5 Quick Sort

**Explanation:**
Also divide-and-conquer: pick a **pivot**, partition the array so smaller elements go left and larger go right of the pivot, then recursively sort each partition.

**Code:**
```python
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]          # choosing last element as pivot
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

print(quick_sort([10, 7, 8, 9, 1, 5]))
# [1, 5, 7, 8, 9, 10]
```

**Dry Run:** `arr = [10, 7, 8, 9, 1, 5]`, pivot = 5 (last element)

- Scan j=0..4, move elements ≤ 5 to the left:
  - Only `1` is ≤ 5 → swap into position → [1, 7, 8, 9, 10, 5]
- Swap pivot into place: [1, 5, 8, 9, 10, 7] → pivot index = 1
- Recurse left on `[1]` (already sorted), right on `[8,9,10,7]` and so on until fully sorted

**Practical Use:**
- Default sorting algorithm in many language libraries (C's `qsort`, older Java arrays of primitives)
- Fast **in-place** sort — no extra array needed, good for memory-constrained systems
- Used in **Quickselect** to find the k-th smallest/largest element in O(n) average time

**Optimization:**
- **Randomized pivot** or **median-of-three** (first, middle, last) selection avoids worst-case O(n²) on sorted/reverse-sorted input
- **Tail-call/recursion on smaller partition only** to keep stack depth at O(log n)
- Switch to insertion sort for small partitions (< 10 elements)
- Use **3-way partitioning (Dutch National Flag)** when there are many duplicate keys

---

### 2.6 Heap Sort

**Explanation:**
Build a **max-heap** from the array (parent ≥ children), then repeatedly swap the root (maximum) with the last element and shrink the heap, re-heapifying each time.

**Code:**
```python
def heap_sort(arr):
    n = len(arr)

    def heapify(n, i):
        largest = i
        left, right = 2 * i + 1, 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n, largest)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)

    return arr

print(heap_sort([12, 11, 13, 5, 6, 7]))
# [5, 6, 7, 11, 12, 13]
```

**Dry Run:** `arr = [12, 11, 13, 5, 6, 7]`

- Build max-heap → `[13, 11, 12, 5, 6, 7]`
- Swap root(13) with last(7) → `[7,11,12,5,6,13]`, heapify(0..4) → `[12,11,7,5,6,13]`
- Swap root(12) with `[..,6]` → continues shrinking heap, re-heapifying, until fully sorted

**Practical Use:**
- **Priority queues** (heap operations underpin `heapq` in Python)
- Guarantees **O(n log n) worst case** (unlike Quick Sort) — useful in real-time systems needing predictable performance
- **Selection algorithms** — finding top-K elements efficiently

**Optimization:**
- Use **Floyd's build-heap** method (bottom-up, shown above) — O(n) instead of O(n log n) for building the initial heap
- For "top-K of a huge stream" problems, keep a heap of size K instead of sorting the whole array (O(n log K) instead of O(n log n))

---

## 3. Graph Algorithms

### 3.1 Breadth-First Search (BFS)

**Explanation:**
Explore a graph **level by level** using a queue — visit all neighbors of a node before moving to the next depth level. Guarantees the shortest path in **unweighted** graphs.

**Code:**
```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']
}
print(bfs(graph, 'A'))  # ['A', 'B', 'C', 'D', 'E', 'F']
```

**Dry Run:** start = `'A'`

| Step | queue (before pop) | node popped | order so far | newly visited pushed |
|------|---------------------|--------------|----------------|------------------------|
| 1 | [A] | A | [A] | B, C |
| 2 | [B, C] | B | [A,B] | D, E |
| 3 | [C, D, E] | C | [A,B,C] | F |
| 4 | [D, E, F] | D | [A,B,C,D] | — |
| 5 | [E, F] | E | [A,B,C,D,E] | — |
| 6 | [F] | F | [A,B,C,D,E,F] | — |

**Practical Use:**
- **Shortest path in unweighted graphs** (e.g., social network "degrees of separation")
- **Web crawlers** (crawl links level by level)
- **GPS navigation** for unweighted road networks
- Finding connected components, testing bipartiteness

**Optimization:**
- Use `deque` (O(1) pops from the left) instead of a Python list (O(n) pops from the front)
- For very large graphs, use **bidirectional BFS** (search from both start and target simultaneously) to cut search space roughly in half
- Mark nodes visited **at the time of enqueueing**, not dequeueing, to avoid duplicate queue entries

---

### 3.2 Depth-First Search (DFS)

**Explanation:**
Explore as far as possible along each branch before backtracking, typically via recursion or an explicit stack.

**Code:**
```python
def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited, order = set(), []
    visited.add(start)
    order.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order

print(dfs(graph, 'A'))  # ['A', 'B', 'D', 'E', 'F', 'C']
```

**Dry Run:** start = `'A'`

- Visit A → visit B (first neighbor) → visit D (dead end, backtrack) → visit E → visit F → visit C (F's neighbor, already reachable) → backtrack fully
- Order: `A → B → D → E → F → C`

**Practical Use:**
- **Cycle detection** in graphs
- **Topological sorting** (task scheduling, build systems, package dependency resolution)
- Solving mazes / puzzles (backtracking problems like Sudoku, N-Queens)
- Finding connected components, strongly connected components (Tarjan's/Kosaraju's algorithm)

**Optimization:**
- Convert recursive DFS to **iterative DFS with an explicit stack** to avoid Python's recursion limit / stack overflow on deep graphs
- Use **adjacency lists** (not matrices) for sparse graphs to reduce space from O(V²) to O(V+E)

---

### 3.3 Dijkstra's Algorithm

**Explanation:**
Finds the shortest path from a source node to all other nodes in a **weighted graph with non-negative edges**, using a min-priority queue to always expand the currently-closest unvisited node.

**Code:**
```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        current_dist, node = heapq.heappop(pq)
        if current_dist > distances[node]:
            continue  # outdated entry, skip
        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('A', 4), ('D', 1)],
    'C': [('A', 1), ('B', 2), ('D', 5)],
    'D': [('B', 1), ('C', 5)]
}
print(dijkstra(graph, 'A'))
# {'A': 0, 'B': 3, 'C': 1, 'D': 4}
```

**Dry Run:** start = `'A'`

| Step | pq popped | current_dist | Update distances |
|------|-----------|---------------|--------------------|
| 1 | (0, A) | 0 | B=4, C=1 |
| 2 | (1, C) | 1 | B=3 (1+2 < 4), D=6 |
| 3 | (3, B) | 3 | D=4 (3+1 < 6) |
| 4 | (4, D) | 4 | no better updates |

Final: `A=0, B=3, C=1, D=4`

**Practical Use:**
- **GPS/map routing** (Google Maps-style shortest routes)
- **Network routing protocols** (OSPF)
- Flight/transit fare optimization
- Any "cheapest path" problem with non-negative costs

**Optimization:**
- Use a **binary heap** (as shown, via `heapq`) instead of scanning for the minimum every time — brings complexity from O(V²) down to O((V+E) log V)
- Use a **Fibonacci heap** for theoretical O(E + V log V) (rarely worth it in practice due to overhead)
- If the graph has **negative edges**, switch to **Bellman-Ford**; if it's a DAG, use simple topological-order relaxation for O(V+E)
- **A\*** search (Dijkstra + heuristic) when you only need the shortest path to a *specific* target, not all nodes

---

## 4. Dynamic Programming

### 4.1 Fibonacci (Memoization)

**Explanation:**
Naive recursion recomputes the same subproblems exponentially many times. **Memoization** caches each subproblem's result so it's computed only once.

**Code:**
```python
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

print(fib_memo(10))  # 55

# Bottom-up (tabulation) version - O(1) space
def fib_tab(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

print(fib_tab(10))  # 55
```

**Dry Run:** `fib_memo(5)`

- fib(5) needs fib(4), fib(3)
- fib(4) needs fib(3) [cached after first compute], fib(2)
- Without memo: fib(3) would be recomputed multiple times
- With memo: `memo = {2:1, 3:2, 4:3, 5:5}` — each value computed **exactly once**

**Practical Use:**
- Core teaching example for **all DP problems** (overlapping subproblems + optimal substructure)
- Real Fibonacci-like recurrences appear in financial modeling, population growth models, and algorithm analysis (e.g., worst-case analysis of Euclidean GCD)

**Optimization:**
- **Tabulation with O(1) space** (shown as `fib_tab`) — no recursion overhead, no dictionary needed
- **Matrix exponentiation** — compute the n-th Fibonacci number in O(log n) time using matrix power
- **Fast doubling method** — another O(log n) technique using identities of Fibonacci numbers

---

### 4.2 0/1 Knapsack

**Explanation:**
Given items with weights and values, and a knapsack of capacity `W`, choose a subset of items (each item used **at most once**) to maximize total value without exceeding capacity.

**Code:**
```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],  # take item
                    dp[i - 1][w]                                     # skip item
                )
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
print(knapsack(weights, values, 7))  # 9
```

**Dry Run:** `weights=[1,3,4,5]`, `values=[1,4,5,7]`, `capacity=7`

The DP table fills in row by row (one row per item considered), column by column (one column per capacity from 0 to 7). At each cell, it picks the better of "skip this item" vs. "take this item + best solution for the remaining capacity":

| Item (w,v) considered | Best value achievable at capacity 7 so far |
|---|---|
| Only (1,1) available | 1 |
| (1,1),(3,4) available | 5 (take both: weight 4, value 5) |
| (1,1),(3,4),(4,5) available | **9** (take (3,4)+(4,5): weight 7, value 9) |
| All four items available | **9** (adding (5,7) doesn't beat the above — taking it plus (1,1) only gives 8) |

Final answer: `dp[4][7] = 9`, achieved by choosing items **(3,4)** and **(4,5)** — note that a naive greedy-by-weight or greedy-by-value approach would miss this combination, which is exactly why the full DP table is needed.

**Practical Use:**
- **Resource allocation** — budget/investment portfolio selection
- **Cargo loading / shipping** optimization
- Cutting stock problems, project selection under budget constraints

**Optimization:**
- **1D rolling array** — since `dp[i]` only depends on `dp[i-1]`, reduce space from O(n·W) to **O(W)** by iterating `w` from high to low
- If values/weights allow, use **branch and bound** or **meet-in-the-middle** for very large item counts
- For the **fractional** knapsack variant (items divisible), a **greedy** approach (sort by value/weight ratio) is optimal and much faster — O(n log n)

```python
# Space-optimized 1D version
def knapsack_optimized(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    return dp[capacity]
```

---

### 4.3 Longest Common Subsequence (LCS)

**Explanation:**
Find the longest sequence that appears (not necessarily contiguously) in both of two strings, in the same relative order.

**Code:**
```python
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

print(lcs("ABCBDAB", "BDCABA"))  # 4  (e.g. "BCBA")
```

**Dry Run:** `text1="ABC"`, `text2="AC"`

|    | "" | A | C |
|----|----|----|----|
| ""| 0 | 0 | 0 |
| A | 0 | 1 | 1 |
| B | 0 | 1 | 1 |
| C | 0 | 1 | **2** |

Final answer = `dp[3][2] = 2` (subsequence `"AC"`)

**Practical Use:**
- **`diff` tools / version control** (Git shows line-by-line changes using LCS-based diffing)
- **DNA/protein sequence alignment** in bioinformatics
- Plagiarism/similarity detection between documents
- Spell-checking and autocorrect suggestion ranking

**Optimization:**
- **Space optimization**: only the previous row of the DP table is needed at any time → reduce space from O(m·n) to **O(min(m,n))**
- For reconstructing the actual subsequence (not just its length), backtrack through the DP table (needs the full 2D table, so the space optimization above only works if you need the length only)
- **Hirschberg's algorithm** finds the actual LCS string in O(m·n) time but only **O(min(m,n))** space using divide-and-conquer — used when both time and space matter

---

## 5. AI / ML Engineering Algorithms

### 5.1 Gradient Descent

**Explanation:**
The foundational optimization algorithm behind almost all machine learning. To minimize a cost function, repeatedly move each parameter a small step in the **opposite direction of the gradient** (the direction of steepest increase), scaled by a **learning rate**.

**Code:**
```python
def gradient_descent(start_x, learning_rate=0.1, iterations=20):
    x = start_x
    history = [x]
    for _ in range(iterations):
        grad = 2 * (x - 3)   # derivative of f(x) = (x - 3)^2, minimum at x=3
        x = x - learning_rate * grad
        history.append(x)
    return x, history

final_x, hist = gradient_descent(start_x=0.0)
print(round(final_x, 3))  # ~2.965, converging toward 3
```

**Dry Run:** minimizing `f(x) = (x-3)²`, starting at `x=0`, `learning_rate=0.1`

| Iteration | x | gradient = 2(x-3) | x_new = x − lr·grad |
|---|---|---|---|
| 1 | 0.000 | -6.000 | 0.600 |
| 2 | 0.600 | -4.800 | 1.080 |
| 3 | 1.080 | -3.840 | 1.464 |
| 4 | 1.464 | -3.072 | 1.771 |
| ... | ... | ... | → converges to **x ≈ 3** |

**Practical Use:**
- Training **every** parametric ML model — linear/logistic regression, neural networks, transformers
- Minimizing loss functions (MSE, cross-entropy) during model training
- Powers modern deep learning frameworks (PyTorch, TensorFlow) under the hood via autograd

**Optimization:**
- **Stochastic Gradient Descent (SGD)** — update using one sample at a time instead of the full dataset, much faster per step for huge datasets
- **Mini-batch Gradient Descent** — the industry-standard middle ground; update using small batches (e.g., 32–256 samples) for a good speed/stability tradeoff
- **Momentum** — accumulate a moving average of past gradients to speed through flat regions and dampen oscillation
- **Adam / RMSprop** — adaptive learning-rate optimizers that adjust step size per-parameter; the default choice in most modern deep learning

---

### 5.2 Linear Regression

**Explanation:**
Fit a straight line `y = wx + b` that best predicts a continuous target by minimizing **Mean Squared Error (MSE)** between predictions and actual values, using gradient descent to update `w` and `b`.

**Code:**
```python
import numpy as np

def linear_regression(X, y, lr=0.01, epochs=1000):
    n = len(X)
    w, b = 0.0, 0.0
    for _ in range(epochs):
        y_pred = w * X + b
        dw = (-2/n) * np.sum(X * (y - y_pred))
        db = (-2/n) * np.sum(y - y_pred)
        w -= lr * dw
        b -= lr * db
    return w, b

X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([3, 5, 7, 9, 11], dtype=float)   # true relationship: y = 2x + 1
w, b = linear_regression(X, y)
print(f"w={w:.3f}, b={b:.3f}")   # w≈2.004, b≈0.986
```

**Dry Run:** `X = [1,2,3,4,5]`, `y = [3,5,7,9,11]` (true line: `y = 2x + 1`)

| Epoch | w | b | Notes |
|---|---|---|---|
| 0 (init) | 0.000 | 0.000 | predictions all 0, large error |
| ~100 | ~1.6 | ~0.7 | rapidly approaching true line |
| 1000 (final) | **2.004** | **0.986** | converged very close to `w=2, b=1` |

**Practical Use:**
- **House price prediction, sales forecasting, demand estimation**
- Baseline model for any regression task before trying more complex models
- Trend analysis in analytics dashboards (e.g., "revenue vs. time")

**Optimization:**
- **Normal Equation** (`w = (XᵀX)⁻¹Xᵀy`) — closed-form solution, no iteration needed for small/medium feature counts (avoids picking a learning rate at all)
- **Feature scaling / normalization** — dramatically speeds up gradient descent convergence when features have very different ranges
- **Regularization** (Ridge = L2, Lasso = L1) — penalizes large weights to reduce overfitting, especially with many correlated features
- **Vectorized NumPy operations** (as shown) instead of Python loops — orders of magnitude faster

---

### 5.3 Logistic Regression

**Explanation:**
Despite the name, this is a **classification** algorithm. It applies a **sigmoid function** to a linear combination of inputs to squash output into a probability between 0 and 1, then minimizes **cross-entropy loss** via gradient descent.

**Code:**
```python
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def logistic_regression(X, y, lr=0.1, epochs=1000):
    n, m = X.shape
    w = np.zeros(m)
    b = 0.0
    for _ in range(epochs):
        y_pred = sigmoid(X @ w + b)
        dw = (1/n) * X.T @ (y_pred - y)
        db = (1/n) * np.sum(y_pred - y)
        w -= lr * dw
        b -= lr * db
    return w, b

X = np.array([[0.5], [1.5], [3.0], [4.0], [5.0]])
y = np.array([0, 0, 1, 1, 1])
w, b = logistic_regression(X, y)
predictions = (sigmoid(X @ w + b) >= 0.5).astype(int)
print(predictions.flatten())  # [0 0 1 1 1]
```

**Dry Run:** 1-feature dataset, labels `[0,0,1,1,1]` for inputs `[0.5,1.5,3.0,4.0,5.0]`

- Start: `w=0, b=0` → sigmoid always outputs 0.5 → 50% probability for everything (all wrong-ish)
- Each epoch nudges `w` positive (higher x → higher probability of class 1) since that reduces cross-entropy loss
- After 1000 epochs, the decision boundary settles between x=1.5 and x=3.0, correctly separating both classes → **final predictions: `[0, 0, 1, 1, 1]`** ✓ matches true labels

**Practical Use:**
- **Binary classification**: spam detection, churn prediction, fraud detection, click-through-rate (CTR) prediction
- Medical diagnosis (disease present / not present) — valued for interpretable coefficients
- Common **baseline classifier** before trying more complex models (SVMs, gradient boosting, neural nets)

**Optimization:**
- **L2/L1 regularization** to prevent overfitting on high-dimensional data (e.g., text features)
- **Class weighting / oversampling** for imbalanced datasets (e.g., 1% fraud cases)
- Use optimized solvers (**L-BFGS**, **Newton's method**) instead of plain gradient descent for faster convergence on small-to-medium datasets
- **One-vs-Rest** or **Softmax (multinomial)** extension for multi-class classification

---

### 5.4 K-Nearest Neighbors (KNN)

**Explanation:**
A **lazy learner** — there's no real "training" phase. To classify a new point, find the `k` closest points in the training data (by distance, usually Euclidean) and take a **majority vote** of their labels.

**Code:**
```python
import numpy as np

def knn_predict(X_train, y_train, x_query, k=3):
    distances = [(np.linalg.norm(x_query - x), label) for x, label in zip(X_train, y_train)]
    distances.sort(key=lambda t: t[0])
    k_nearest_labels = [label for _, label in distances[:k]]
    return max(set(k_nearest_labels), key=k_nearest_labels.count)

X_train = np.array([[1,1],[1,2],[2,1],[6,6],[6,7],[7,6]])
y_train = ['A','A','A','B','B','B']
print(knn_predict(X_train, y_train, np.array([1.5, 1.5]), k=3))  # 'A'
```

**Dry Run:** classify point `[1.5, 1.5]` with `k=3`

| Training point | Label | Distance to [1.5,1.5] |
|---|---|---|
| [1,1] | A | 0.71 |
| [1,2] | A | 0.71 |
| [2,1] | A | 0.71 |
| [6,6] | B | 6.36 |
| [6,7] | B | 7.16 |
| [7,6] | B | 6.86 |

3 nearest = `[1,1], [1,2], [2,1]` → all label **A** → **predicted class = 'A'**

**Practical Use:**
- **Recommendation systems** (find users/items similar to a given one)
- Image classification baselines, handwriting recognition (classic MNIST baseline)
- **Anomaly detection** — points with far/no close neighbors are outliers
- Collaborative filtering in e-commerce ("customers who bought this also liked...")

**Optimization:**
- Use **KD-Trees or Ball Trees** to reduce nearest-neighbor lookup from O(n) to ~O(log n) per query (huge win for large datasets)
- **Dimensionality reduction (PCA)** before KNN — distance metrics become less meaningful in very high dimensions ("curse of dimensionality")
- For massive datasets, use **Approximate Nearest Neighbor (ANN)** libraries like **FAISS** or **Annoy** — trade a little accuracy for huge speed gains
- **Feature scaling is essential** — unscaled features with large ranges dominate the distance calculation

---

### 5.5 K-Means Clustering

**Explanation:**
An **unsupervised** algorithm that partitions data into `k` clusters. Iteratively: (1) assign each point to its nearest centroid, (2) recompute each centroid as the mean of its assigned points, and repeat until centroids stop moving.

**Code:**
```python
import numpy as np

def k_means(X, k, iterations=100):
    centroids = X[np.random.choice(len(X), k, replace=False)]
    for _ in range(iterations):
        clusters = [[] for _ in range(k)]
        for point in X:
            distances = [np.linalg.norm(point - c) for c in centroids]
            clusters[np.argmin(distances)].append(point)
        new_centroids = np.array([
            np.mean(c, axis=0) if c else centroids[i]
            for i, c in enumerate(clusters)
        ])
        if np.allclose(new_centroids, centroids):
            break
        centroids = new_centroids
    return centroids, clusters

X = np.array([[1,1],[1.5,2],[3,4],[5,7],[3.5,5],[4.5,5],[3.5,4.5]])
centroids, clusters = k_means(X, k=2)
print(np.round(centroids, 2))
# roughly [[1.25, 1.5], [3.9, 5.1]]
```

**Dry Run:** 7 points, `k=2`

- Initial centroids picked randomly, e.g. `[1,1]` and `[5,7]`
- **Assignment**: points near `[1,1]` → cluster 0; points near `[5,7]` → cluster 1
- **Update**: recompute mean of each cluster → new centroids move toward `[1.25, 1.5]` and `[3.9, 5.1]`
- Repeat assignment/update until centroids stop changing → **converged**, final centroids ≈ `[1.25, 1.5]` and `[3.9, 5.1]`

**Practical Use:**
- **Customer segmentation** for targeted marketing
- **Image compression** (color quantization — reduce an image to k dominant colors)
- Document/topic clustering, anomaly detection (points far from every centroid)
- Pre-processing step to generate features for downstream supervised models

**Optimization:**
- **K-Means++** initialization — spreads out initial centroids intelligently, avoiding poor local minima and speeding up convergence (the default in scikit-learn)
- **Mini-batch K-Means** — use random subsets per iteration for huge datasets, trading a little accuracy for major speed gains
- Use the **Elbow Method** or **Silhouette Score** to systematically choose the right value of `k`
- Vectorize distance computation across all points/centroids at once instead of nested loops

---

### 5.6 Decision Tree

**Explanation:**
Builds a tree by recursively splitting data on the feature/threshold that most reduces **impurity** (commonly measured with **Gini Impurity** or **entropy**), until a stopping condition (max depth, min samples, or pure leaf) is reached.

**Code:**
```python
def gini_impurity(labels):
    classes = set(labels)
    n = len(labels)
    impurity = 1.0
    for c in classes:
        p = labels.count(c) / n
        impurity -= p ** 2
    return impurity

def best_split(X, y, feature_idx):
    best_gain, best_threshold = -1, None
    base_impurity = gini_impurity(y)
    thresholds = sorted(set(row[feature_idx] for row in X))
    for t in thresholds:
        left_y  = [y[i] for i in range(len(X)) if X[i][feature_idx] <= t]
        right_y = [y[i] for i in range(len(X)) if X[i][feature_idx] > t]
        if not left_y or not right_y:
            continue
        p = len(left_y) / len(y)
        gain = base_impurity - (p * gini_impurity(left_y) + (1 - p) * gini_impurity(right_y))
        if gain > best_gain:
            best_gain, best_threshold = gain, t
    return best_threshold, best_gain

X = [[2.7], [1.3], [3.3], [7.6], [8.6], [7.7]]
y = ['no', 'no', 'no', 'yes', 'yes', 'yes']
threshold, gain = best_split(X, y, feature_idx=0)
print(threshold, round(gain, 3))  # 3.3  0.5
```

**Dry Run:** feature values `[2.7, 1.3, 3.3, 7.6, 8.6, 7.7]`, labels `[no,no,no,yes,yes,yes]`

- Base Gini impurity of the full set (3 "no", 3 "yes") = `1 - (0.5² + 0.5²) = 0.5`
- Try threshold `t=3.3`: left = `{2.7,1.3,3.3}` → all "no" (Gini=0); right = `{7.6,8.6,7.7}` → all "yes" (Gini=0)
- Weighted impurity after split = `0.5·0 + 0.5·0 = 0` → **information gain = 0.5 (maximum possible)** → this is the best split found

**Practical Use:**
- **Credit scoring, loan approval, medical diagnosis** — valued for being human-interpretable ("if income > X and age < Y, then...")
- **Feature importance analysis** — which inputs matter most for a prediction
- The **building block for ensemble methods**: Random Forest (bagging of trees) and Gradient Boosting/XGBoost/LightGBM (boosting of trees) — among the most-used models in real-world tabular ML

**Optimization:**
- **Pruning** (pre-pruning: max depth/min samples per leaf; post-pruning: trim after building) to prevent overfitting on training data
- Use **ensembles** — Random Forest or Gradient Boosting dramatically outperform a single tree by averaging out variance/bias
- Pre-sort feature values and use efficient split-finding (histogram-based binning, as XGBoost/LightGBM do) instead of scanning every threshold — brings split-finding from O(n²) to O(n log n) or better
- **Feature subsampling** per split (as in Random Forest) reduces correlation between trees and overfitting

---

### 5.7 Naive Bayes

**Explanation:**
A probabilistic classifier based on **Bayes' Theorem**, with the "naive" assumption that all features are conditionally independent given the class. Computes the posterior probability of each class and picks the highest.

**Code:**
```python
import numpy as np

def gaussian_prob(x, mean, var):
    eps = 1e-9
    coeff = 1 / np.sqrt(2 * np.pi * var + eps)
    exponent = np.exp(-((x - mean) ** 2) / (2 * var + eps))
    return coeff * exponent

def train_naive_bayes(X, y):
    classes = set(y)
    stats, priors = {}, {}
    for c in classes:
        X_c = np.array([X[i] for i in range(len(X)) if y[i] == c])
        stats[c] = (X_c.mean(axis=0), X_c.var(axis=0))
        priors[c] = len(X_c) / len(X)
    return stats, priors

def predict_naive_bayes(x, stats, priors):
    best_class, best_prob = None, -1
    for c, (mean, var) in stats.items():
        prob = priors[c]
        for i in range(len(x)):
            prob *= gaussian_prob(x[i], mean[i], var[i])
        if prob > best_prob:
            best_class, best_prob = c, prob
    return best_class

X = [[1.0,2.0],[1.5,1.8],[5.0,8.0],[6.0,9.0]]
y = ['A','A','B','B']
stats, priors = train_naive_bayes(X, y)
print(predict_naive_bayes([1.2, 1.9], stats, priors))  # 'A'
```

**Dry Run:** classes `A={[1.0,2.0],[1.5,1.8]}`, `B={[5.0,8.0],[6.0,9.0]}`, query `[1.2, 1.9]`

- Prior for A and B = 0.5 each (2 samples each out of 4)
- Class A's feature means are close to `[1.2, 1.9]` → high Gaussian probability under class A
- Class B's feature means (`~[5.5, 8.5]`) are far from the query → very low Gaussian probability under class B
- `P(A) × likelihood_A` ≫ `P(B) × likelihood_B` → **predicted class = 'A'**

**Practical Use:**
- **Spam filtering** — the classic textbook use case, extremely fast even on huge vocabularies
- **Sentiment analysis, document/news categorization**
- Real-time prediction systems where speed matters more than squeezing out the last bit of accuracy

**Optimization:**
- Use **log-probabilities** (sum of logs instead of product of probabilities) to avoid numerical underflow with many features
- **Laplace (additive) smoothing** to handle the "zero-frequency problem" (a feature value never seen in training for a class)
- **Feature selection** to remove highly correlated features, since they violate the independence assumption and can skew results
- For text, use **Multinomial Naive Bayes** with TF-IDF features instead of Gaussian NB (which assumes continuous, normally-distributed features)

---

### 5.8 Principal Component Analysis (PCA)

**Explanation:**
An **unsupervised dimensionality-reduction** technique. Finds new orthogonal axes (**principal components**) ordered by how much variance in the data they capture, then projects the data onto the top few components — compressing dimensions while preserving as much information as possible.

**Code:**
```python
import numpy as np

def pca(X, n_components=1):
    X_meaned = X - np.mean(X, axis=0)
    cov_matrix = np.cov(X_meaned, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    order = np.argsort(eigenvalues)[::-1]          # sort descending
    top_components = eigenvectors[:, order[:n_components]]
    return X_meaned @ top_components

X = np.array([[2,3],[3,4],[4,5],[5,6],[6,7]], dtype=float)
reduced = pca(X, n_components=1)
print(np.round(reduced.flatten(), 3))
# [-2.828 -1.414  0.     1.414  2.828]
```

**Dry Run:** 5 points lying almost exactly on the line `y = x + 1` (2D → 1D)

- Mean-center the data: subtract the column means
- Since all points lie almost perfectly on one diagonal direction, **one principal component captures ~100% of the variance**
- Projecting onto that single component collapses each 2D point to a single number, spaced evenly: `[-2.828, -1.414, 0, 1.414, 2.828]` — the *relative ordering and spacing* of the original points is fully preserved in 1 dimension instead of 2

**Practical Use:**
- **Dimensionality reduction** before training models — fewer features means faster training and less overfitting risk
- **Data visualization** — projecting high-dimensional data (e.g., 100 features) down to 2D/3D for plotting
- **Noise reduction** — discarding low-variance components often discards noise, not signal
- **Image compression / feature extraction** (e.g., Eigenfaces for face recognition)

**Optimization:**
- Use **SVD (Singular Value Decomposition)** instead of eigen-decomposition of the covariance matrix — more numerically stable, and what scikit-learn actually uses internally
- **Randomized PCA** — approximate the top-k components without computing the full decomposition, much faster for large, high-dimensional datasets
- Only compute the top-`k` components you need rather than the full decomposition when `k` is small
- Standardize/scale features first — PCA is sensitive to feature scale, since it operates on variance

---

### 5.9 Backpropagation (Neural Networks)

**Explanation:**
The algorithm that trains neural networks. A **forward pass** computes predictions layer by layer; a **backward pass** then uses the **chain rule** to compute how much each weight contributed to the error, propagating gradients from the output layer back to the input layer, and gradient descent updates the weights.

**Code:**
```python
import numpy as np
np.random.seed(1)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def train_nn(X, y, hidden_size=4, lr=0.5, epochs=5000):
    input_size, output_size = X.shape[1], 1
    W1 = np.random.randn(input_size, hidden_size)
    W2 = np.random.randn(hidden_size, output_size)
    for _ in range(epochs):
        # ---- forward pass ----
        a1 = sigmoid(X @ W1)
        a2 = sigmoid(a1 @ W2)
        # ---- backward pass (chain rule) ----
        error = a2 - y
        d2 = error * a2 * (1 - a2)          # gradient at output layer
        d1 = (d2 @ W2.T) * a1 * (1 - a1)    # gradient propagated to hidden layer
        W2 -= lr * a1.T @ d2
        W1 -= lr * X.T @ d1
    return W1, W2

X = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=float)
y = np.array([[0],[1],[1],[0]], dtype=float)   # XOR problem
W1, W2 = train_nn(X, y)
predictions = sigmoid(sigmoid(X @ W1) @ W2)
print(np.round(predictions.flatten(), 3))
# [0.044 0.965 0.96  0.036]  → correctly learns XOR (not linearly separable!)
```

**Dry Run:** learning the **XOR function** `[0,0]→0, [0,1]→1, [1,0]→1, [1,1]→0`

- XOR is **not linearly separable** — a single-layer model (like plain logistic regression) can never learn it
- **Forward pass**: input → hidden layer (sigmoid) → output layer (sigmoid) → prediction
- **Backward pass**: compute output error → propagate it backward through `W2` into the hidden layer → compute `W1`'s gradient via the chain rule
- After 5000 epochs of forward+backward+update: predictions converge to `[0.044, 0.965, 0.960, 0.036]` — correctly close to `[0, 1, 1, 0]` ✓, proving the hidden layer learned a non-linear decision boundary

**Practical Use:**
- **The foundation of all deep learning** — image recognition (CNNs), language models (Transformers), speech recognition, recommendation engines, generative AI
- Any task where the input-output relationship is too complex for linear models (non-linear boundaries, unstructured data like images/audio/text)

**Optimization:**
- **Vectorized batch processing** (as shown) instead of looping sample-by-sample — essential for GPU acceleration
- **ReLU activation** instead of sigmoid in hidden layers of deep networks — avoids the **vanishing gradient problem** that slows/stalls training in deep architectures
- **Adaptive optimizers** (Adam, RMSprop) instead of plain SGD — faster, more stable convergence
- **Batch Normalization** — normalizes activations between layers, allowing higher learning rates and faster training
- **Dropout / weight regularization (L2)** — reduces overfitting in large networks
- **GPU/TPU acceleration** — matrix multiplications in forward/backward passes parallelize extremely well on specialized hardware

---

## 6. Master Complexity Comparison Tables

### 6.1 Classical CS Algorithms

| Algorithm | Best Case (Time) | Average Case (Time) | Worst Case (Time) | Space Complexity | Stable? | In-Place? |
|---|---|---|---|---|---|---|
| Linear Search | O(1) | O(n) | O(n) | O(1) | — | — |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) iterative / O(log n) recursive | — | — |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) (call stack) | No | Yes |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes |
| BFS | O(V + E) | O(V + E) | O(V + E) | O(V) | — | — |
| DFS | O(V + E) | O(V + E) | O(V + E) | O(V) | — | — |
| Dijkstra's (binary heap) | O((V+E) log V) | O((V+E) log V) | O((V+E) log V) | O(V) | — | — |
| Fibonacci (memoized) | O(n) | O(n) | O(n) | O(n) (O(1) with tabulation) | — | — |
| 0/1 Knapsack (DP) | O(n·W) | O(n·W) | O(n·W) | O(n·W) (O(W) optimized) | — | — |
| LCS (DP) | O(m·n) | O(m·n) | O(m·n) | O(m·n) (O(min(m,n)) optimized) | — | — |

**Legend:**
- `n` = number of elements/items, `V` = number of vertices, `E` = number of edges, `W` = knapsack capacity, `m, n` (in LCS row) = lengths of the two strings
- **Stable** = equal elements retain their original relative order after sorting
- **In-Place** = uses O(1) or O(log n) auxiliary space (not counting input); "No" means it needs significant extra memory proportional to input size

---

### 6.2 AI / ML Algorithms

| Algorithm | Training Time | Prediction Time | Space Complexity | Learning Type |
|---|---|---|---|---|
| Gradient Descent | O(n·d·i) | — | O(d) | Optimization core |
| Linear Regression | O(n·d·i) (GD) / O(d³) (Normal Eq.) | O(d) | O(d) | Supervised |
| Logistic Regression | O(n·d·i) | O(d) | O(d) | Supervised |
| K-Nearest Neighbors | O(1) (lazy — no training) | O(n·d) brute force / O(d log n) w/ KD-Tree | O(n·d) | Supervised (instance-based) |
| K-Means Clustering | O(n·k·d·i) | O(k·d) | O(n·d) | Unsupervised |
| Decision Tree | O(n·d·log n) | O(depth) ≈ O(log n) | O(n) | Supervised |
| Naive Bayes | O(n·d) | O(d·c) | O(d·c) | Supervised |
| PCA | O(d²·n + d³) (covariance + eigen-decomp) | O(d·k) | O(d²) | Unsupervised |
| Backpropagation (NN) | O(n·i·W) | O(W) | O(W) | Supervised (deep learning) |

**Legend:**
- `n` = number of training samples, `d` = number of features/dimensions, `i` = number of iterations/epochs, `k` = number of clusters (K-Means) or neighbors (KNN) or reduced dimensions (PCA), `c` = number of classes, `W` = total number of weights/parameters in a neural network
- "Lazy learner" (KNN) means there is effectively no training phase — all computation happens at prediction time
- These complexities describe the algorithms **as implemented above from scratch**; production libraries (scikit-learn, XGBoost, PyTorch) use heavily optimized, often approximate or GPU-parallelized versions

---

### Quick Decision Guide

**Classical CS Tasks**

| If you need to... | Use |
|---|---|
| Search unsorted data | Linear Search |
| Search sorted data | Binary Search |
| Sort small/nearly-sorted data | Insertion Sort |
| Guarantee O(n log n) worst case | Merge Sort or Heap Sort |
| Sort in-place, fastest average case | Quick Sort |
| Find shortest path, unweighted graph | BFS |
| Detect cycles / topological order | DFS |
| Find shortest path, weighted graph (non-negative) | Dijkstra's |
| Solve "choose best combination under a constraint" | 0/1 Knapsack (DP) |
| Compare similarity between two sequences | LCS (DP) |

**AI / ML Tasks**

| If you need to... | Use |
|---|---|
| Minimize any differentiable loss function | Gradient Descent (and its variants: SGD, Adam) |
| Predict a continuous numeric value | Linear Regression |
| Predict a binary yes/no outcome | Logistic Regression |
| Classify based on similarity to known examples | K-Nearest Neighbors |
| Group unlabeled data into natural clusters | K-Means Clustering |
| Get an interpretable, rule-based classifier | Decision Tree |
| Classify fast with limited data / text classification | Naive Bayes |
| Reduce feature count / visualize high-dimensional data | PCA |
| Learn complex, non-linear patterns (images, text, audio) | Neural Network (Backpropagation) |
