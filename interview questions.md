# INTERVIEW QUESTIONS

### Cloud Science Labs

* Q1. Difference between 'WHERE' and 'HAVING' ?
The WHERE clause is used to filter records before any groupings are made, while the HAVING clause is used to filter records after the groupings have been made. In other words, WHERE is applied to individual rows, and HAVING is applied to groups of rows.

* Q2. What are the limitations of inheritance ?
Inheritance can lead to a rigid class hierarchy, making it difficult to modify or extend the code. It can also result in tight coupling between classes, where changes in the parent class can have unintended consequences in the child classes. Additionally, inheritance can make the code harder to understand and maintain, especially when dealing with complex hierarchies.

* Q3. Difference betweeen 'INNER JOIN' and 'LEFT JOIN' ?
An INNER JOIN returns only the rows that have matching values in both tables, while a LEFT JOIN returns all the rows from the left table and the matched rows from the right table. If there is no match, the result will contain NULL values for the columns from the right table.

* Q4. Write a query using inner join and left join ?
Here is an example of a query using INNER JOIN and LEFT JOIN:
```sql
SELECT employees.name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.id
LEFT JOIN salaries ON employees.id = salaries.employee_id;
```

### Exellence Technologies

* Q1. Differnce between asynchornus await() and promise ?
The main difference between asynchronous `await()` and Promises is in how they handle asynchronous operations.
- Promises are a way to handle asynchronous operations in JavaScript. They represent a value that may be available now, or in the future, or never. Promises have three states: pending, fulfilled, and rejected. You can use `.then()` and `.catch()` methods to handle the result of a Promise.
- `async/await` is a syntactic sugar built on top of Promises that allows you to write asynchronous code in a more synchronous manner. The `await` keyword can only be used inside an `async` function, and it pauses the execution of the function until the Promise is resolved or rejected. This makes the code easier to read and understand, as it resembles synchronous code.

* Q2. What is chunking and what are chunking strategies ?
Chunking is a technique used to break down large data sets or tasks into smaller, more manageable pieces, called chunks. This can improve performance, reduce memory usage, and make it easier to process data in parallel. Chunking strategies can vary depending on the context, but some common strategies include:
- Fixed-size chunking: Dividing the data into chunks of a fixed size, such as 1000 records per chunk.
- Dynamic chunking: Adjusting the chunk size based on the available resources or the characteristics of the data, such as splitting the data into chunks based on the number of available threads or the size of the data being processed.
- Overlapping chunking: Creating overlapping chunks to ensure that no data is missed during processing, which can be useful in certain scenarios where data dependencies exist between chunks.

* Q3. What is rank fusion and how it is used in search engines ?
Rank fusion is a technique used in search engines to combine the results of multiple ranking algorithms or models to produce a final ranking of search results. The idea is to leverage the strengths of different ranking methods to improve the overall quality of search results. Rank fusion can be used in various ways, such as
- Score-based fusion: Combining the scores from different ranking algorithms to produce a final score for each document, which is then used to rank the results.
- Rank-based fusion: Combining the ranks of documents from different ranking algorithms to produce a final ranking, often using methods like Borda count or reciprocal rank fusion.
- Hybrid fusion: Combining both score-based and rank-based fusion methods to produce a final ranking that takes into account both the scores and ranks of documents from different algorithms. This can help to improve the diversity and relevance of search results, as it allows for a more comprehensive evaluation of the documents    

* Q4. What are the chunking algorithms ?
Chunking algorithms are methods used to divide data into smaller, manageable pieces or chunks. These algorithms can vary based on the type of data and the specific requirements of the application. Some common chunking algorithms include:
- Fixed-size chunking: This algorithm divides the data into chunks of a predetermined size, regardless of the content or structure of the data. It is simple to implement but may not be optimal for all types of data, especially if the data has variable lengths or structures.
- Content-based chunking: This algorithm divides the data into chunks based on the content or structure of the data. For example, it may use delimiters, patterns, or specific markers within the data to determine where to create the chunks. This approach can be more efficient for certain types of data, such as text or structured data, as it takes into account the inherent characteristics of the data.
- Adaptive chunking: This algorithm dynamically adjusts the chunk size based on the characteristics of the data or the processing requirements. It may use heuristics or machine learning techniques to determine the optimal chunk size for a given dataset, allowing for more efficient processing and resource utilization. Adaptive chunking can be particularly useful in scenarios where the data is heterogeneous or has varying sizes, as it can help to balance the workload and improve performance.

* Q5. What is binary search , its code , its use cases and its limitations ?
Binary search is an efficient algorithm for finding a target value within a sorted array. It works by repeatedly dividing the search interval in half. If the target value is less than the middle element, the search continues in the lower half; otherwise, it continues in the upper half. This process is repeated until the target value is found or the search interval is empty.
Here is a simple implementation of binary search in Python:
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    return -1  # Target not found
```
Use cases of binary search:
- Searching in large sorted datasets, such as databases or arrays.
- Finding elements in sorted lists or arrays, such as in search engines or recommendation systems.
Limitations of binary search:
- The array must be sorted for binary search to work correctly.
- It is not suitable for unsorted data, as it relies on the order of elements to efficiently narrow down the search space.
- Binary search can be less efficient than other search algorithms for small datasets, as the overhead of dividing the search space may outweigh the benefits of the algorithm.

* Q6. What is MCP in the context of AI and its components ?
Model Context Protocol (MCP) is a framework used in the context of AI to define the structure and behavior of machine learning models. It provides a standardized way to represent models, their inputs, outputs, and the relationships between them. The components of MCP typically include:
- Model Definition: This component defines the architecture and parameters of the machine learning model, including the type of model (e.g., neural network, decision tree), the layers or nodes, and the hyperparameters used for training.
- Input/Output Specification: This component specifies the format and structure of the input data that the model expects, as well as the format of the output data produced by the model. It may include information about data types, shapes, and any preprocessing steps required for the input data.
- Training and Evaluation: This component outlines the procedures for training the model, including the training dataset, loss functions, optimization algorithms, and evaluation metrics used to assess the model's performance. It may also include information about validation and testing procedures to ensure the model generalizes well to unseen data.

* Q7. What are decorators in Python and how are they used ?
Decorators in Python are a powerful feature that allows you to modify the behavior of functions or classes without changing their code. They are essentially functions that take another function as an argument and return a new function that enhances or alters the original function's behavior. Decorators are often used for logging, access control, caching, and other cross-cutting concerns.
Here is an example of a simple decorator in Python:
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result
    return wrapper  

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")
    return f"Hello, {name}!"

# Usage
say_hello("Alice")
```
In this example, `my_decorator` is a decorator that wraps the `say_hello` function. When `say_hello` is called, the decorator adds behavior before and after the function execution, printing messages to the console. The `@my_decorator` syntax is a shorthand for applying the decorator to the function. Decorators can also be applied to classes and methods, allowing for more advanced use cases such as class-based decorators and method decorators.