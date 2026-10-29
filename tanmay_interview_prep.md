# 🚀 Tanmay Kushwaha — Complete Technical Interview Preparation Guide

> **Tailored for:** Python Developer · Backend Developer · FastAPI Developer · AI/LLM Engineer · SDE-1

---

## 📋 Table of Contents

1. [Core Python](#1-core-python)
2. [OOP & Design Principles](#2-oop--design-principles)
3. [Data Structures & Algorithms](#3-data-structures--algorithms)
4. [FastAPI & Backend Development](#4-fastapi--backend-development)
5. [Django & Django REST Framework](#5-django--django-rest-framework)
6. [REST API Design & Best Practices](#6-rest-api-design--best-practices)
7. [Authentication & Authorization](#7-authentication--authorization)
8. [Databases — PostgreSQL & SQL](#8-databases--postgresql--sql)
9. [System Design](#9-system-design)
10. [Docker & DevOps](#10-docker--devops)
11. [Cloud & Azure/AWS](#11-cloud--azureaws)
12. [AI / ML / GenAI / LLM Round](#12-ai--ml--genai--llm-round)
13. [LangChain, RAG & Vector Databases](#13-langchain-rag--vector-databases)
14. [Project Deep Dives](#14-project-deep-dives)
15. [Internship Deep Dives](#15-internship-deep-dives)
16. [System Design Round](#16-system-design-round)
17. [Mock Interview Section](#17-mock-interview-section)
18. [Rapid Fire Round](#18-rapid-fire-round)
19. [HR + Behavioral Questions](#19-hr--behavioral-questions)
20. [Final Revision Cheat Sheet](#20-final-revision-cheat-sheet)

---

## 🎯 Resume-Grounded Interview Focus

Use the questions below as the highest-priority revision path. Be precise about what you personally built, the measurable result, and how you validated it.

| Resume area | Interview themes to prepare |
|---|---|
| **TechAhead — OneWealth** | 50+ FastAPI endpoints, sub-150 ms average responses, JWT authentication, RBAC and advisor hierarchy, repository/service layers, Pydantic validation, async SQLAlchemy, and the reported 30% query-latency reduction |
| **LLM-Powered SQL Generator** | Five-stage agentic Text-to-SQL flow, hybrid keyword + pgvector retrieval, Retriever Strategy Pattern, SQL self-correction, query caching, prompt-injection reduction, and the 80% reduction in redundant LLM calls |
| **Exam Oracle** | Seven-stage orchestration, FastAPI/Celery/Redis, ChromaDB and sentence-transformer embeddings, RAG, multi-LLM fallback, supported exam domains, accuracy measurement, and hallucination reduction |
| **AI Voice Teller** | Gemini story generation, structured prompt hierarchy, Piper/TTS or Google TTS integration, asynchronous audio generation, Redis caching, Celery queues, Docker, and the latency improvement |
| **Webwright Solutions** | Founder/consultant responsibilities, workshops, client discovery, scope management, and delivering end-to-end web solutions |
| **Credentials and education** | MCA (IMS Engineering College), BCA (Invertis University), and AI/ML, Generative AI, and Python certifications |

**Interview discipline:** Treat resume metrics as claims you must be able to explain. For every percentage, state the baseline, measurement method, test conditions, and trade-offs. Do not claim production ownership for technologies or features that are not on the resume.

---

# 1. Core Python

## 1.1 Python Fundamentals

### [BEGINNER] Q1: What are Python's key features that make it suitable for backend development?

**Answer:**
Python is interpreted, dynamically typed, and supports multiple programming paradigms (OOP, functional, procedural). Key backend-relevant features:
- **Readability & maintainability:** Clean syntax reduces cognitive overhead in large codebases.
- **Rich ecosystem:** Libraries like FastAPI, SQLAlchemy, Celery, Pydantic cover the entire backend stack.
- **Async support:** `asyncio` enables non-blocking I/O — critical for high-throughput APIs.
- **Duck typing:** Enables flexible, loosely coupled designs.
- **GIL:** The Global Interpreter Lock limits true parallelism for CPU-bound tasks but async I/O mitigates this for network-bound work.

**Why Interviewers Ask This:** They want to know if you understand Python's fit vs. limitations, not just that you "like" it.

**Common Mistakes:** Claiming Python is the fastest language, or not knowing about the GIL.

**Follow-Up Questions:**
- What is the GIL and why does it exist?

GIL is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecode simultaneously. It exists to simplify memory management and ensure thread safety in CPython, but it limits multi-threaded performance for CPU-bound tasks.

- How do you handle CPU-bound tasks in Python?

For CPU-bound tasks, you can use multiprocessing (via `multiprocessing` module or `ProcessPoolExecutor`) to bypass the GIL by running code in separate processes. Alternatively, for certain workloads, you might use C extensions or libraries like NumPy that release the GIL.

- When would you choose Python over Java or Go?

Python is ideal for rapid development, prototyping, and when you need a rich ecosystem of libraries (e.g., for AI/ML). It's also great for teams that prioritize developer productivity and readability. Java or Go might be better choices for performance-critical applications or when you need strong static typing and concurrency primitives out of the box.


**Production Example:** At your internship (TECHAHEAD/OneWealth), you chose Python + FastAPI over alternatives because of rapid development speed, async capabilities, and the mature SQLAlchemy ORM ecosystem.

**Best Practices:** Use Python 3.10+ for pattern matching, better type hints, and `asyncio` improvements.

---

### [INTERMEDIATE] Q2: Explain Python's memory management and garbage collection.

**Answer:**
Python uses **reference counting** as its primary memory management strategy. Every object maintains a count of references pointing to it. When the count reaches zero, the memory is immediately freed.

```python
import sys
x = [1, 2, 3]
print(sys.getrefcount(x))  # Usually 2 (one for x, one for getrefcount argument)
```

**Problem with reference counting — circular references:**
```python
a = []
b = []
a.append(b)
b.append(a)
del a, b  # ref count never hits 0 — memory leak without GC
```

Python's **cyclic garbage collector** (gc module) runs periodically to detect and collect these cycles. It uses a **generational** approach:
- **Gen 0:** New objects — collected most frequently.
- **Gen 1:** Survived one collection.
- **Gen 2:** Long-lived objects — collected rarely.

**Why Interviewers Ask This:** Backend systems with long-running processes (FastAPI, Celery workers) must not leak memory. Understanding GC helps you write leak-free code.

**Common Mistakes:** Thinking `del` immediately frees memory, or not knowing about `__del__` pitfalls.

**Follow-Up Questions:**
- How do you detect memory leaks in Python?

You can use the `tracemalloc` module to track memory allocations and identify leaks. Tools like `objgraph` can visualize object references to find unexpected growth in certain types.

- What is `__slots__` and how does it save memory?

`__slots__` is a class variable that defines a fixed set of attributes for instances, preventing the creation of the default `__dict__` for each instance. This can save memory when creating many instances of a class, as it avoids the overhead of the dynamic attribute dictionary.


- How does `weakref` help with circular reference problems?

The `weakref` module allows you to create weak references to objects, which do not increase the reference count. This is useful for callback registries or caches where you don't want the reference to prevent garbage collection.

```python

**Production Example:** In long-running Celery workers (like your Exam Oracle project), uncollected circular references in large prompt/response objects can cause OOM crashes. You'd use `gc.collect()` checkpoints or `weakref` for callback registries.

**Best Practices:**
- Use `tracemalloc` for profiling memory.
- Prefer generators over lists for large data streams.
- Use `__slots__` in high-frequency data classes.

---

### [INTERMEDIATE] Q3: What are decorators in Python? Write a practical example.

**Answer:**
A decorator is a higher-order function that wraps another function to extend its behavior without modifying it. This is the **Open/Closed Principle** in action.

```python
import time
import functools
import logging

logger = logging.getLogger(__name__)

def log_execution_time(func):
    @functools.wraps(func)  # Preserves original function metadata
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        logger.info(f"{func.__name__} executed in {elapsed:.4f}s")
        return result
    return wrapper

# Usage in FastAPI
@log_execution_time
async def get_user_portfolio(user_id: int):
    # DB call
    ...
```

**Stacking decorators:**
```python
@app.get("/users/{user_id}")
@require_auth
@log_execution_time
async def get_user(user_id: int):
    ...
# Execution order: log_execution_time → require_auth → get_user (bottom-up application, top-down execution)
```

**Why Interviewers Ask This:** FastAPI itself is decorator-heavy. Understanding decorators means you can write reusable middleware logic, auth guards, retry logic, and caching layers.

**Common Mistakes:** Forgetting `@functools.wraps`, which causes `__name__` and `__doc__` to be lost. Also confusing application order with execution order.

**Follow-Up Questions:**
- What is `functools.wraps` and why is it important?

`functools.wraps` is a decorator for decorators. It updates the wrapper function to look like the original function by copying attributes such as `__name__`, `__doc__`, and `__module__`. This is important for debugging, introspection, and tools that rely on function metadata.

- Write a retry decorator with exponential backoff.
```python
import asyncio
import random

def retry(max_attempts: int, backoff_factor: float = 1.0):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    wait_time = backoff_factor * (2 ** attempt) + random.uniform(0, 1)
                    await asyncio.sleep(wait_time)
        return wrapper
    return decorator
```

- How do class-based decorators differ from function decorators?
Class-based decorators are implemented as classes that define a `__call__` method, allowing instances of the class to be used as decorators. This can be useful when you need to maintain state across multiple calls or want to provide additional methods.

```pythonclass LogExecutionTime:
    def __init__(self, logger):
        self.logger = logger

    def __call__(self, func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = await func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            self.logger.info(f"{func.__name__} executed in {elapsed:.4f}s")
            return result
        return wrapper
```


- What is `@property` internally?

`@property` is a built-in decorator that turns a method into a "getter" for a read-only attribute. Internally, it creates a property object that manages access to the method. You can also define setters and deleters using `@<property_name>.setter` and `@<property_name>.deleter`.

```pythonclass User:
    def __init__(self, email):
        self._email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        self._email = value
``` 

**Production Example:** In OneWealth, you'd use a decorator for `@require_advisor_role` to enforce RBAC at the function level cleanly.

---

### [INTERMEDIATE] Q4: Explain generators and when to use them over lists.

**Answer:**
A generator is a lazy iterator — it produces values one at a time on demand using `yield`, without loading everything into memory.

```python
# List — loads all 1M records into memory
def get_all_users_list():
    return [fetch_user(i) for i in range(1_000_000)]

# Generator — yields one at a time
def get_all_users_gen():
    for i in range(1_000_000):
        yield fetch_user(i)

# Usage
for user in get_all_users_gen():
    process(user)
```

**Generator expressions:**
```python
total = sum(user['score'] for user in get_all_users_gen())  # Memory efficient
```

**Send values into generators:**
```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

gen = accumulator()
next(gen)       # Prime the generator
gen.send(10)    # total = 10
gen.send(20)    # total = 30
```

**Why Interviewers Ask This:** Processing large datasets in Exam Oracle and retrieving schema/context for the SQL Generator requires memory-efficient patterns.

**Common Mistakes:** Trying to reuse a consumed generator; using lists when datasets are large.

**Follow-Up Questions:**
- What is the difference between `yield` and `yield from`?

`yield` produces a value from the generator, while `yield from` is used to delegate part of the generator's operations to another generator. It allows you to yield all values from a sub-generator without needing an explicit loop.

```pythondef sub_generator():
    yield 1
    yield 2
def main_generator():
    yield from sub_generator()  # Delegates to sub_generator
    yield 3
```



- How do async generators work?

Async generators are defined with `async def` and use `yield` to produce values. They can be iterated over using `async for`, allowing for asynchronous iteration over data streams.

```pythonasync def async_gen():
    for i in range(5):
        await asyncio.sleep(1)  # Simulate async work
        yield i
```

- When would you use `itertools` instead of a generator?

The `itertools` module provides a collection of fast, memory-efficient tools for creating iterators. You would use `itertools` when you need to perform complex iteration patterns (like permutations, combinations, or infinite sequences) that are not easily implemented with simple generators.

```pythonfrom itertools import count, cycle
# Infinite counter
for i in count(1):
    print(i)
    if i >= 5:
        break
```
---

### [ADVANCED] Q5: Explain `asyncio`, the event loop, and `async/await` in depth.

**Answer:**
Python's `asyncio` implements **cooperative multitasking** using an event loop. It is single-threaded but achieves concurrency by suspending coroutines at I/O boundaries.

**Core concepts:**
- **Coroutine:** A function defined with `async def`. It pauses at `await` points.
- **Event Loop:** Manages scheduling of coroutines. Only one coroutine runs at a time.
- **Task:** A scheduled coroutine wrapped to run concurrently.
- **Future:** A placeholder for a value not yet available.

```python
import asyncio
import httpx

async def fetch_data(url: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)  # Suspends here, event loop runs other tasks
        return response.json()

async def main():
    # Sequential: 3 seconds total if each takes 1s
    # result1 = await fetch_data(url1)
    # result2 = await fetch_data(url2)

    # Concurrent: ~1 second total
    results = await asyncio.gather(
        fetch_data("https://api.example.com/user/1"),
        fetch_data("https://api.example.com/user/2"),
        fetch_data("https://api.example.com/user/3"),
    )
    return results

asyncio.run(main())
```

**FastAPI's async model:**
FastAPI runs on `uvicorn` (ASGI server) which provides the event loop. Each request becomes a task.

```python
@app.get("/portfolio")
async def get_portfolio(user_id: int, db: AsyncSession = Depends(get_db)):
    # This suspends and lets other requests run while waiting for DB
    portfolio = await db.execute(select(Portfolio).where(Portfolio.user_id == user_id))
    return portfolio.scalars().all()
```

**Blocking calls in async context — the danger:**
```python
# BAD — blocks the entire event loop
@app.get("/data")
async def bad_endpoint():
    time.sleep(5)  # Blocks ALL other requests for 5 seconds!

# GOOD — run blocking code in thread pool
@app.get("/data")
async def good_endpoint():
    result = await asyncio.get_event_loop().run_in_executor(None, blocking_function)
    return result
```

**Why Interviewers Ask This:** FastAPI is async-first. If you don't understand the event loop, you'll accidentally block it and destroy performance.

**Common Mistakes:**
- Using `time.sleep()` instead of `asyncio.sleep()` in async functions.

 This blocks the entire event loop, preventing other tasks from running and causing performance issues.

- Calling sync DB operations in async endpoints without `run_in_executor`.

This can lead to blocking the event loop, resulting in slow response times and unresponsive APIs.

- Not understanding that `asyncio.gather` is concurrent but NOT parallel. It runs coroutines concurrently in the same thread, so CPU-bound tasks won't benefit.

**Follow-Up Questions:**
- What is the difference between concurrency and parallelism?

Concurrency is about dealing with multiple tasks at the same time (interleaving), while parallelism is about doing multiple tasks simultaneously (using multiple CPU cores). `asyncio` provides concurrency, not parallelism.

- How does `asyncio.gather` differ from `asyncio.wait`?

`asyncio.gather` runs multiple coroutines concurrently and returns their results in order. If any coroutine raises an exception, `gather` will raise immediately. `asyncio.wait` allows you to wait for a set of coroutines to complete, but it doesn't return results in order and can be configured to return when the first coroutine completes or when all complete.

- When would you use `ThreadPoolExecutor` vs `ProcessPoolExecutor`?

Use `ThreadPoolExecutor` for I/O-bound tasks that release the GIL (like network calls or file I/O). Use `ProcessPoolExecutor` for CPU-bound tasks that need to bypass the GIL for true parallelism (like data processing or ML inference).

- How does FastAPI handle sync vs async endpoints internally?

FastAPI detects whether an endpoint is defined as `async def` or `def`. For `async def`, it runs the function as a coroutine in the event loop. For `def`, it runs the function in a thread pool using `run_in_executor` to avoid blocking the event loop. This allows FastAPI to support both sync and async code seamlessly.

---

### [ADVANCED] Q6: Context Managers — `__enter__`, `__exit__`, and `contextlib`.

**Answer:**
Context managers manage resources (files, DB connections, locks) ensuring cleanup happens even if exceptions occur.

```python
# Class-based context manager
class DatabaseTransaction:
    def __init__(self, session):
        self.session = session

    def __enter__(self):
        self.session.begin()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
            return False  # Re-raise the exception
        self.session.commit()
        return True

# Usage
with DatabaseTransaction(session) as txn:
    txn.execute(insert_query)
    # If exception here → rollback; else → commit
```

**Using `contextlib.contextmanager`:**
```python
from contextlib import contextmanager, asynccontextmanager

@asynccontextmanager
async def get_db_session():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise

# FastAPI dependency
async def get_db():
    async with get_db_session() as session:
        yield session
```

**Why Interviewers Ask This:** Your OneWealth project uses transactional DB handling — context managers are the idiomatic way to implement this.

**Follow-Up Questions:**
- What happens if `__exit__` returns `True`? What if it returns `False`?

If `__exit__` returns `True`, it indicates that the exception has been handled and should not be propagated. If it returns `False` (or `None`), the exception will be re-raised after the context manager exits.

- How do you nest context managers using `contextlib.ExitStack`?
`ExitStack` allows you to manage a dynamic number of context managers. You can enter multiple context managers and ensure they are all properly exited, even if an exception occurs.

```pythonfrom contextlib import ExitStack
with ExitStack() as stack:
    file1 = stack.enter_context(open('file1.txt'))
    file2 = stack.enter_context(open('file2.txt'))
    # Both files will be properly closed when the block exits
```

- How does `asynccontextmanager` differ from a regular contextmanager?
`asynccontextmanager` is designed for asynchronous context managers. It allows you to use `async with` syntax and supports `await` within the context manager's body. Regular `contextmanager` is for synchronous context managers and does not support asynchronous operations.

```python@asynccontextmanager
async def async_resource_manager():
    resource = await acquire_resource()
    try:
        yield resource
    finally:
        await release_resource(resource)
``` 


---

## 1.2 Exception Handling

### [INTERMEDIATE] Q7: Best practices for exception handling in production FastAPI applications.

**Answer:**

```python
# Custom exception hierarchy
class AppException(Exception):
    def __init__(self, message: str, status_code: int = 500, error_code: str = "INTERNAL_ERROR"):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        super().__init__(message)

class UserNotFoundException(AppException):
    def __init__(self, user_id: int):
        super().__init__(
            message=f"User {user_id} not found",
            status_code=404,
            error_code="USER_NOT_FOUND"
        )

class UnauthorizedException(AppException):
    def __init__(self):
        super().__init__(
            message="Unauthorized access",
            status_code=401,
            error_code="UNAUTHORIZED"
        )

# Global exception handler in FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error_code": exc.error_code,
            "message": exc.message,
        }
    )

# Endpoint — clean, no try/except noise
@app.get("/users/{user_id}")
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await user_repository.get_by_id(db, user_id)
    if not user:
        raise UserNotFoundException(user_id)
    return user
```

**Why Interviewers Ask This:** Production APIs must return structured errors, not raw stack traces. Your OneWealth project explicitly required standardized API response structures.

**Common Mistakes:** Bare `except:` clauses, swallowing exceptions silently, returning 500 for client errors.

**Follow-Up Questions:**
- What is the difference between `Exception` and `BaseException`?

`BaseException` is the base class for all exceptions in Python, including system-exiting exceptions like `SystemExit`, `KeyboardInterrupt`, and `GeneratorExit`. `Exception` is a subclass of `BaseException` and is the base class for all non-system-exiting exceptions. You should generally catch `Exception` rather than `BaseException` to avoid catching system-exiting exceptions unintentionally.

- How do you log exceptions without exposing sensitive stack traces to clients?
You can use Python's `logging` module to log exceptions on the server side while returning a generic error message to clients. In your global exception handler, you can log the exception details and return a sanitized response.

```pythonimport logging
logger = logging.getLogger(__name__)
@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    logger.error(f"Error occurred: {exc.message}", exc_info=exc)
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error_code": exc.error_code,
            "message": exc.message,
        }
    )
``` 

- What is `ExceptionGroup` in Python 3.11?
`ExceptionGroup` is a new exception type introduced in Python 3.11 that allows you to group multiple exceptions together. This is particularly useful in concurrent programming where multiple exceptions may occur simultaneously. You can catch an `ExceptionGroup` and handle each individual exception within it.

```pythontry:
    # Some concurrent operations that may raise multiple exceptions
except ExceptionGroup as eg:
    for exc in eg.exceptions:
        logger.error(f"Individual exception: {exc}", exc_info=exc)
``` 

---

## 1.3 Multithreading, Multiprocessing & Async

### [ADVANCED] Q8: When do you use threading vs multiprocessing vs asyncio?

**Answer:**

| Scenario | Best Choice | Reason |
|---|---|---|
| I/O-bound: DB queries, HTTP calls, file I/O | `asyncio` | No threads needed; event loop handles concurrency efficiently |
| I/O-bound legacy sync code | `ThreadPoolExecutor` | Threads release GIL during I/O |
| CPU-bound: image processing, ML inference | `ProcessPoolExecutor` or `multiprocessing` | Bypasses GIL with separate processes |
| Background tasks in FastAPI | `BackgroundTasks` or Celery | Depends on complexity and persistence needs |

```python
# asyncio — best for FastAPI endpoints (I/O-bound)
@app.get("/data")
async def get_data():
    result = await some_async_db_call()
    return result

# ThreadPoolExecutor — for blocking sync libraries
import asyncio
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=4)

@app.get("/pdf")
async def process_pdf(file_path: str):
    loop = asyncio.get_event_loop()
    # pdfplumber is synchronous — run in thread pool
    result = await loop.run_in_executor(executor, extract_pdf_text, file_path)
    return result

# Celery — for long-running background tasks (like in Exam Oracle)
from celery import Celery

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def run_exam_prediction_pipeline(exam_type: str, user_id: int):
    # Runs in separate Celery worker process
    pipeline = ExamPredictionPipeline(exam_type)
    return pipeline.run()
```

**Why Interviewers Ask This:** Your Exam Oracle project uses Celery + Redis for exactly this — CPU-intensive agent pipelines running asynchronously.

**Follow-Up Questions:**
- What is the GIL and how does it affect threading?

GIL (Global Interpreter Lock) is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecode simultaneously. This means that even if you have multiple threads, only one can execute Python code at a time, which limits the performance of CPU-bound tasks in multi-threaded programs.

- How does `concurrent.futures` simplify thread/process pool usage?

The `concurrent.futures` module provides a high-level interface for asynchronously executing callables using threads or processes. It abstracts away the complexities of managing thread/process lifecycles and provides a simple API for submitting tasks and retrieving results.

- What is Celery's architecture? What is a broker vs backend?
Celery's architecture consists of workers, a message broker, and a result backend. The **broker** (like Redis or RabbitMQ) is responsible for receiving and distributing tasks to workers. The **backend** (like Redis, database, or RPC) is used to store the results of completed tasks so that they can be retrieved later.


---

# 2. OOP & Design Principles

## 2.1 Object-Oriented Programming

### [BEGINNER] Q9: Explain the four pillars of OOP with Python examples relevant to backend systems.

**Answer:**

**1. Encapsulation** — Bundle data and methods; control access. 

```python
class UserAccount:
    def __init__(self, email: str, password: str):
        self._email = email
        self.__password_hash = self._hash_password(password)  # Private

    @property
    def email(self):
        return self._email

    def verify_password(self, plain_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode(), self.__password_hash)

    def _hash_password(self, plain: str) -> bytes:
        return bcrypt.hashpw(plain.encode(), bcrypt.gensalt())
```

**2. Inheritance** — Reuse and extend behavior.
```python
class BaseRepository:
    def __init__(self, model, session: AsyncSession):
        self.model = model
        self.session = session

    async def get_by_id(self, id: int):
        return await self.session.get(self.model, id)

    async def save(self, obj):
        self.session.add(obj)
        await self.session.flush()
        return obj

class UserRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(User, session)

    async def get_by_email(self, email: str):
        result = await self.session.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()
```

**3. Polymorphism** — Same interface, different behavior.
```python
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    async def send(self, recipient: str, message: str) -> bool:
        pass

class EmailNotificationService(NotificationService):
    async def send(self, recipient: str, message: str) -> bool:
        # Send email via SMTP
        return True

class SMSNotificationService(NotificationService):
    async def send(self, recipient: str, message: str) -> bool:
        # Send SMS via Twilio
        return True

# Client code is polymorphic — works with any NotificationService
async def notify_user(service: NotificationService, user_email: str, msg: str):
    await service.send(user_email, msg)
```

**4. Abstraction** — Hide implementation details.
```python
class PaymentProcessor(ABC):
    @abstractmethod
    async def charge(self, amount: float, currency: str) -> str:  # Returns transaction_id
        pass

    @abstractmethod
    async def refund(self, transaction_id: str) -> bool:
        pass
```

**Why Interviewers Ask This:** Your OneWealth project explicitly uses service-layer and repository architecture patterns — pure OOP in practice.

---

## 2.2 SOLID Principles

### [INTERMEDIATE] Q10: Explain all SOLID principles with code examples from a backend context.

**Answer:**

**S — Single Responsibility Principle:**
Each class/module has one reason to change.
```python
# BAD — UserService doing too much
class UserService:
    def create_user(self, data): ...
    def send_welcome_email(self, user): ...  # Should be EmailService
    def log_creation(self, user): ...         # Should be LoggingService
    def hash_password(self, pwd): ...         # Should be PasswordHasher

# GOOD
class UserService:
    def __init__(self, user_repo, email_service, password_hasher):
        self.repo = user_repo
        self.email = email_service
        self.hasher = password_hasher

    async def create_user(self, data: UserCreateSchema) -> User:
        hashed = self.hasher.hash(data.password)
        user = await self.repo.create(email=data.email, password_hash=hashed)
        await self.email.send_welcome(user)
        return user
```

**O — Open/Closed Principle:**
Open for extension, closed for modification.
```python
# Use strategy pattern instead of if/elif chains
class AuthStrategy(ABC):
    @abstractmethod
    async def authenticate(self, credentials: dict) -> User:
        pass

class JWTAuthStrategy(AuthStrategy): ...
class OAuth2Strategy(AuthStrategy): ...
class APIKeyStrategy(AuthStrategy): ...

# Adding a new auth method doesn't modify existing code
```

**L — Liskov Substitution Principle:**
Subclasses must be substitutable for their base class.
```python
class BaseCache(ABC):
    @abstractmethod
    async def get(self, key: str) -> Optional[str]: pass
    @abstractmethod
    async def set(self, key: str, value: str, ttl: int) -> None: pass

class RedisCache(BaseCache): ...
class InMemoryCache(BaseCache): ...  # For testing — LSP: swappable in tests
```

**I — Interface Segregation Principle:**
Clients shouldn't be forced to depend on interfaces they don't use.
```python
# BAD — fat interface
class StorageService(ABC):
    def upload(self): pass
    def download(self): pass
    def delete(self): pass
    def list_objects(self): pass
    def generate_presigned_url(self): pass

# GOOD — segregated interfaces
class Uploadable(ABC):
    @abstractmethod
    async def upload(self, file: bytes, key: str) -> str: pass

class Downloadable(ABC):
    @abstractmethod
    async def download(self, key: str) -> bytes: pass
```

**D — Dependency Inversion Principle:**
Depend on abstractions, not concretions. (FastAPI's `Depends()` is built on this.)
```python
# HIGH-LEVEL MODULE depends on ABSTRACTION
class OnboardingService:
    def __init__(
        self,
        user_repo: BaseUserRepository,  # Abstraction
        email_service: BaseEmailService,  # Abstraction
        storage: Uploadable              # Abstraction
    ):
        self.user_repo = user_repo
        self.email_service = email_service
        self.storage = storage

# FastAPI DI wiring
def get_onboarding_service(db: AsyncSession = Depends(get_db)) -> OnboardingService:
    return OnboardingService(
        user_repo=UserRepository(db),
        email_service=SendgridEmailService(),
        storage=ObjectStorage()
    )
```

**Why Interviewers Ask This:** Your OneWealth work (repository + service-layer patterns) is a direct application of SOLID. Interviewers at product companies love this question.

---

## 2.3 Design Patterns

### [INTERMEDIATE] Q11: Explain the Repository Pattern — why you use it and how it works.

**Answer:**
The **Repository Pattern** abstracts the data access layer. Service classes work with repository interfaces, not directly with the database. This provides:
- Separation of concerns
- Testability (mock the repository in unit tests)
- Flexibility (swap PostgreSQL for MongoDB without touching service logic)

```python
# Base Repository
from typing import TypeVar, Generic, Type, Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.model = model
        self.session = session

    async def get(self, id: int) -> Optional[ModelType]:
        return await self.session.get(self.model, id)

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        result = await self.session.execute(
            select(self.model).offset(skip).limit(limit)
        )
        return result.scalars().all()

    async def create(self, **kwargs) -> ModelType:
        obj = self.model(**kwargs)
        self.session.add(obj)
        await self.session.flush()
        await self.session.refresh(obj)
        return obj

    async def delete(self, id: int) -> bool:
        obj = await self.get(id)
        if not obj:
            return False
        await self.session.delete(obj)
        return True

# Concrete Repository
class AdvisorRepository(BaseRepository[Advisor]):
    def __init__(self, session: AsyncSession):
        super().__init__(Advisor, session)

    async def get_by_firm(self, firm_id: int) -> List[Advisor]:
        result = await self.session.execute(
            select(Advisor)
            .where(Advisor.firm_id == firm_id)
            .where(Advisor.is_active == True)
        )
        return result.scalars().all()

    async def get_hierarchy(self, root_advisor_id: int) -> List[Advisor]:
        # Recursive CTE for hierarchy traversal
        ...
```

**Why Interviewers Ask This:** Your resume explicitly mentions "async repository patterns" from your OneWealth internship. Expect deep questions here.

**Follow-Up Questions:**
- How do you handle transactions spanning multiple repositories?

transactions that span multiple repositories can be managed using a **Unit of Work** pattern, which coordinates the work of multiple repositories by maintaining a list of objects affected by a business transaction and coordinating the writing out of changes and the resolution of concurrency problems.

- Unit of Work pattern — how does it relate to Repository?

Unit of Work is a design pattern that maintains a list of objects affected by a business transaction and coordinates the writing out of changes. It works alongside the Repository pattern to ensure that all changes across multiple repositories are committed or rolled back together, maintaining data integrity.

```pythonclass UnitOfWork:
    def __init__(self, session: AsyncSession):
        self.session = session
        self._repositories = {}
        self._new_objects = []
        self._dirty_objects = []
        self._removed_objects = []
        def get_repository(self, repo_class):
        if repo_class not in self._repositories:
            self._repositories[repo_class] = repo_class(self.session)
        return self._repositories[repo_class]
        async def commit(self):
        try:
            await self.session.commit()
        except Exception as e:
            await self.session.rollback()
            raise e
```



- How would you mock repositories for unit testing?

Unit testing repositories can be done by creating mock classes that implement the same interface as the actual repository. You can use libraries like `unittest.mock` to create mock objects and define their behavior for testing purposes.



---

### [ADVANCED] Q12: Explain other design patterns relevant to your projects.

**Answer:**

**Factory Pattern** — Object creation without specifying exact class:
```python
class LLMFactory:
    @staticmethod
    def create(provider: str) -> BaseLLM:
        providers = {
            "groq": GroqLLM,
            "gemini": GeminiLLM,
            "ollama": OllamaLLM,
        }
        if provider not in providers:
            raise ValueError(f"Unknown LLM provider: {provider}")
        return providers[provider]()

# Exam Oracle's multi-LLM cascade uses this pattern
llm = LLMFactory.create("groq")
```

**Strategy Pattern** — Runtime algorithm selection:
```python
class EmbeddingStrategy(ABC):
    @abstractmethod
    def embed(self, text: str) -> List[float]: pass

class SentenceTransformerStrategy(EmbeddingStrategy):
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed(self, text: str) -> List[float]:
        return self.model.encode(text).tolist()

class OpenAIEmbeddingStrategy(EmbeddingStrategy):
    def embed(self, text: str) -> List[float]: ...
```

**Observer Pattern** — Event-driven architecture:
```python
class EventBus:
    def __init__(self):
        self._subscribers: dict[str, list] = {}

    def subscribe(self, event_type: str, handler):
        self._subscribers.setdefault(event_type, []).append(handler)

    async def publish(self, event_type: str, payload: dict):
        for handler in self._subscribers.get(event_type, []):
            await handler(payload)

event_bus = EventBus()
event_bus.subscribe("user.registered", send_welcome_email)
event_bus.subscribe("user.registered", create_default_portfolio)
```

---

# 3. Data Structures & Algorithms

### [INTERMEDIATE] Q13: What data structures does Python provide, and when do you use each?

**Answer:**

| Structure | Python Type | Use Case | Time Complexity (avg) |
|---|---|---|---|
| Dynamic Array | `list` | Ordered collection, random access | O(1) access, O(n) insert |
| Hash Map | `dict` | Key-value lookup, caching | O(1) get/set |
| Hash Set | `set` | Uniqueness checks, fast membership | O(1) lookup |
| Double-ended Queue | `collections.deque` | Efficient prepend/append | O(1) both ends |
| Priority Queue | `heapq` | Min/max retrieval, scheduling | O(log n) push/pop |
| Ordered Dict | `collections.OrderedDict` | LRU cache implementation | O(1) get/set |
| Named Tuple | `collections.namedtuple` | Lightweight immutable objects | O(1) access |
| Counter | `collections.Counter` | Frequency analysis | O(n) build |

**Real examples from your projects:**

```python
# Exam Oracle: Counter for topic frequency analysis
from collections import Counter

def analyze_topic_frequency(past_papers: list[dict]) -> dict:
    topic_counter = Counter()
    for paper in past_papers:
        for question in paper['questions']:
            topic_counter[question['topic']] += 1
    return dict(topic_counter.most_common(20))

# Deque for sliding window (ARIMA preprocessing)
from collections import deque
window = deque(maxlen=5)  # Auto-drops oldest when full
for data_point in time_series:
    window.append(data_point)
    if len(window) == 5:
        process_window(list(window))
```

**Follow-Up Questions:**
- Implement an LRU cache without `functools.lru_cache`.
- How does Python's `dict` maintain insertion order since 3.7?
- When would you use a `defaultdict` vs a regular `dict`?

---

### [INTERMEDIATE] Q14: Explain Big-O notation and analyze the complexity of common operations.

**Answer:**

```python
# O(1) — Hash map lookup
user_cache = {"user_123": user_object}
user = user_cache.get("user_123")  # O(1)

# O(log n) — Binary search
import bisect
sorted_scores = [10, 20, 30, 40, 50]
pos = bisect.bisect_left(sorted_scores, 35)  # O(log n) — find insertion point
#bisect_left returns the index where 35 should be inserted to maintain order.

# O(n) — Linear scan
def find_user_by_email(users: list, email: str):
    for user in users:           # O(n)
        if user.email == email:
            return user

# O(n log n) — Sorting
sorted_users = sorted(users, key=lambda u: u.created_at)  # O(n log n) — Timsort

# O(n²) — Nested loops — avoid in production!
def find_duplicate_pairs(items: list):
    pairs = []
    for i in range(len(items)):         # O(n)
        for j in range(i+1, len(items)): # O(n)
            if items[i] == items[j]:
                pairs.append((i, j))
    return pairs  # O(n²) total — use set instead!

# Better approach: O(n)
def find_duplicates_fast(items: list):
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return duplicates
```

**Why Interviewers Ask This:** SDE-1 roles at product companies almost always include DSA. Even backend-focused roles test algorithmic thinking.

---

# 4. FastAPI & Backend Development

## 4.1 FastAPI Core

### [BEGINNER] Q15: What is FastAPI and why is it preferred for building modern APIs?

**Answer:**
FastAPI is a modern, high-performance Python web framework for building APIs based on Python type hints. Key advantages:

- **Performance:** Built on Starlette (ASGI) and Uvicorn. Comparable to Node.js and Go in benchmarks.
- **Automatic docs:** Generates Swagger UI (`/docs`) and ReDoc (`/redoc`) from type annotations — zero extra work.
- **Type safety:** Pydantic integration provides request/response validation at runtime.
- **Native async:** Built async-first, unlike Django which bolted async on later.
- **Dependency Injection:** Clean, testable DI system via `Depends()`.
- **OpenAPI compliance:** Automatic OpenAPI 3.0 schema generation.

```python
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI(title="OneWealth API", version="1.0.0")

class UserCreateRequest(BaseModel):
    email: EmailStr
    full_name: str
    password: str
    role: str = "client"

class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str
    is_active: bool

    class Config:
        from_attributes = True  # Pydantic v2 (replaces orm_mode)

@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    request: UserCreateRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    user = await user_service.create(db, request)
    return user
```

**Why Interviewers Ask This:** Your primary framework — they'll want depth, not surface-level answers.

**Follow-Up Questions:**
- How does FastAPI handle request validation errors?


- What is the difference between `APIRouter` and the main `app`?
- How does FastAPI compare to Flask and Django REST Framework?

---

### [INTERMEDIATE] Q16: Explain FastAPI's Dependency Injection system in depth.

**Answer:**
FastAPI's `Depends()` is a declarative DI system. Dependencies are callables (functions or classes) that FastAPI automatically resolves and injects.

```python
from fastapi import Depends, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

# Dependency: Extract & validate JWT token
async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Security(security),
    db: AsyncSession = Depends(get_db)
) -> User:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("sub")
        if not user_id:
            raise UnauthorizedException()
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    
    user = await user_repository.get(db, int(user_id))
    if not user or not user.is_active:
        raise UnauthorizedException()
    return user

# Dependency: Role-based access
def require_role(*roles: str):
    async def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role not in roles:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return current_user
    return role_checker

# Dependency: Database session with lifecycle management
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise

# Usage — clean endpoint with no auth/DB boilerplate
@app.get("/advisor/clients", response_model=List[ClientResponse])
async def get_clients(
    advisor: User = Depends(require_role("advisor", "admin")),
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 50
):
    return await advisor_service.get_clients(db, advisor.id, skip, limit)
```

**Dependency Caching:** Within a single request, FastAPI caches a dependency's result — the same `db` session is reused across all dependencies in one request.

**Why Interviewers Ask This:** Your entire OneWealth architecture revolves around DI for RBAC, session management, and service injection.

**Follow-Up Questions:**
- How does `use_cache=False` in `Depends` work?
- What is the difference between `Depends` and `Security`?
- How do you override dependencies in tests?
- What is a "sub-dependency"?

---

### [INTERMEDIATE] Q17: How does Pydantic validation work in FastAPI? Explain V1 vs V2.

**Answer:**

```python
from pydantic import BaseModel, Field, validator, field_validator, model_validator
from typing import Optional
from datetime import datetime

# Pydantic V2 style (modern)
class InvestmentRequest(BaseModel):
    amount: float = Field(gt=0, description="Investment amount in USD")
    currency: str = Field(default="USD", pattern="^[A-Z]{3}$")
    risk_level: int = Field(ge=1, le=5, description="Risk level 1-5")
    notes: Optional[str] = Field(default=None, max_length=500)

    @field_validator('amount')
    @classmethod
    def round_amount(cls, v: float) -> float:
        return round(v, 2)

    @model_validator(mode='after')
    def check_high_risk_minimum(self):
        if self.risk_level >= 4 and self.amount < 10000:
            raise ValueError("High-risk investments require minimum $10,000")
        return self

class InvestmentResponse(BaseModel):
    id: int
    amount: float
    currency: str
    created_at: datetime
    status: str

    model_config = {"from_attributes": True}  # V2 replacement for orm_mode=True

# FastAPI automatically returns 422 Unprocessable Entity for validation failures
@app.post("/investments", response_model=InvestmentResponse)
async def create_investment(request: InvestmentRequest):
    ...
```

**V1 vs V2 key differences:**

| Feature | V1 | V2 |
|---|---|---|
| ORM mode | `orm_mode = True` | `from_attributes = True` |
| Validator | `@validator` | `@field_validator` |
| Performance | Slower | ~5-50x faster (Rust core) |
| Config | `class Config` | `model_config = {}` |

**Why Interviewers Ask This:** Pydantic is core to your work at OneWealth ("schema-driven validation with Pydantic").

---

### [ADVANCED] Q18: How would you implement Rate Limiting and Caching in FastAPI?

**Answer:**

**Rate Limiting with Redis:**
```python
import redis.asyncio as redis
from fastapi import Request, HTTPException
import time

redis_client = redis.from_url("redis://localhost:6379")

async def rate_limiter(request: Request, max_requests: int = 100, window_seconds: int = 60):
    client_ip = request.client.host
    key = f"rate_limit:{client_ip}:{int(time.time() // window_seconds)}"
    
    pipe = redis_client.pipeline()
    pipe.incr(key)
    pipe.expire(key, window_seconds)
    results = await pipe.execute()
    
    request_count = results[0]
    if request_count > max_requests:
        raise HTTPException(
            status_code=429,
            detail="Too many requests",
            headers={"Retry-After": str(window_seconds)}
        )

# Apply as dependency
@app.get("/api/data", dependencies=[Depends(rate_limiter)])
async def get_data():
    ...
```

**Response Caching:**
```python
import json
import hashlib
from functools import wraps

def cache_response(ttl_seconds: int = 300):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Build cache key from function name + arguments
            cache_key = f"cache:{func.__name__}:{hashlib.md5(str(kwargs).encode()).hexdigest()}"
            
            cached = await redis_client.get(cache_key)
            if cached:
                return json.loads(cached)
            
            result = await func(*args, **kwargs)
            await redis_client.setex(cache_key, ttl_seconds, json.dumps(result))
            return result
        return wrapper
    return decorator

@app.get("/market/summary")
@cache_response(ttl_seconds=60)  # Cache market data for 60 seconds
async def get_market_summary():
    return await market_service.get_summary()
```

**Why Interviewers Ask This:** Rate limiting is critical for your fintech APIs (OneWealth) — prevent abuse, protect downstream systems.

**Follow-Up Questions:**
- What is the sliding window algorithm vs fixed window for rate limiting?
- How does Redis's `INCR` + `EXPIRE` guarantee atomicity?
- What is cache stampede and how do you prevent it?
- How does CDN-level caching differ from application-level caching?

---

### [ADVANCED] Q19: Explain Middleware in FastAPI and write a custom middleware.

**Answer:**
Middleware intercepts every request before it reaches route handlers and every response before it's sent to the client.

```python
import time
import uuid
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import logging

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id
        
        start_time = time.perf_counter()
        
        # Log incoming request
        logger.info(f"[{request_id}] {request.method} {request.url.path}")
        
        try:
            response = await call_next(request)
        except Exception as e:
            logger.error(f"[{request_id}] Unhandled exception: {e}")
            raise
        
        duration = time.perf_counter() - start_time
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Process-Time"] = f"{duration:.4f}"
        
        logger.info(
            f"[{request_id}] {request.method} {request.url.path} "
            f"-> {response.status_code} ({duration:.4f}s)"
        )
        return response

class CORSMiddleware:
    # (use fastapi.middleware.cors.CORSMiddleware in production)
    pass

# Register middleware (order matters: last added = first executed)
app.add_middleware(RequestLoggingMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://app.onewealth.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**Follow-Up Questions:**
- What is the difference between middleware and a dependency?
- How does CORS middleware work at the HTTP level?
- How would you implement request body logging without consuming the stream?
- What is the order of middleware execution?

---

### [ADVANCED] Q20: How do you implement API Versioning in FastAPI?

**Answer:**

```python
from fastapi import FastAPI, APIRouter

app = FastAPI()

# Version 1 Router
v1_router = APIRouter(prefix="/api/v1", tags=["v1"])

@v1_router.get("/users/{user_id}")
async def get_user_v1(user_id: int):
    return {"id": user_id, "name": "...", "email": "..."}  # Old format

# Version 2 Router — breaking change: email removed, phone added
v2_router = APIRouter(prefix="/api/v2", tags=["v2"])

@v2_router.get("/users/{user_id}")
async def get_user_v2(user_id: int):
    return {"id": user_id, "name": "...", "phone": "...", "profile_url": "..."}

app.include_router(v1_router)
app.include_router(v2_router)

# Alternative: Header-based versioning
from fastapi import Header

@app.get("/users/{user_id}")
async def get_user(user_id: int, api_version: str = Header(default="v1")):
    if api_version == "v2":
        return await user_service.get_user_v2(user_id)
    return await user_service.get_user_v1(user_id)
```

**When to version:** When making breaking changes — removing fields, changing data types, restructuring response format.

---

# 5. Django & Django REST Framework

### [INTERMEDIATE] Q21: How does Django differ from FastAPI? When would you choose one over the other?

**Answer:**

| Aspect | Django | FastAPI |
|---|---|---|
| Philosophy | "Batteries included" — ORM, admin, auth built-in | Lightweight, composable |
| Async | Partial (3.1+), async views supported | Native async-first (ASGI) |
| ORM | Django ORM (excellent, opinionated) | SQLAlchemy (flexible, complex) |
| Performance | Moderate | High (~3-10x faster under load) |
| Admin Panel | Built-in, powerful | None (use external tools) |
| Learning Curve | Steeper initial, but conventions guide you | Gentler with type hints |
| Best For | CMS, admin-heavy, monoliths | Microservices, high-perf APIs, ML APIs |

**When to choose Django:**
- You need Django Admin for internal tools.
- You're building a traditional web app with templates.
- Team prefers convention over configuration.
- You need Django's mature ecosystem (django-allauth, etc.).

**When to choose FastAPI:**
- High-throughput APIs (your OneWealth fintech case).
- Microservices with async I/O.
- ML/AI API serving (your AI projects).
- API-first products where auto-docs matter.

**DRF specifics:**
```python
# Django REST Framework — Serializers are DRF's equivalent of Pydantic models
from rest_framework import serializers, viewsets

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'is_active']
        read_only_fields = ['id']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
```

---

# 6. REST API Design & Best Practices

### [INTERMEDIATE] Q22: What are RESTful API design principles? Apply them to your OneWealth project.

**Answer:**

**6 REST Constraints:**
1. **Client-Server:** Separation of concerns — frontend and backend evolve independently.
2. **Stateless:** Each request contains all information needed. No server-side session.
3. **Cacheable:** Responses must define cacheability.
4. **Uniform Interface:** Consistent resource identification (URLs), manipulation via representations.
5. **Layered System:** Client doesn't know if it's talking to origin server or proxy/load balancer.
6. **Code on Demand (optional):** Server can send executable code (JavaScript).

**HTTP Methods semantics:**
```
GET    /api/v1/advisors          → List all advisors (200 OK)
POST   /api/v1/advisors          → Create advisor (201 Created)
GET    /api/v1/advisors/{id}     → Get specific advisor (200 OK or 404)
PUT    /api/v1/advisors/{id}     → Replace entire advisor (200 OK)
PATCH  /api/v1/advisors/{id}     → Partial update (200 OK)
DELETE /api/v1/advisors/{id}     → Delete (204 No Content)

# Nested resources
GET    /api/v1/firms/{firm_id}/advisors        → Advisors in a firm
POST   /api/v1/advisors/{id}/invite            → Send invitation (action)
POST   /api/v1/advisors/{id}/onboarding/start  → Start onboarding
```

**Standard response structure (your OneWealth pattern):**
```json
// Success
{
  "success": true,
  "data": { "id": 1, "email": "advisor@firm.com" },
  "message": "Advisor created successfully",
  "meta": { "timestamp": "2024-01-01T00:00:00Z" }
}

// Error
{
  "success": false,
  "error_code": "ADVISOR_NOT_FOUND",
  "message": "Advisor with ID 123 not found",
  "details": []
}
```

**Pagination:**
```json
{
  "data": [...],
  "pagination": {
    "total": 500,
    "page": 2,
    "page_size": 20,
    "total_pages": 25,
    "next": "/api/v1/advisors?page=3&page_size=20",
    "previous": "/api/v1/advisors?page=1&page_size=20"
  }
}
```

---

# 7. Authentication & Authorization

### [INTERMEDIATE] Q23: Explain JWT authentication — how it works and how you implemented it.

**Answer:**

**JWT Structure:** `Header.Payload.Signature` — base64url encoded.

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.  ← Header
eyJzdWIiOiIxMjMiLCJlbWFpbCI6ImFkdmlzb3JAZmlybS5jb20iLCJyb2xlIjoiYWR2aXNvciIsImV4cCI6MTcwMDAwMDAwMH0.  ← Payload
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c  ← Signature
```

```python
from datetime import datetime, timedelta, timezone
import jwt
from passlib.context import CryptContext
from pydantic import BaseModel

SECRET_KEY = "your-256-bit-secret"  # Use env vars in production!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class TokenPair(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

def create_access_token(user_id: int, role: str, firm_id: int) -> str:
    payload = {
        "sub": str(user_id),
        "role": role,
        "firm_id": firm_id,
        "type": "access",
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(user_id: int) -> str:
    payload = {
        "sub": str(user_id),
        "type": "refresh",
        "exp": datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

async def login(email: str, password: str, db: AsyncSession) -> TokenPair:
    user = await user_repo.get_by_email(db, email)
    if not user or not pwd_context.verify(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return TokenPair(
        access_token=create_access_token(user.id, user.role, user.firm_id),
        refresh_token=create_refresh_token(user.id)
    )
```

**Why Interviewers Ask This:** Your OneWealth project has JWT auth + RBAC + invitation lifecycle — all JWT-dependent.

**Common Mistakes:** Storing JWT in localStorage (XSS risk), not validating `exp`, using weak secrets, not using HTTPS.

**Follow-Up Questions:**
- How do you revoke a JWT before expiry?
- What is the difference between access tokens and refresh tokens?
- JWT vs Session-based auth — tradeoffs?
- How does RS256 differ from HS256?
- What is a JWT blacklist and how do you implement it with Redis?

---

### [ADVANCED] Q24: Explain RBAC (Role-Based Access Control) — your OneWealth implementation.

**Answer:**
RBAC restricts system access to authorized users based on their role. In OneWealth's advisor hierarchy:

```
Firm Admin
    └── Senior Advisor
           └── Junior Advisor
                  └── Client
```

```python
from enum import Enum
from typing import Set

class Role(str, Enum):
    ADMIN = "admin"
    SENIOR_ADVISOR = "senior_advisor"
    JUNIOR_ADVISOR = "junior_advisor"
    CLIENT = "client"

# Permission definitions
ROLE_PERMISSIONS: dict[Role, Set[str]] = {
    Role.ADMIN: {
        "users:read", "users:write", "users:delete",
        "advisors:read", "advisors:write", "advisors:delete",
        "firms:read", "firms:write", "investments:all"
    },
    Role.SENIOR_ADVISOR: {
        "users:read", "advisors:read",
        "clients:read", "clients:write",
        "investments:read", "investments:write"
    },
    Role.JUNIOR_ADVISOR: {
        "clients:read", "investments:read", "investments:write:own"
    },
    Role.CLIENT: {
        "portfolio:read:own", "documents:read:own"
    }
}

def require_permission(permission: str):
    async def checker(current_user: User = Depends(get_current_user)):
        user_permissions = ROLE_PERMISSIONS.get(Role(current_user.role), set())
        if permission not in user_permissions:
            raise HTTPException(
                status_code=403,
                detail=f"Permission '{permission}' required"
            )
        return current_user
    return checker

# Hierarchy-aware: senior advisor can only access their firm's clients
async def get_accessible_client(
    client_id: int,
    advisor: User = Depends(require_permission("clients:read")),
    db: AsyncSession = Depends(get_db)
) -> Client:
    client = await client_repo.get(db, client_id)
    if not client:
        raise HTTPException(404, "Client not found")
    # Firm-level isolation
    if advisor.firm_id != client.firm_id:
        raise HTTPException(403, "Access denied: different firm")
    return client
```

---

# 8. Databases — PostgreSQL & SQL

### [INTERMEDIATE] Q25: Explain ACID properties with examples from your fintech projects.

**Answer:**
ACID ensures database transaction reliability — critical in financial systems.

**A — Atomicity:** All operations in a transaction succeed or all fail (no partial state).
```sql
-- Transfer $1000 between accounts — must be atomic
BEGIN;
    UPDATE accounts SET balance = balance - 1000 WHERE id = 1;  -- Debit
    UPDATE accounts SET balance = balance + 1000 WHERE id = 2;  -- Credit
COMMIT;
-- If second UPDATE fails, ROLLBACK ensures money isn't lost
```

**C — Consistency:** Transaction brings DB from one valid state to another (enforcing constraints).
```sql
-- Constraint ensures consistency
ALTER TABLE accounts ADD CONSTRAINT positive_balance CHECK (balance >= 0);
-- Any transaction that would make balance negative is rejected
```

**I — Isolation:** Concurrent transactions don't see each other's uncommitted changes.

PostgreSQL isolation levels:
- `READ COMMITTED` (default): Reads only committed data. Phantom reads possible.
- `REPEATABLE READ`: Same rows returned throughout transaction. No non-repeatable reads.
- `SERIALIZABLE`: Transactions appear to execute serially. Strongest guarantee.

```python
# SQLAlchemy async transaction
async with session.begin():
    portfolio = await session.get(Portfolio, portfolio_id, with_for_update=True)  # Lock row
    portfolio.value += trade_amount
    # No other transaction can modify this row until commit
```

**D — Durability:** Committed transactions survive system failures (persisted to disk via WAL).

**Why Interviewers Ask This:** OneWealth is a fintech platform — transactions are literally financial. ACID knowledge is non-negotiable.

**Follow-Up Questions:**
- What is a deadlock and how do you prevent it?
- Explain WAL (Write-Ahead Logging).
- What is the difference between `FOR UPDATE` and `FOR SHARE`?
- What are PostgreSQL's MVCC guarantees?

---

### [INTERMEDIATE] Q26: Explain database indexing — types, when to use, and tradeoffs.

**Answer:**

**B-Tree Index (default):** Ordered tree. Best for equality and range queries.
```sql
-- Without index: O(n) sequential scan
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'advisor@firm.com';
-- Seq Scan on users (cost=0.00..10000.00 rows=500000)

-- With index: O(log n) B-tree traversal
CREATE INDEX idx_users_email ON users(email);
-- Index Scan (cost=0.29..8.31 rows=1)
```

**Composite Index:**
```sql
-- Covers queries filtering by firm_id AND role together
CREATE INDEX idx_users_firm_role ON users(firm_id, role);
-- Useful: WHERE firm_id = 1 AND role = 'advisor' ✓
-- Not useful: WHERE role = 'advisor' alone (leading column must match) ✗
```

**Partial Index:**
```sql
-- Only index active users — smaller, faster
CREATE INDEX idx_active_users ON users(email) WHERE is_active = TRUE;
```

**GIN Index for JSONB:**
```sql
-- For document/JSONB columns
CREATE INDEX idx_user_metadata ON users USING GIN(metadata);
SELECT * FROM users WHERE metadata @> '{"investment_type": "equity"}';
```

**Indexing tradeoffs:**
- Speeds up `SELECT` queries.
- Slows down `INSERT`, `UPDATE`, `DELETE` (index must be updated).
- Consumes disk space.
- Wrong indexes can hurt more than help (query planner confusion).

**When NOT to index:**
- Small tables (< 1000 rows) — sequential scan is faster.
- Columns with low cardinality (e.g., `is_active` with only true/false).
- Columns rarely used in WHERE, JOIN, or ORDER BY.

**Follow-Up Questions:**
- What is an index scan vs bitmap index scan vs sequential scan?
- How does `EXPLAIN ANALYZE` help optimize queries?
- What is index bloat and how do you fix it (`REINDEX`/`VACUUM`)?

---

### [ADVANCED] Q27: Write complex SQL queries for common backend scenarios.

**Answer:**

```sql
-- 1. Window functions — Rank advisors by AUM within their firm
SELECT
    advisor_id,
    firm_id,
    total_aum,
    RANK() OVER (PARTITION BY firm_id ORDER BY total_aum DESC) as rank_in_firm,
    PERCENT_RANK() OVER (PARTITION BY firm_id ORDER BY total_aum DESC) as percentile
FROM advisor_metrics;

-- 2. CTE — Advisor hierarchy (recursive)
WITH RECURSIVE advisor_tree AS (
    -- Base: root advisors (no parent)
    SELECT id, name, parent_advisor_id, 1 AS level
    FROM advisors WHERE parent_advisor_id IS NULL
    
    UNION ALL
    
    -- Recursive: children
    SELECT a.id, a.name, a.parent_advisor_id, at.level + 1
    FROM advisors a
    INNER JOIN advisor_tree at ON a.parent_advisor_id = at.id
)
SELECT * FROM advisor_tree ORDER BY level, name;

-- 3. Aggregation with HAVING
SELECT
    firm_id,
    COUNT(*) as total_clients,
    AVG(portfolio_value) as avg_portfolio,
    SUM(portfolio_value) as total_aum
FROM client_portfolios
WHERE created_at >= CURRENT_DATE - INTERVAL '90 days'
GROUP BY firm_id
HAVING SUM(portfolio_value) > 1000000
ORDER BY total_aum DESC;

-- 4. Upsert (INSERT ON CONFLICT)
INSERT INTO user_sessions (user_id, token_hash, expires_at, last_active)
VALUES ($1, $2, $3, NOW())
ON CONFLICT (user_id)
DO UPDATE SET
    token_hash = EXCLUDED.token_hash,
    expires_at = EXCLUDED.expires_at,
    last_active = NOW();
```

**Follow-Up Questions:**
- What is the N+1 query problem and how do you solve it with SQLAlchemy?
- How does `SELECT FOR UPDATE` work and when is it needed?
- What is connection pooling and why does it matter?

---

### [ADVANCED] Q28: Database normalization — explain all normal forms with examples.

**Answer:**

**1NF (First Normal Form):** No repeating groups; atomic values.
```sql
-- VIOLATES 1NF: multiple values in one column
CREATE TABLE bad_users (
    id INT,
    email TEXT,
    phone_numbers TEXT  -- "123456, 789012" — not atomic!
);

-- SATISFIES 1NF
CREATE TABLE users (id INT, email TEXT, PRIMARY KEY(id));
CREATE TABLE user_phones (user_id INT, phone_number TEXT, FOREIGN KEY(user_id) REFERENCES users(id));
```

**2NF:** 1NF + no partial dependencies (all non-key columns depend on the WHOLE primary key).
```sql
-- VIOLATES 2NF (composite key: order_id + product_id)
CREATE TABLE bad_order_items (
    order_id INT,
    product_id INT,
    product_name TEXT,  -- Depends only on product_id, not full composite key!
    quantity INT,
    PRIMARY KEY(order_id, product_id)
);

-- SATISFIES 2NF
CREATE TABLE products (id INT PRIMARY KEY, name TEXT);
CREATE TABLE order_items (order_id INT, product_id INT, quantity INT, PRIMARY KEY(order_id, product_id));
```

**3NF:** 2NF + no transitive dependencies.
```sql
-- VIOLATES 3NF
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    dept_id INT,
    dept_name TEXT,  -- Transitively depends on emp_id via dept_id
    salary DECIMAL
);

-- SATISFIES 3NF
CREATE TABLE departments (id INT PRIMARY KEY, name TEXT);
CREATE TABLE employees (id INT PRIMARY KEY, dept_id INT REFERENCES departments(id), salary DECIMAL);
```

**When to DENORMALIZE:** Read-heavy analytics, data warehouses (OLAP), performance-critical aggregations.

---

# 9. System Design

### [INTERMEDIATE] Q29: Design a scalable URL shortener (classic system design).

**Answer:**

**Requirements clarification first:**
- Write: 100 URLs/second
- Read: 10,000 redirects/second (100:1 read:write ratio)
- URL length: ~7 characters
- Data retention: 5 years

**High-level design:**
```
Client → Load Balancer → API Servers (horizontal) → Cache (Redis) → DB (PostgreSQL)
                                                  ↑
                                              CDN for redirect
```

**Data model:**
```sql
CREATE TABLE shortened_urls (
    id BIGSERIAL PRIMARY KEY,
    short_code VARCHAR(10) UNIQUE NOT NULL,
    original_url TEXT NOT NULL,
    user_id INT REFERENCES users(id),
    created_at TIMESTAMP DEFAULT NOW(),
    expires_at TIMESTAMP,
    click_count BIGINT DEFAULT 0
);
CREATE INDEX idx_short_code ON shortened_urls(short_code);
```

**Encoding strategy:** Base62 encoding of auto-incremented ID.
```python
import string
BASE62 = string.ascii_letters + string.digits  # 62 chars

def encode(num: int) -> str:
    result = []
    while num:
        result.append(BASE62[num % 62])
        num //= 62
    return ''.join(reversed(result)).zfill(7)  # Pad to 7 chars

def decode(s: str) -> int:
    return sum(BASE62.index(c) * (62 ** i) for i, c in enumerate(reversed(s)))
```

**Caching strategy:** Cache hot URLs in Redis with LRU eviction.
```python
async def redirect(short_code: str) -> str:
    # Check cache first
    cached_url = await redis.get(f"url:{short_code}")
    if cached_url:
        return cached_url.decode()
    
    # Cache miss: DB lookup
    url = await db.query(short_code)
    if url:
        await redis.setex(f"url:{short_code}", 3600, url.original_url)
        return url.original_url
    
    raise HTTPException(404, "URL not found")
```

**Scalability considerations:**
- Horizontal scaling of API servers behind load balancer.
- Read replicas for DB read scaling.
- CDN for redirect caching.
- Consistent hashing for Redis cluster.

---

### [ADVANCED] Q30: Monolith vs Microservices — when to choose which?

**Answer:**

**Monolith:**
- Single deployable unit.
- Simple development, testing, debugging.
- Lower operational overhead.
- Best for: startups, small teams, early product development.

**Microservices:**
- Each service owns one business domain.
- Independent deployment, scaling, tech stack.
- Operational complexity: service discovery, distributed tracing, eventual consistency.
- Best for: large teams, independent scaling requirements, diverse tech stacks needed.

**Your project context — the LLM-Powered SQL Generator:**
The SQL Generator can start as a modular service and split only when scale or ownership requires it:

```
INITIAL MODULAR SERVICE:
┌─────────────────────────────────────────────┐
│ API │ retrieval │ generation │ validation │ caching │
└─────────────────────────────────────────────┘

OPTIONAL EXTRACTION:
┌──────────────┐  ┌────────────────┐  ┌──────────────┐
│ FastAPI API  │  │ Retrieval svc  │  │ Worker queue │
│ auth + limits│  │ pgvector      │  │ Celery/Redis │
└──────────────┘  └────────────────┘  └──────────────┘
```

**Martin Fowler's advice:** "Don't start with microservices — start with a modular monolith."

**Follow-Up Questions:**
- How do microservices communicate (sync REST vs async messaging)?
- What is the Saga pattern for distributed transactions?
- How do you handle authentication across microservices?
- What is service mesh (Istio)?

---

### [ADVANCED] Q31: Explain CAP Theorem.

**Answer:**
In a distributed system, you can only guarantee 2 of 3 properties simultaneously:

- **C — Consistency:** Every read returns the most recent write (or an error).
- **A — Availability:** Every request receives a response (not necessarily the most recent).
- **P — Partition Tolerance:** System continues operating despite network partitions.

**Since network partitions are unavoidable in distributed systems, you must choose CP or AP:**

**CP (Consistency + Partition Tolerance):** Accept unavailability during partitions.
- Examples: PostgreSQL, HBase, ZooKeeper.
- Your fintech use case (OneWealth): **CP is required** — you cannot show stale portfolio balances.

**AP (Availability + Partition Tolerance):** Accept stale data during partitions.
- Examples: Cassandra, DynamoDB (eventually consistent mode), CouchDB.
- Use case: Social media feeds, product catalogs, DNS.

```python
# CP system behavior during partition
# PostgreSQL: If primary can't reach replica, refuses writes to replica
# → Users get 503 but never stale financial data ✓

# AP system behavior during partition
# Cassandra: All nodes accept reads/writes but may return stale data
# → Users get responses but might see old account balances ✗ (for fintech)
```

---

# 10. Docker & DevOps

### [BEGINNER] Q32: What is Docker and why did you use it in your projects?

**Answer:**
Docker is a containerization platform that packages an application with its dependencies into a portable, isolated container.

**Key concepts:**
- **Image:** Blueprint (read-only). Built from `Dockerfile`.
- **Container:** Running instance of an image.
- **Registry:** Docker Hub, ECR, GCR — stores images.
- **Compose:** Multi-container orchestration for development.

```dockerfile
# Production Dockerfile for FastAPI app
FROM python:3.11-slim AS base

# Security: run as non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# Layer caching: install dependencies before copying app code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY --chown=appuser:appuser . .

USER appuser

EXPOSE 8000

# Use gunicorn with uvicorn workers for production
CMD ["gunicorn", "app.main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]
```

```yaml
# docker-compose.yml — local development (like your AI Voice Teller)
version: '3.8'
services:
  api:
    build: .
    ports: ["8000:8000"]
    environment:
      - DATABASE_URL=postgresql+asyncpg://user:pass@db:5432/app
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
    volumes:
      - .:/app  # Hot reload in dev

  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: pass
      POSTGRES_USER: user
      POSTGRES_DB: app
    volumes:
      - pgdata:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine

  celery_worker:
    build: .
    command: celery -A app.worker worker --loglevel=info -Q exam_pipeline
    depends_on:
      - redis
      - db

volumes:
  pgdata:
```

**Why Interviewers Ask This:** You use Docker in AI Voice Teller and the surrounding AI services, alongside Redis and Celery.

**Follow-Up Questions:**
- What is the difference between CMD and ENTRYPOINT?
- How do multi-stage builds reduce image size?
- How do you handle secrets in Docker? (Never use ENV for secrets!)
- What is the difference between `COPY` and `ADD`?
- How does container networking work? (bridge, host, overlay networks)

---

### [INTERMEDIATE] Q33: Explain CI/CD pipelines — how would you set one up for a FastAPI project?

**Answer:**

```yaml
# .github/workflows/ci-cd.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: testpass
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
      redis:
        image: redis:7

    steps:
      - uses: actions/checkout@v3
      - name: Set up Python 3.11
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install -r requirements.txt -r requirements-dev.txt
      
      - name: Lint with ruff
        run: ruff check .
      
      - name: Type check with mypy
        run: mypy app/
      
      - name: Run tests with coverage
        run: pytest --cov=app --cov-report=xml -v
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3

  build-and-deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - name: Build Docker image
        run: docker build -t myapp:${{ github.sha }} .
      
      - name: Push to ECR
        run: |
          aws ecr get-login-password | docker login --username AWS --password-stdin $ECR_URI
          docker push $ECR_URI/myapp:${{ github.sha }}
      
      - name: Deploy to EC2
        run: |
          ssh deploy@$EC2_HOST "docker pull $ECR_URI/myapp:${{ github.sha }} && \
          docker-compose up -d --no-deps api"
```

**Follow-Up Questions:**
- What is the difference between continuous delivery and continuous deployment?
- How do you do zero-downtime deployments?
- What is blue-green deployment vs canary deployment?

---

# 11. Cloud & Azure/AWS

### [INTERMEDIATE] Q34: Explain cloud services relevant to your projects (Azure and AWS equivalents).

**Answer:**

**Object storage (Azure Blob Storage; AWS S3 is the equivalent):**
- Store files such as user documents, generated audio, and exam PDFs.
- Keep objects private and expose them through short-lived signed URLs when needed.

```python
import boto3
from botocore.exceptions import ClientError

class ObjectStorageService:
    def __init__(self):
        self.client = boto3.client('s3', region_name='ap-south-1')
        self.bucket = "onewealth-documents"

    async def upload_document(self, file_content: bytes, user_id: int, doc_type: str) -> str:
        key = f"users/{user_id}/documents/{doc_type}/{uuid.uuid4()}.pdf"
        
        self.client.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=file_content,
            ContentType="application/pdf",
            ServerSideEncryption="AES256",  # Encrypt at rest
            Metadata={"user_id": str(user_id), "doc_type": doc_type}
        )
        return key

    def generate_presigned_url(self, key: str, expiry_seconds: int = 3600) -> str:
        return self.client.generate_presigned_url(
            'get_object',
            Params={'Bucket': self.bucket, 'Key': key},
            ExpiresIn=expiry_seconds
        )
```

**Compute (Azure Virtual Machines; AWS EC2 is the equivalent):**
- Virtual servers for hosting backend workloads and supporting services.
- Choose capacity based on CPU, memory, network, and scaling requirements.

**Security best practices:**
- Never hardcode cloud credentials; use managed identities, environment variables, or a secret manager.
- Object storage should be private by default; use signed URLs for client access.
- Security groups: whitelist only required ports.
- Encrypt data in transit (HTTPS) and at rest (KMS/AES-256).

**Follow-Up Questions:**
- How do managed identities compare with AWS IAM roles?
- How does Azure Blob lifecycle management work, and what is the S3 equivalent?
- How would you put a CDN in front of object storage?
- When would you use a serverless function instead of a VM?

---

# 12. AI / ML / GenAI / LLM Round

## 12.1 Machine Learning Fundamentals

### [BEGINNER] Q35: Explain the difference between supervised, unsupervised, and reinforcement learning.

**Answer:**

**Supervised Learning:** Train on labeled data (input → known output).
- Examples: Classification (spam/not spam), Regression (house prices), NLP (sentiment analysis).
- Your project connection: The statistical scoring engine in Exam Oracle is supervised-like (historical exam data as training signal).

**Unsupervised Learning:** Train on unlabeled data; find patterns.
- Examples: Clustering (K-Means, DBSCAN), Dimensionality reduction (PCA, t-SNE).
- Your project connection: **Exam Oracle uses DBSCAN** for semantic clustering of topics.

**Reinforcement Learning:** Agent learns by interacting with environment; maximizes reward.
- Examples: Game playing (AlphaGo), robotics, recommendation systems.

```python
# DBSCAN usage from your Exam Oracle project
from sklearn.cluster import DBSCAN
import numpy as np

def cluster_topics_semantically(embeddings: np.ndarray, epsilon: float = 0.3, min_samples: int = 2):
    """
    Cluster semantically similar topics using DBSCAN.
    epsilon: max distance between two samples to be in same neighborhood.
    DBSCAN doesn't require specifying number of clusters (unlike K-Means).
    """
    clusterer = DBSCAN(eps=epsilon, min_samples=min_samples, metric='cosine')
    labels = clusterer.fit_predict(embeddings)  # -1 = noise/outlier
    
    # Topics with label == -1 are outliers (unique, niche topics)
    unique_topics_mask = labels == -1
    clustered_topics = labels[~unique_topics_mask]
    
    return labels, unique_topics_mask
```

---

## 12.2 LLM Fundamentals

### [INTERMEDIATE] Q36: How do Large Language Models work at a high level?

**Answer:**
LLMs are neural networks (Transformer architecture) trained on massive text corpora via **self-supervised learning** (predict next token).

**Key concepts:**

**Tokenization:** Text → tokens (sub-words).
```python
# "FastAPI is amazing" → ["Fast", "API", " is", " amazing"]
# Each token maps to an integer ID in the vocabulary
```

**Embeddings:** Tokens → dense vector representations (meaning in high-dimensional space).

**Attention Mechanism:** The core of transformers. Allows each token to "attend" to all other tokens and learn contextual relationships.

**Self-attention formula:**
```
Attention(Q, K, V) = softmax(QK^T / √d_k) · V
Where: Q = Query, K = Key, V = Value matrices
```

**Transformer architecture:**
```
Input Tokens
     ↓
Token Embeddings + Positional Encodings
     ↓
[Self-Attention → Add & Norm → Feed Forward → Add & Norm] × N layers
     ↓
Linear + Softmax
     ↓
Next Token Probabilities
```

**Temperature:** Controls randomness. 0 = deterministic (always top token), 1 = balanced, 2 = very random.

**Context window:** Maximum tokens the model can process at once. GPT-4: 128K, Claude: 200K.

---

### [INTERMEDIATE] Q37: What is RAG (Retrieval-Augmented Generation) and how did you implement it in Exam Oracle?

**Answer:**

**RAG solves two LLM problems:**
1. **Hallucination:** LLMs generate plausible-sounding but false information.
2. **Knowledge cutoff:** LLMs don't know recent information.

**RAG Pipeline:**
```
User Query
    ↓
[Retrieval] Query → Embedding → Vector DB similarity search → Relevant chunks
    ↓
[Augmentation] Prompt = "Context: {retrieved chunks}\n\nQuestion: {user query}"
    ↓
[Generation] LLM generates answer grounded in retrieved context
```

**Your Exam Oracle implementation:**
```python
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 1. INDEXING PHASE (offline)
class ExamPaperIndexer:
    def __init__(self):
        self.embedder = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.vectorstore = Chroma(
            collection_name="exam_papers",
            embedding_function=self.embedder,
            persist_directory="./chroma_db"
        )
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=512,
            chunk_overlap=50,  # Overlap preserves context at boundaries
            separators=["\n\n", "\n", ".", " "]
        )

    def index_exam_paper(self, paper_text: str, metadata: dict):
        chunks = self.text_splitter.split_text(paper_text)
        
        docs_with_metadata = [
            {"content": chunk, "metadata": {**metadata, "chunk_id": i}}
            for i, chunk in enumerate(chunks)
        ]
        self.vectorstore.add_texts(
            texts=[d["content"] for d in docs_with_metadata],
            metadatas=[d["metadata"] for d in docs_with_metadata]
        )

# 2. RETRIEVAL + GENERATION PHASE (online)
class ExamQuestionGenerator:
    def __init__(self, vectorstore: Chroma, llm):
        self.vectorstore = vectorstore
        self.llm = llm

    async def generate_questions(self, topic: str, exam_type: str, count: int = 5):
        # Retrieve relevant historical questions
        relevant_chunks = self.vectorstore.similarity_search(
            query=f"{exam_type} questions about {topic}",
            k=10,
            filter={"exam_type": exam_type}
        )

        # Build RAG prompt
        context = "\n\n".join([chunk.page_content for chunk in relevant_chunks])
        prompt = f"""
        Based on these historical {exam_type} exam questions:
        {context}
        
        Generate {count} NEW practice questions on the topic: {topic}
        Focus on the patterns and difficulty level seen in the historical data.
        Format each question with: Question, 4 Options, Correct Answer, Explanation.
        """
        
        response = await self.llm.agenerate([prompt])
        return self.parse_questions(response.generations[0][0].text)
```

**Why Interviewers Ask This:** RAG is THE most important GenAI architecture pattern for 2024-2026. You've implemented it — be ready to explain every component.

**Follow-Up Questions:**
- What is the difference between sparse (BM25) and dense (embedding) retrieval?
- What is hybrid search?
- How do you evaluate RAG quality? (Context precision, context recall, faithfulness)
- What is the optimal chunk size and overlap? How do you tune it?
- What is HyDE (Hypothetical Document Embeddings)?

---

### [ADVANCED] Q38: Explain your multi-LLM cascade architecture in Exam Oracle.

**Answer:**
Your cascade: `Groq Llama-3-70B → Gemini Flash → Ollama Mistral-7B`

```python
from abc import ABC, abstractmethod
import asyncio
import logging

logger = logging.getLogger(__name__)

class BaseLLM(ABC):
    @abstractmethod
    async def generate(self, prompt: str, **kwargs) -> str: pass

    @property
    @abstractmethod
    def name(self) -> str: pass

class GroqLLM(BaseLLM):
    name = "groq-llama-3-70b"
    async def generate(self, prompt: str, **kwargs) -> str:
        # Groq API call — fastest inference
        ...

class GeminiFlashLLM(BaseLLM):
    name = "gemini-flash"
    async def generate(self, prompt: str, **kwargs) -> str:
        # Google AI API call
        ...

class OllamaLocalLLM(BaseLLM):
    name = "ollama-mistral-7b"
    async def generate(self, prompt: str, **kwargs) -> str:
        # Local inference — no cost, no internet required
        import httpx
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:11434/api/generate",
                json={"model": "mistral", "prompt": prompt, "stream": False},
                timeout=120.0
            )
        return response.json()["response"]

class LLMCascade:
    """Multi-LLM cascade with automatic fallback — zero single point of failure."""

    def __init__(self, llms: list[BaseLLM], max_retries: int = 1):
        self.llms = llms
        self.max_retries = max_retries

    async def generate(self, prompt: str, **kwargs) -> str:
        last_error = None

        for llm in self.llms:
            for attempt in range(self.max_retries + 1):
                try:
                    logger.info(f"Trying LLM: {llm.name} (attempt {attempt+1})")
                    result = await asyncio.wait_for(
                        llm.generate(prompt, **kwargs),
                        timeout=30.0  # Per-LLM timeout
                    )
                    logger.info(f"Success with {llm.name}")
                    return result

                except asyncio.TimeoutError:
                    logger.warning(f"{llm.name} timed out")
                    last_error = "Timeout"
                    break  # Don't retry on timeout — try next LLM

                except Exception as e:
                    logger.warning(f"{llm.name} failed: {e}")
                    last_error = str(e)
                    if attempt < self.max_retries:
                        await asyncio.sleep(2 ** attempt)  # Exponential backoff

        raise RuntimeError(f"All LLMs failed. Last error: {last_error}")

# Instantiation
cascade = LLMCascade([
    GroqLLM(),        # Free tier, fastest
    GeminiFlashLLM(), # Free tier backup
    OllamaLocalLLM()  # Zero cost, fully local fallback
])
```

**Why Interviewers Ask This:** This is sophisticated production AI architecture — it shows you think about reliability, not just functionality.

**Follow-Up Questions:**
- How do you handle rate limits across different LLM providers?
- What is token counting and why does it matter for cost management?
- How would you add monitoring/observability to this cascade (latency per provider, failure rates)?
- When would you prefer local LLMs (Ollama) over API-based LLMs?

---

### [ADVANCED] Q39: Explain Vector Databases — what they are and why you used ChromaDB.

**Answer:**
Vector databases store high-dimensional numerical vectors (embeddings) and support **similarity search** — find vectors closest to a query vector using distance metrics.

**Why regular databases can't do this:**
- SQL `WHERE embedding = [0.1, 0.2, ...]` — exact match, useless for semantic search.
- Need to find the K most similar vectors out of millions — requires ANN (Approximate Nearest Neighbor) algorithms.

**ANN algorithms:**
- **HNSW (Hierarchical Navigable Small World):** Graph-based. Fast, high recall. Used by Chroma, Pinecone, Weaviate.
- **IVF (Inverted File Index):** Clusters vectors, searches only relevant clusters. Used by FAISS.
- **LSH (Locality Sensitive Hashing):** Hash-based approximation.

**ChromaDB for Exam Oracle:**
```python
import chromadb
from chromadb.config import Settings

# Initialize ChromaDB
client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_data",
    anonymized_telemetry=False
))

collection = client.create_collection(
    name="exam_questions",
    metadata={"hnsw:space": "cosine"}  # Use cosine similarity (not euclidean)
)

# Add documents with embeddings
collection.add(
    documents=["What is Newton's second law?", "Explain photosynthesis", ...],
    embeddings=[[0.1, 0.2, ...], [0.3, 0.4, ...], ...],  # From all-MiniLM-L6-v2
    metadatas=[{"exam": "JEE", "year": 2023, "topic": "Physics"}, ...],
    ids=["q1", "q2", ...]
)

# Semantic search
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=10,
    where={"exam": "JEE"},  # Metadata filter
    include=["documents", "distances", "metadatas"]
)

# distances[0] contains cosine distances — lower = more similar
```

**ChromaDB vs Pinecone vs Weaviate vs FAISS:**

| DB | Type | Best For |
|---|---|---|
| ChromaDB | Open source, local | Development, prototyping |
| FAISS | Library (no server) | Research, offline batch |
| Pinecone | Managed cloud | Production, no ops overhead |
| Weaviate | Open source, self-hosted | Production, hybrid search |
| pgvector | PostgreSQL extension | Already using PostgreSQL |

**Why Interviewers Ask This:** Vector DBs are the cornerstone of RAG — every GenAI interview will ask this.

**Follow-Up Questions:**
- What is cosine similarity vs Euclidean distance for embeddings?
- How do you handle metadata filtering in vector search?
- What is the difference between semantic search and keyword search?
- How do you update/delete vectors in a production vector DB?
- What is pgvector and when would you use it instead of a dedicated vector DB?

---

### [ADVANCED] Q40: Explain your 7-agent autonomous AI pipeline architecture.

**Answer:**

Your pipeline: `Crawler → Parser → Embedder → Analyzer → Predictor → Validator → Assembler`

```python
from celery import Celery, chain, chord
from abc import ABC, abstractmethod
import redis

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name
        self.redis = redis.from_url("redis://localhost:6379")

    @abstractmethod
    def execute(self, input_data: dict) -> dict:
        """Each agent processes input and produces output for next agent."""
        pass

    def checkpoint(self, task_id: str, status: str, data: dict):
        """Fault tolerance: save state to Redis."""
        self.redis.setex(
            f"agent:{self.name}:{task_id}",
            3600,  # 1 hour TTL
            json.dumps({"status": status, "data": data})
        )

    def resume(self, task_id: str) -> Optional[dict]:
        """Resume from checkpoint if agent previously failed."""
        cached = self.redis.get(f"agent:{self.name}:{task_id}")
        return json.loads(cached) if cached else None

class CrawlerAgent(BaseAgent):
    """Downloads and extracts raw exam paper content."""
    def execute(self, input_data: dict) -> dict:
        exam_type = input_data["exam_type"]
        years = input_data.get("years", range(2018, 2024))
        
        papers = []
        for year in years:
            pdf_url = self.find_paper_url(exam_type, year)
            raw_text = self.download_and_extract(pdf_url)
            papers.append({"year": year, "text": raw_text})
        
        return {"exam_type": exam_type, "papers": papers}

class EmbedderAgent(BaseAgent):
    """Converts text chunks to vector embeddings."""
    def __init__(self):
        super().__init__("Embedder")
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def execute(self, input_data: dict) -> dict:
        chunks = input_data["parsed_chunks"]
        embeddings = self.model.encode(
            [chunk["text"] for chunk in chunks],
            batch_size=64,
            show_progress_bar=False,
            normalize_embeddings=True  # Unit vectors for cosine similarity
        ).tolist()
        
        for chunk, emb in zip(chunks, embeddings):
            chunk["embedding"] = emb
        
        return {"embedded_chunks": chunks}

class PredictorAgent(BaseAgent):
    """Combines frequency + ARIMA + DBSCAN to rank topic predictions."""
    def execute(self, input_data: dict) -> dict:
        topics = input_data["analyzed_topics"]
        
        # Exponential decay frequency analysis
        freq_scores = self.compute_frequency_scores(topics)
        
        # ARIMA(1,1,1) time-series trend detection
        trend_scores = self.compute_arima_trends(topics)
        
        # DBSCAN semantic clustering
        cluster_scores = self.compute_cluster_scores(topics)
        
        # Weighted combination with recency boost (up to 4x for latest papers)
        final_scores = {
            topic: (
                freq_scores.get(topic, 0) * 0.4 +
                trend_scores.get(topic, 0) * 0.4 +
                cluster_scores.get(topic, 0) * 0.2
            ) * self.recency_multiplier(topic)
            for topic in topics
        }
        
        return {"predictions": sorted(final_scores.items(), key=lambda x: -x[1])}

# Orchestration with Celery chain
@celery_app.task(bind=True, max_retries=3)
def run_exam_pipeline(self, exam_type: str, user_id: int):
    try:
        pipeline = chain(
            crawl_task.s(exam_type),
            parse_task.s(),
            embed_task.s(),
            analyze_task.s(),
            predict_task.s(),
            validate_task.s(),
            assemble_task.s(user_id)
        )
        return pipeline.apply_async()
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)
```

**Why Interviewers Ask This:** Agentic AI is the hottest topic in 2024-2026. Your 7-agent pipeline demonstrates real production AI engineering skills.

**Follow-Up Questions:**
- How do you handle a failure in agent 4 of a 7-agent pipeline?
- What is the difference between sequential agents (chain) and parallel agents (chord)?
- How do you test individual agents in isolation?
- What monitoring would you add to track pipeline performance?
- How does your pipeline compare to LangGraph's agent framework?

---

# 13. LangChain, RAG & Vector Databases

### [INTERMEDIATE] Q41: What is LangChain and how did you use it in Exam Oracle?

**Answer:**
LangChain is a framework for building LLM-powered applications. Key abstractions:
- **LLMs/Chat Models:** Unified interface to multiple providers.
- **Prompts:** Template management.
- **Chains:** Sequence of calls (LLM + prompts + tools).
- **Memory:** Conversation history management.
- **Retrievers:** Interface to vector stores.
- **Agents:** LLMs that decide which tools to call.

```python
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

# LLM
llm = ChatGroq(model_name="llama3-70b-8192", temperature=0.7)

# Embedder
embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Vector store
vectorstore = Chroma(
    collection_name="exam_papers",
    embedding_function=embedder,
    persist_directory="./chroma_db"
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 10})

# Custom prompt template
prompt_template = PromptTemplate(
    input_variables=["context", "question", "exam_type", "year"],
    template="""
You are an expert {exam_type} exam question predictor with 20 years of experience analyzing question patterns.

Historical exam data context:
{context}

Based on the patterns above, predict and generate practice questions for {exam_type} {year}:
Topic: {question}

Generate 5 high-probability questions with detailed solutions.
Format: Question | Options | Answer | Explanation
"""
)

# RAG Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt_template},
    return_source_documents=True
)

# Usage
result = qa_chain.invoke({
    "query": "Newton's Laws of Motion",
    "exam_type": "JEE",
    "year": "2024"
})
print(result["result"])        # Generated questions
print(result["source_documents"])  # Retrieved exam papers used
```

**Follow-Up Questions:**
- What is LangChain Expression Language (LCEL)?
- How does LangSmith help with LangChain debugging?
- What is the difference between a Chain and an Agent in LangChain?
- How do you add memory to a LangChain conversation?
- What is LlamaIndex and how does it differ from LangChain?

---

### [ADVANCED] Q42: Explain Prompt Engineering techniques you've used.

**Answer:**

**1. Zero-shot prompting:** No examples, direct instruction.
```
"Generate 5 JEE Physics questions on Newton's Laws."
```

**2. Few-shot prompting:** Provide examples to guide format and quality.
```
"Here are 2 example JEE Physics questions:
Q1: [example]
Q2: [example]
Now generate 5 more questions on Thermodynamics following the same format."
```

**3. Chain-of-Thought (CoT):** Ask model to reason step by step.
```
"Analyze the trend of topics in these JEE papers over 5 years.
Think step by step:
1. Count frequency of each topic per year
2. Identify upward trends
3. Predict which topics are likely in 2024
4. Rank by probability"
```

**4. Role prompting:**
```
"You are a 20-year veteran IIT JEE question setter who deeply understands
question pattern evolution. Analyze these papers..."
```

**5. Output format specification:**
```
"Respond ONLY in valid JSON with schema:
{
  'topic': string,
  'questions': [{'question': string, 'options': [4 strings], 'answer': int, 'explanation': string}]
}"
```

**6. Constitutional prompting / Self-critique:**
```
"Generate 5 exam questions.
Then review each question:
- Is it factually accurate?
- Is it appropriate difficulty for JEE?
- Does it have exactly one correct answer?
Revise any that fail these criteria."
```

**Production best practices:**
- Temperature 0 for factual/deterministic tasks (question validation).
- Temperature 0.7-0.9 for creative tasks (question generation).
- Always validate/parse LLM output — never trust format compliance blindly.
- Limit output format to JSON when downstream parsing is required.

---

# 14. Project Deep Dives

## 14.1 Exam Oracle — Deep Dive

### Architecture Questions

**Q43: Walk me through the entire Exam Oracle architecture.**

**Answer:**

```
User (HTTP Request)
        ↓
FastAPI API Layer
  - POST /predict → validate request, authenticate, submit Celery task
  - GET  /predictions/{task_id} → poll task status
        ↓
Celery Task Queue (Redis broker)
        ↓
Worker Process: 7-Agent Pipeline
┌─────────────────────────────────────────────────────────────────┐
│  1. CrawlerAgent    → Downloads exam PDFs from web/sources       │
│  2. ParserAgent     → pdfplumber extracts text, structures data  │
│  3. EmbedderAgent   → sentence-transformers → float vectors      │
│  4. AnalyzerAgent   → Topic extraction, frequency counting       │
│  5. PredictorAgent  → ARIMA + DBSCAN + frequency → ranked topics │
│  6. ValidatorAgent  → Validates predictions, removes noise       │
│  7. AssemblerAgent  → Generates questions via RAG + LLM cascade  │
└─────────────────────────────────────────────────────────────────┘
        ↓
ChromaDB (vector store for semantic search)
PostgreSQL (structured data: users, tasks, results)
Redis (task queue, caching, agent checkpoints)
        ↓
LLM Cascade: Groq → Gemini → Ollama (fallback chain)
        ↓
Result stored → User polls for completion → JSON response
```

**Design decisions and their rationale:**

1. **Why Celery vs async endpoint?** Prediction pipeline takes 30-120 seconds — can't hold HTTP connection open. Celery enables background processing with polling.

2. **Why ChromaDB vs Pinecone?** Free tier, local development, no API cost. For production at scale, Pinecone or Weaviate would be better.

3. **Why all-MiniLM-L6-v2?** Fast inference (384 dimensions vs 1536 for OpenAI), free, good semantic quality for academic content.

4. **Why ARIMA for trend detection?** Time-series model that captures autocorrelation in exam topic patterns (topics that trended up tend to continue trending).

5. **Why DBSCAN vs K-Means for clustering?** DBSCAN doesn't need predefined K, handles noise/outliers well (unusual topics become noise), works with cosine distance.

---

**Q44: How would you scale Exam Oracle to handle 10,000 concurrent prediction requests?**

**Answer:**
```
Current: Single Celery worker, local ChromaDB, single Redis
Problem at scale: Worker queue backlog, ChromaDB bottleneck, Redis memory limits

Scaled architecture:

Client → CDN → Load Balancer
                    ↓
          [FastAPI Cluster] × 5 instances
                    ↓
          [Redis Cluster] (task queue + caching)
          [Celery Workers] × 20 instances (autoscaling)
                    ↓
          [Worker pool tasks]
              ↓           ↓
        [Pinecone]   [PostgreSQL read replicas]
        (vector DB)  (structured data)
              ↓
    [LLM API Gateway] (load balance across Groq/Gemini/OpenAI)
              ↓
         [Ollama cluster] (local inference fallback)
```

**Specific optimizations:**
- Pre-compute and cache embeddings for common exam topics.
- Use Celery `chord` for parallel agent execution where possible.
- Implement request deduplication (same exam + same year → serve cached result).
- LLM response caching for identical prompts.

---

## 14.2 AI Voice Teller — Deep Dive

**Q45: Describe the AI Voice Teller architecture and your key design decisions.**

**Answer:**

```
Frontend (React)
      ↓ HTTP POST /generate-story
FastAPI Backend
      ↓
  ┌──────────────────────────────────────┐
  │ 1. Validate prompt (Pydantic)        │
  │ 2. Submit Celery task                │
  │ 3. Return task_id immediately        │
  └──────────────────────────────────────┘
      ↓ Background Celery task
  ┌──────────────────────────────────────┐
  │ 4. Google Gemini API → story text    │
  │ 5. Piper/TTS → audio (WAV/MP3)       │
  │ 6. Cache audio metadata/result in Redis│
  │ 7. Return a retrievable audio result   │
  └──────────────────────────────────────┘
      ↓ Client polls GET /story/{task_id}
  ┌──────────────────────────────────────┐
  │ 8. Return status + audio URL         │
  └──────────────────────────────────────┘
```

**Key design decisions:**

1. **Why async story generation?** TTS processing + LLM inference takes 15-60 seconds. Long-polling is better UX than blocking.

2. **Why Redis for result storage?** Fast read, TTL-based automatic cleanup. Stories don't need permanent storage — expire after 24h.

3. **Why Docker + Redis + Celery?** Docker keeps services reproducible, Celery moves slow generation off the request path, and Redis supports caching and task coordination.
4. **CORS management:** The React client and FastAPI service may have different origins, so the API should allow only the required frontend origins.

---

## 14.3 LLM-Powered SQL Generator — Deep Dive

**Q46: Walk me through your LLM-Powered SQL Generator and the engineering decisions behind it.**

**Answer:**
The project converts natural-language questions into optimized PostgreSQL queries through a five-stage agentic pipeline: request analysis, hybrid keyword plus pgvector retrieval, schema-aware SQL generation, autonomous validation/self-correction, and safe execution or a structured error response.

```python
import asyncio
import httpx
from pydantic import BaseModel
from typing import Optional, Any
import json
import deepdiff

class APIEndpointConfig(BaseModel):
    name: str
    old_base_url: str
    new_base_url: str
    path: str
    method: str = "GET"
    headers: dict = {}
    auth_token: Optional[str] = None

class ComparisonResult(BaseModel):
    endpoint: str
    status_match: bool
    payload_differences: dict
    schema_differences: dict
    old_response_time_ms: float
    new_response_time_ms: float
    pass_fail: str

class APIComparator:
    def __init__(self, config: APIEndpointConfig):
        self.config = config

    async def compare(self, params: dict = {}, body: dict = {}) -> ComparisonResult:
        headers = self.config.headers.copy()
        if self.config.auth_token:
            headers["Authorization"] = f"Bearer {self.config.auth_token}"

        async with httpx.AsyncClient() as client:
            # Run both APIs concurrently
            old_task = client.request(
                method=self.config.method,
                url=f"{self.config.old_base_url}{self.config.path}",
                params=params, json=body, headers=headers
            )
            new_task = client.request(
                method=self.config.method,
                url=f"{self.config.new_base_url}{self.config.path}",
                params=params, json=body, headers=headers
            )

            old_resp, new_resp = await asyncio.gather(old_task, new_task)

        # Deep comparison
        diff = deepdiff.DeepDiff(old_resp.json(), new_resp.json(), ignore_order=True)

        return ComparisonResult(
            endpoint=self.config.path,
            status_match=old_resp.status_code == new_resp.status_code,
            payload_differences=diff.get("values_changed", {}),
            schema_differences=diff.get("type_changes", {}),
            old_response_time_ms=old_resp.elapsed.total_seconds() * 1000,
            new_response_time_ms=new_resp.elapsed.total_seconds() * 1000,
            pass_fail="PASS" if not diff else "FAIL"
        )
```

**Resume-grounded result:** The hybrid retrieval system improved context relevance by 98%, while query caching and self-correction reduced redundant LLM calls by 80% and lowered average response latency. Be ready to explain the baseline and evaluation method behind each metric.

---

# 15. Internship Deep Dives

## 15.1 OneWealth (TECHAHEAD)

**Q47: Describe a technically complex problem you solved at OneWealth.**

**Answer (STAR Format):**

**Situation:** The advisor invitation lifecycle had a complex state machine — invitations could be pending, accepted, expired, revoked — and had to integrate with onboarding workflows triggered on acceptance.

**Task:** Design a fault-tolerant invitation system that handles invitation expiry, resend logic, and onboarding trigger on acceptance.

```python
from enum import Enum
from datetime import datetime, timedelta, timezone

class InvitationStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    EXPIRED = "expired"
    REVOKED = "revoked"
    RESENT = "resent"

class InvitationService:
    EXPIRY_HOURS = 72

    async def send_invitation(
        self,
        db: AsyncSession,
        inviter_id: int,
        invitee_email: str,
        role: str,
        firm_id: int
    ) -> Invitation:
        # Validate inviter has permission to invite for this role/firm
        inviter = await self.user_repo.get(db, inviter_id)
        if not self.can_invite(inviter, role):
            raise UnauthorizedException()

        # Check for existing pending invitation
        existing = await self.invitation_repo.get_active_by_email(db, invitee_email, firm_id)
        if existing:
            raise DuplicateInvitationException(invitee_email)

        token = secrets.token_urlsafe(32)
        invitation = await self.invitation_repo.create(db,
            email=invitee_email,
            token_hash=hashlib.sha256(token.encode()).hexdigest(),
            role=role,
            firm_id=firm_id,
            inviter_id=inviter_id,
            status=InvitationStatus.PENDING,
            expires_at=datetime.now(timezone.utc) + timedelta(hours=self.EXPIRY_HOURS)
        )

        await self.email_service.send_invitation_email(invitee_email, token, inviter.full_name)
        return invitation

    async def accept_invitation(self, db: AsyncSession, token: str, user_data: dict) -> User:
        token_hash = hashlib.sha256(token.encode()).hexdigest()
        invitation = await self.invitation_repo.get_by_token(db, token_hash)

        if not invitation:
            raise InvalidTokenException()
        if invitation.status != InvitationStatus.PENDING:
            raise InvalidTokenException(f"Invitation is {invitation.status}")
        if invitation.expires_at < datetime.now(timezone.utc):
            await self.invitation_repo.update_status(db, invitation.id, InvitationStatus.EXPIRED)
            raise ExpiredInvitationException()

        # Create user and trigger onboarding — all in one transaction
        async with db.begin():
            user = await self.user_repo.create(db, **user_data, firm_id=invitation.firm_id, role=invitation.role)
            await self.invitation_repo.update_status(db, invitation.id, InvitationStatus.ACCEPTED)
            await self.onboarding_service.initialize_onboarding(db, user.id)

        return user
```

**Result:** Zero invitation-related production bugs post-deployment. The state machine approach made it easy to add new invitation types.

---

**Q48: How did you implement async repository patterns in OneWealth? Why async?**

**Answer:**

```python
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy import select, update, delete
from typing import Generic, TypeVar, Type, List, Optional

# Why async PostgreSQL?
# OneWealth serves concurrent advisor/client requests.
# Async I/O means a single worker handles hundreds of concurrent DB-waiting requests
# instead of blocking a thread per request.

DATABASE_URL = "postgresql+asyncpg://user:pass@localhost:5432/onewealth"
engine = create_async_engine(DATABASE_URL, pool_size=10, max_overflow=20, pool_pre_ping=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

ModelT = TypeVar("ModelT")

class AsyncBaseRepository(Generic[ModelT]):
    def __init__(self, model: Type[ModelT], session: AsyncSession):
        self.model = model
        self.session = session

    async def get(self, id: int) -> Optional[ModelT]:
        return await self.session.get(self.model, id)

    async def get_multi(
        self,
        *,
        skip: int = 0,
        limit: int = 100,
        filters: dict = None
    ) -> List[ModelT]:
        query = select(self.model)
        if filters:
            for key, value in filters.items():
                query = query.where(getattr(self.model, key) == value)
        query = query.offset(skip).limit(limit)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create(self, **kwargs) -> ModelT:
        obj = self.model(**kwargs)
        self.session.add(obj)
        await self.session.flush()
        await self.session.refresh(obj)
        return obj

    async def update(self, id: int, **kwargs) -> Optional[ModelT]:
        await self.session.execute(
            update(self.model)
            .where(self.model.id == id)
            .values(**kwargs)
            .execution_options(synchronize_session="fetch")
        )
        return await self.get(id)

    async def delete(self, id: int) -> bool:
        obj = await self.get(id)
        if not obj:
            return False
        await self.session.delete(obj)
        return True
```

**Why `asyncpg` driver?** asyncpg is the fastest async PostgreSQL driver for Python — pure async, no synchronous fallbacks.

---

## 15.2 LLM SQL Generator — Project Deep Dive

**Q49: How would you make the SQL generator safe, reliable, and production-ready?**

**Answer:**
Treat the LLM as an untrusted planner, not as a database administrator. Validate generated SQL, restrict it to authorized read-only operations, enforce tenant scope, apply timeouts and result limits, and execute through a read-only database role.

**Reliability strategy:**
```
Phase 1: Validate generated SQL syntactically and semantically
Phase 2: Execute with a read-only role, timeout, and bounded result set
Phase 3: Capture feedback, cache safe results, and monitor failures

                    Traffic %
┌──────────────────────────────────────────────────────┐
│ Rails (old)  ████████████████████░░░░░░░░░░░░░░░░ │  80% → 0%
│ FastAPI (new)░░░░░░░░░░░░░░░░░░░░████████████████ │  20% → 100%
└──────────────────────────────────────────────────────┘
     Week 1-4          Week 5-8         Week 9-12
```

The rollout diagram above is a generic migration illustration retained for structure; it is not a claim that the resume describes a Rails migration.

**Evaluation role:** Maintain a benchmark of natural-language questions with expected SQL/results, then track execution correctness, result equivalence, retrieval relevance, latency, cost, and unsafe-query rejection rate.

**Migration challenges:**
1. **Hybrid retrieval:** Keyword search catches exact schema terms; pgvector catches semantically similar descriptions.
2. **Self-correction:** Retry only when the database error is actionable, and cap retries to avoid runaway cost.
3. **Caching:** Include schema/version and authorization scope in the cache key.
4. **Prompt injection:** Never let retrieved text or user input override system constraints.

---

# 16. System Design Round

## 16.1 Design a Fintech Trading Platform (OneWealth-scale)

**Q50: Design a system like OneWealth that handles 100,000 advisor-client interactions daily.**

**Answer:**

**Requirements:**
- Functional: Onboarding, authentication, portfolio management, document storage, advisor hierarchy.
- Non-functional: 99.99% uptime, sub-200ms API latency, GDPR compliance, data encryption.

**High-Level Architecture:**

```
Mobile/Web Client
        ↓
    CDN / DDoS protection
        ↓
    Cloud load balancer
        ↓
┌────────────────────────────────────────────────────┐
│              API Gateway (Kong / managed gateway)    │
│  Rate limiting · Auth validation · Request routing  │
└────────────────────────────────────────────────────┘
        ↓              ↓                 ↓
[Auth Service]  [User Service]    [Portfolio Service]
 (FastAPI)       (FastAPI)         (FastAPI)
    ↓                ↓                  ↓
[Auth DB]        [User DB]         [Portfolio DB]
(PostgreSQL)    (PostgreSQL)       (PostgreSQL)
                    ↓
              [Document Service]
               (FastAPI + object storage)
                    ↓
             [Notification Svc]
              (FastAPI + SES)
                    ↓
              [Event Bus: Kafka/SQS]
    (async events: user.created, document.uploaded, etc.)
```

**Database design for advisor hierarchy:**
```sql
-- Adjacency list model for advisor hierarchy
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    role VARCHAR(50) NOT NULL,
    firm_id INT REFERENCES firms(id),
    parent_advisor_id INT REFERENCES users(id),  -- Self-referential
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Fast hierarchy traversal index
CREATE INDEX idx_parent_advisor ON users(parent_advisor_id) WHERE parent_advisor_id IS NOT NULL;
CREATE INDEX idx_firm_active_role ON users(firm_id, role, is_active);
```

**Security considerations:**
- All PII encrypted at rest with managed keys from the selected cloud provider.
- Financial data: separate encryption keys per firm.
- Audit logs for all data access (GDPR compliance).
- JWT with 30-min expiry + refresh token rotation.

---

# 17. Mock Interview Section

## 17.1 Mock Interview #1 — Python Backend Role

**Interviewer:** "Tell me about yourself and your most challenging technical project."

**Model Answer:**
"I'm Tanmay Kushwaha, an MCA graduate currently working as a Python Developer Intern at TECHAHEAD, where I'm building production-grade backend systems for OneWealth, an enterprise fintech platform.

My most technically challenging project is Exam Oracle — an autonomous AI system that predicts exam questions for JEE, NEET, and UPSC using a 7-agent pipeline. The hard part wasn't building any single component, but designing a fault-tolerant pipeline where if agent 4 fails, you don't lose all the work done by agents 1-3. I solved this by implementing Redis-based checkpointing — each agent saves its state before passing to the next. On failure, the pipeline resumes from the last checkpoint instead of restarting entirely.

I'm looking for a role where I can combine my backend engineering experience with my growing AI/ML expertise."

---

**Technical Questions Flow:**

**Q:** "You mentioned async repository patterns — show me how your repository handles concurrent DB access."

**A:** [Explain AsyncSession + asyncpg + connection pooling as shown in Q48]

**Q:** "What happens if two advisors try to invite the same person simultaneously?"

**A:** "This is a race condition. I handle it with a unique constraint on `(email, firm_id)` in the invitations table AND application-level checking within a transaction. The DB constraint is the safety net even if the application check has a race window."

```sql
-- Database-level protection
CREATE UNIQUE INDEX idx_active_invitation 
ON invitations(email, firm_id) 
WHERE status = 'pending';  -- Partial unique index — only one active per email/firm
```

---

## 17.2 Mock Interview #2 — AI/GenAI Role

**Q:** "Explain the difference between fine-tuning and RAG. When would you use each?"

**A:**
| | RAG | Fine-tuning |
|---|---|---|
| **What it does** | Retrieves external context at inference time | Adjusts model weights on domain data |
| **Knowledge update** | Real-time (update vector DB) | Requires retraining |
| **Cost** | Low (inference + vector DB) | High (GPU training time) |
| **Hallucination** | Grounded in retrieved context | Can still hallucinate |
| **Best for** | Domain-specific Q&A, up-to-date info | Specific output style/format, classification |

"For Exam Oracle, I chose RAG because exam papers are updated yearly — I can just add new papers to ChromaDB without retraining. Fine-tuning would make sense if I needed the model to consistently output questions in a very specific XML format."

---

# 18. Rapid Fire Round

**Q: What is the Python GIL?**
A: Global Interpreter Lock — prevents multiple threads from executing Python bytecode simultaneously. Only one thread runs at a time. Released during I/O.

**Q: Difference between `__str__` and `__repr__`?**
A: `__repr__` is for developers (should be unambiguous, ideally recreatable). `__str__` is for end users (human-readable).

**Q: What is a generator expression?**
A: `(x**2 for x in range(10))` — lazy evaluation, memory efficient, only iterable once.

**Q: What is `functools.lru_cache`?**
A: Memoization decorator. Caches function return values by input arguments. `maxsize=None` means unlimited cache.

**Q: What HTTP status code for successful resource creation?**
A: 201 Created.

**Q: What HTTP status code when a resource is not found?**
A: 404 Not Found.

**Q: What is an ORM?**
A: Object-Relational Mapper. Maps database tables to Python classes. SQLAlchemy is Python's most popular ORM.

**Q: Difference between `INNER JOIN` and `LEFT JOIN`?**
A: INNER JOIN returns only matching rows. LEFT JOIN returns all rows from left table, matching or NULL for non-matching right table rows.

**Q: What is database connection pooling?**
A: Pre-creating a pool of DB connections to reuse, avoiding expensive connection setup per request. SQLAlchemy's `pool_size` configures this.

**Q: What is a Docker layer?**
A: Each instruction in a Dockerfile creates a read-only layer. Layers are cached — unchanged layers aren't rebuilt.

**Q: What is `asyncio.gather` vs `asyncio.wait`?**
A: `gather` collects all results, raises on first exception by default. `wait` gives more control — returns `done` and `pending` sets, configurable error handling.

**Q: What is idempotency?**
A: An operation that produces the same result if called multiple times. `GET`, `PUT`, `DELETE` should be idempotent. `POST` typically isn't.

**Q: What is a JWT claim?**
A: Key-value pair in the JWT payload. Standard claims: `sub` (subject/user ID), `exp` (expiry), `iat` (issued at), `iss` (issuer).

**Q: What is CORS?**
A: Cross-Origin Resource Sharing. Browser security mechanism preventing JavaScript from making requests to different origins. Server sends headers (`Access-Control-Allow-Origin`) to permit specific origins.

**Q: What is `SELECT N+1` problem?**
A: Executing N additional queries after an initial query. Example: Fetch 100 advisors (1 query), then fetch each advisor's clients (100 queries) = 101 queries. Fix: `JOIN` or SQLAlchemy `selectinload`.

**Q: What is cosine similarity?**
A: Measures angle between two vectors. Value between -1 and 1. 1 = identical direction. Used in semantic search because magnitude of embedding doesn't matter, only direction (meaning).

**Q: What is temperature in LLMs?**
A: Controls randomness. 0 = greedy (always top token), 1 = standard sampling. Higher = more creative/random.

**Q: What is a Pydantic BaseModel?**
A: Python class that provides runtime data validation and serialization via type hints. Core to FastAPI request/response handling.

**Q: What is Redis?**
A: In-memory data structure store. Used for caching, session storage, message queuing, rate limiting, pub/sub.

**Q: What is a foreign key?**
A: Column referencing the primary key of another table. Enforces referential integrity.

**Q: What is the difference between `==` and `is` in Python?**
A: `==` compares values. `is` compares identity (same object in memory). `None` checks should always use `is None`.

---

# 19. HR + Behavioral Questions

### Q51: "Why are you interested in backend development and AI?"

**Model Answer:**
"I built my first API during my BCA internship, and I was fascinated by how a few hundred lines of Python could power experiences for thousands of users. That got me deep into FastAPI and system design. The AI interest came when I started Exam Oracle — I realized that combining solid backend engineering with LLMs creates applications that weren't possible two years ago. For me, backend isn't just CRUD APIs; it's the foundation that makes AI applications reliable and scalable. That intersection is where I want to grow."

---

### Q52: "Tell me about a time you faced a challenging bug in production."

**Model Answer (STAR):**
"While building the LLM SQL Generator, a generated query was intermittently failing despite passing prompt-level checks. The error wasn't reproducible from a single happy-path example.

I added structured request, retrieval, SQL-validation, and database-error logging and found that a retrieved schema fragment was occasionally missing a required join relationship. I added schema-aware retrieval checks, a bounded self-correction retry, and a regression case for the failing question.

Fix: The service now validates generated SQL before execution, rejects unsafe or incomplete queries with a clear error, and records the failure for evaluation instead of returning an opaque 500.

Key lesson: Production errors are often at infrastructure boundaries, not just application code."

---

### Q53: "Where do you see yourself in 3 years?"

**Model Answer:**
"In three years, I want to be a mid-level engineer owning the design of production AI systems end-to-end — not just writing the code, but making architecture decisions: when to use RAG vs fine-tuning, how to design a vector search system that scales to millions of documents, how to make AI pipelines fault-tolerant.

I'm also very interested in the intersection of distributed systems and AI — things like distributed inference and agentic systems with persistence. I'd love to be at a company where I can push in that direction."

---

### Q54: "What is your greatest technical weakness?"

**Model Answer:**
"Honestly, my weakest area right now is Kubernetes. I'm comfortable with Docker and have used Docker Compose, but I haven't deployed a full K8s cluster in production. I know the concepts — pods, deployments, services, ingress — but I lack hands-on experience with K8s-specific failure scenarios like pod eviction, resource limits, and HPA autoscaling.

I've started working through the CKA syllabus and have set up a local minikube cluster to practice. I expect to close this gap over the next three to six months."

---

### Q55: "Describe your experience founding Webwright Solutions."

**Model Answer:**
"Webwright Solutions taught me things a classroom never could. I ran technical workshops at two engineering colleges and delivered web solutions for three small organizations. The hardest part wasn't technical — it was understanding client requirements. In one project, the client said they wanted a 'simple website,' but after the first demo, they wanted an admin dashboard, an inquiry form with email notifications, and an SEO-optimized blog. That experience taught me to do structured requirement gathering upfront and to set expectations in writing.

It also taught me the value of maintainable code — when a client needed a change six months later, my clean, documented code meant I could deliver in hours instead of days."

---

# 20. Final Revision Cheat Sheet

## Python Core — 10 Must-Know Concepts
1. GIL — prevents true multi-threading for CPU tasks; use multiprocessing or async for I/O.
2. Generators — `yield` for lazy evaluation; memory-efficient.
3. Decorators — Higher-order functions; `@functools.wraps` preserves metadata.
4. Context Managers — `with` statement; `__enter__`/`__exit__`; use `asynccontextmanager` for async.
5. asyncio — Single-threaded concurrency; `await` suspends; `gather` runs concurrently.
6. Memory management — Reference counting + cyclic GC; `__slots__` saves memory.
7. List comprehensions vs generators — `[x for x in range(n)]` vs `(x for x in range(n))`.
8. `*args` and `**kwargs` — Variable positional/keyword arguments.
9. `@property` — Getter/setter without explicit method calls.
10. `__dunder__` methods — Python data model for operator overloading.

## FastAPI — 10 Must-Know Concepts
1. `Depends()` — Dependency injection; cached per request by default.
2. `Pydantic BaseModel` — Request/response validation; `Field()` for constraints.
3. Path/Query/Body parameters — Different injection mechanisms.
4. `response_model` — Filters and validates output.
5. `BackgroundTasks` — Fire-and-forget async tasks.
6. Middleware — Intercepts all requests/responses.
7. `HTTPException` — Standard HTTP error responses.
8. `APIRouter` — Modular route organization.
9. `Security` vs `Depends` — `Security` adds OpenAPI auth metadata.
10. Lifespan events — `@app.on_event("startup")` / `@app.on_event("shutdown")`.

## Database — 10 Must-Know Concepts
1. ACID — Atomicity, Consistency, Isolation, Durability.
2. Indexing — B-Tree (default), GIN (JSONB), partial indexes.
3. `EXPLAIN ANALYZE` — Query execution plan; spot sequential scans.
4. N+1 problem — Use `JOIN` or `selectinload` in SQLAlchemy.
5. Transactions — `BEGIN`/`COMMIT`/`ROLLBACK`; nested transactions with savepoints.
6. Connection pooling — `pool_size`, `max_overflow` in SQLAlchemy engine.
7. `UPSERT` — `INSERT ... ON CONFLICT DO UPDATE`.
8. Normalization — 1NF/2NF/3NF; denormalize for read performance when needed.
9. Window functions — `RANK()`, `LAG()`, `LEAD()` over partitions.
10. Recursive CTEs — Hierarchical data traversal.

## AI/GenAI — 10 Must-Know Concepts
1. **RAG** — Retrieve → Augment → Generate; solves hallucination + knowledge cutoff.
2. **Embeddings** — Dense vectors representing semantic meaning; `all-MiniLM-L6-v2`.
3. **Vector DB** — Semantic similarity search; ChromaDB, Pinecone, pgvector.
4. **Cosine similarity** — Angle between vectors; direction matters, not magnitude.
5. **Chunking** — Text splitting strategy; chunk size + overlap are hyperparameters.
6. **Temperature** — 0 = deterministic, 1 = balanced, >1 = creative/random.
7. **Context window** — Max tokens the model processes; larger = more expensive.
8. **Prompt engineering** — Zero-shot, few-shot, CoT, role, output format.
9. **LangChain** — Framework: LLMs, Prompts, Chains, Retrievers, Agents.
10. **Agents** — LLMs with tools; decide what to call based on user intent.

## System Design Checklist
- [ ] Clarify requirements (functional + non-functional)
- [ ] Estimate scale (users, requests/sec, data volume)
- [ ] High-level architecture diagram
- [ ] Database design (schema, indexes)
- [ ] API design (endpoints, request/response)
- [ ] Scalability (horizontal scaling, caching)
- [ ] Reliability (failover, replication, backups)
- [ ] Security (auth, encryption, rate limiting)
- [ ] Monitoring & observability (metrics, logs, traces)

## Common Interview Traps to Avoid

1. **"I used Redis for caching"** → Interviewer will ask: What eviction policy? What happens on Redis crash? How do you handle cache invalidation?

2. **"I used JWT for auth"** → Know: How to revoke tokens, RS256 vs HS256, refresh token rotation, token storage (not localStorage!).

3. **"I used Docker"** → Know: CMD vs ENTRYPOINT, multi-stage builds, non-root users, secrets management.

4. **"I used async/await"** → Know: Blocking calls in async context destroy performance. `time.sleep()` vs `asyncio.sleep()`.

5. **"I did RAG"** → Know: Chunking strategy, embedding model choice, retrieval quality metrics, hybrid search.

---

## Quick Reference: HTTP Status Codes

| Code | Meaning | When to Use |
|---|---|---|
| 200 | OK | Successful GET, PUT, PATCH |
| 201 | Created | Successful POST (resource created) |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Invalid request data |
| 401 | Unauthorized | Missing/invalid authentication |
| 403 | Forbidden | Authenticated but insufficient permissions |
| 404 | Not Found | Resource doesn't exist |
| 409 | Conflict | Duplicate resource, state conflict |
| 422 | Unprocessable Entity | Validation error (FastAPI default) |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Unexpected server error |
| 503 | Service Unavailable | Server temporarily unavailable |

---

## SQLAlchemy Quick Reference

```python
# Select
result = await session.execute(select(User).where(User.email == email))
user = result.scalar_one_or_none()

# Joins
result = await session.execute(
    select(User, Firm)
    .join(Firm, User.firm_id == Firm.id)
    .where(User.is_active == True)
)

# Eager loading (solve N+1)
result = await session.execute(
    select(Advisor).options(selectinload(Advisor.clients))
)

# Update
await session.execute(
    update(User)
    .where(User.id == user_id)
    .values(is_active=False, updated_at=func.now())
)

# Delete
await session.execute(delete(Session).where(Session.user_id == user_id))
```

---

*This guide covers 55 core questions across 12 technical domains at 4 difficulty levels. Master all sections and you'll be well-prepared for Python Developer, Backend Developer, FastAPI Developer, Associate Software Engineer, SDE-1, AI Engineer, and Generative AI Engineer interviews.*

---
**Guide prepared based on resume analysis of Tanmay Kushwaha | June 2026**
