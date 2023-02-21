* [^ Contents](../README.md)

<!-- TOC -->
* [Threading and multiprocessing](#threading-and-multiprocessing)
  * [GIL, Definition, Algorithms in 2.x and 3.x](#gil-definition-algorithms-in-2x-and-3x)
  * [Threads, modules thread, threading, class Queue, locks](#threads-modules-thread-threading-class-queue-locks)
  * [Processes, multiprocessing, Process, Queue, Pipe, Value, Array, Pool, Manager](#processes-multiprocessing-process-queue-pipe-value-array-pool-manager)
  * [How to avoid GIL restrictions, C extensions](#how-to-avoid-gil-restrictions-c-extensions)
<!-- TOC -->

# Threading and multiprocessing

## GIL, Definition, Algorithms in 2.x and 3.x

The mechanism used by the CPython interpreter to assure that only one thread executes Python bytecode at a time. This
simplifies the CPython implementation by making the object model (including critical built-in types such as dict)
implicitly safe against concurrent access. Locking the entire interpreter makes it easier for the interpreter to be
multi-threaded, at the expense of much of the parallelism afforded by multi-processor machines.

However, some extension modules, either standard or third-party, are designed so as to release the GIL when doing
computationally-intensive tasks such as compression or hashing. Also, the GIL is always released when doing I/O.

Past efforts to create a “free-threaded” interpreter (one which locks shared data at a much finer granularity) have not
been successful because performance suffered in the common single-processor case. It is believed that overcoming this
performance issue would make the implementation much more complicated and therefore costlier to maintain.

```python
import sys
# The interval is set to 100 instructions:
sys.getcheckinterval()
# 100
```

The problem in this mechanism was that most of the time the CPU-bound thread would reacquire the GIL itself before other
threads could acquire it. This was researched by David Beazley and visualizations can be found here.

This problem was fixed in Python 3.2 in 2009 by Antoine Pitrou who added a mechanism of looking at the number of GIL
acquisition requests by other threads that got dropped and not allowing the current thread to reacquire GIL before other
threads got a chance to run.

## Threads, modules thread, threading, class Queue, locks

Straight forward:

```python
from time import sleep, perf_counter
from threading import Thread

def task():
    print('Starting a task...')
    sleep(1)
    print('done')

start_time = perf_counter()

# create two new threads
t1 = Thread(target=task)
t2 = Thread(target=task)

# start the threads
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()

end_time = perf_counter()

print(f'It took {end_time - start_time: 0.2f} second(s) to complete.')
```

Better:

```python
from concurrent.futures import ThreadPoolExecutor
from time import sleep
 
values = [3,4,5,6]
 
def cube(x):
    print(f'Cube of {x}:{x*x*x}')
 
 
if __name__ == '__main__':
    result = []
    with ThreadPoolExecutor(max_workers=5) as exe:
        exe.submit(cube, 2)

        # Maps the method 'cube' with a list of values.
        result = exe.map(cube, values)

    for r in result:
        print(r)
```

Operations associated with `queue.Queue` are:

- `maxsize` – Number of items allowed in the queue.
- `empty()` – Return True if the queue is empty, False otherwise.
- `full()` – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the
  default), then full() never returns True.
- `get()` – Remove and return an item from the queue. If queue is empty, wait until an item is available.
- `get_nowait()` – Return an item if one is immediately available, else raise QueueEmpty.
- `put(item)` – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the
  item.
- `put_nowait(item)` – Put an item into the queue without blocking. If no free slot is immediately available, raise
  QueueFull.
- `qsize()` – Return the number of items in the queue.

## Processes, multiprocessing, Process, Queue, Pipe, Value, Array, Pool, Manager

Simple case:

```python
#!/usr/bin/python

from multiprocessing import Process
import time

def fun():
    print('starting fun')
    time.sleep(2)
    print('finishing fun')

def main():
    p = Process(target=fun)
    p.start()
    p.join()


if __name__ == '__main__':
    print('starting main')
    main()
    print('finishing main')
```

Nice pool:

```python
#!/usr/bin/python

import time
from timeit import default_timer as timer
from multiprocessing import Pool, cpu_count

def square(n):
    time.sleep(2)
    return n * n

def main():
    start = timer()
    print(f'starting computations on {cpu_count()} cores')
    values = (2, 4, 6, 8)

    with Pool() as pool:
        res = pool.map(square, values)
        print(res)

    end = timer()
    print(f'elapsed time: {end - start}')

if __name__ == '__main__':
    main()
```

`pipes` — Interface to shell pipelines. The pipes module defines a class to abstract the concept of a pipeline — a
sequence of converters from one file to another.

## How to avoid GIL restrictions, C extensions

Only C treads:

```c
#include "Python.h"
...
PyObject *pyfunc(PyObject *self, PyObject *args)
{
    ...
    Py_BEGIN_ALLOW_THREADS
      
    // Threaded C code. 
    // Must not use Python API functions
    ...
    Py_END_ALLOW_THREADS
    ...
    return result;
}
```

Mixing C and Python (please don't do it without glasses):

```c
include <Python.h>
...
if (!PyEval_ThreadsInitialized())
{
    PyEval_InitThreads();
}
...
```
