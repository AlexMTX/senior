* [^ Contents](../README.md)

<!-- TOC -->
* [Memory management](#memory-management)
  * [3 generations of GC](#3-generations-of-gc)
    * [module gc](#module-gc)
    * [Which type of objects are tracked?](#which-type-of-objects-are-tracked)
  * [Recommendations for GC usage](#recommendations-for-gc-usage)
  * [Memory leaks and deleters issues](#memory-leaks-and-deleters-issues)
<!-- TOC -->

# Memory management

## 3 generations of GC

The main garbage collection algorithm used by CPython is reference counting. The basic idea is that CPython counts how
many different places there are that have a reference to an object. Such a place could be another object, or a global (
or static) C variable, or a local variable in some C function. When an object’s reference count becomes zero, the object
is deallocated. If it contains references to other objects, their reference counts are decremented. Those other objects
may be deallocated in turn, if this decrement makes their reference count become zero, and so on. The reference count
field can be examined using the sys.getrefcount function (notice that the value returned by this function is always 1
more as the function also has a reference to the object when called):

```python
x = object()
print(sys.getrefcount(x))
# 2
y = x
print(sys.getrefcount(x))
# 3
del y
print(sys.getrefcount(x))
# 2
```

The main problem with the reference counting scheme is that it does not handle reference cycles. For instance, consider
this code:

```python
container = []
container.append(container)
print(sys.getrefcount(container))
# 3
del container
```

In this example, container holds a reference to itself, so even when we remove our reference to it (the variable
“container”) the reference count never falls to 0 because it still has its own internal reference. Therefore it would
never be cleaned just by simple reference counting. For this reason some additional machinery is needed to clean these
reference cycles between objects once they become unreachable. This is the cyclic garbage collector, usually called just
Garbage Collector (GC), even though reference counting is also a form of garbage collection.

In order to limit the time each garbage collection takes, the GC uses a popular optimization: generations. The main idea
behind this concept is the assumption that most objects have a very short lifespan and can thus be collected shortly
after their creation. This has proven to be very close to the reality of many Python programs as many temporary objects
are created and destroyed very fast. The older an object is the less likely it is that it will become unreachable.

To take advantage of this fact, all container objects are segregated into three spaces/generations. Every new object
starts in the first generation (generation 0). The previous algorithm is executed only over the objects of a particular
generation and if an object survives a collection of its generation it will be moved to the next one (generation 1),
where it will be surveyed for collection less often. If the same object survives another GC round in this new
generation (generation 1) it will be moved to the last generation (generation 2) where it will be surveyed the least
often.

Generations are collected when the number of objects that they contain reaches some predefined threshold, which is
unique for each generation and is lower the older the generations are. These thresholds can be examined using the
gc.get_threshold function:

### module gc

```python
import gc
print(gc.get_threshold())
# (700, 10, 10)
```

```python
import gc
print(gc.get_count())
# (596, 2, 1)
```

You can trigger a manual garbage collection process by using the `gc.collect()` method

```python
import gc
class MyObj:
    pass

# Move everything to the last generation so it's easier to inspect
# the younger generations.

gc.collect()
# 0

# Create a reference cycle.

x = MyObj()
x.self = x

# Initially the object is in the youngest generation.

gc.get_objects(generation=0)
# [..., <__main__.MyObj object at 0x7fbcc12a3400>, ...]

# After a collection of the youngest generation the object
# moves to the next generation.
gc.collect(generation=0)
# 0
gc.get_objects(generation=0)
# []
gc.get_objects(generation=1)
# [..., <__main__.MyObj object at 0x7fbcc12a3400>, ...]
```

The garbage collector module provides the Python function is_tracked(obj), which returns the current tracking status of
the object.

The oldest generation is collected when `long_lived_pending / long_lived_total > 25%`. Amortized linear
performance. Fewer collections as the number of long living objects grows.

### Which type of objects are tracked?

As a general rule, instances of atomic types aren’t tracked and instances of non-atomic types (containers, user-defined
objects…) are. However, some type-specific optimizations can be present in order to suppress the garbage collector
footprint of simple instances. Some examples of native types that benefit from delayed tracking:
- Tuples containing only immutable objects (integers, strings etc, and recursively, tuples of immutable objects) do not
need to be tracked
- Dictionaries containing only immutable objects also do not need to be tracked

## Recommendations for GC usage

General rule: Don’t change garbage collector behavior

## Memory leaks and deleters issues

The Python program, just like other programming languages, experiences memory leaks. Memory leaks in Python happen if
the garbage collector doesn't clean and eliminate the unreferenced or unused data from Python.

Python developers have tried to address memory leaks through the addition of features that free unused memory
automatically.

However, some unreferenced objects may pass through the garbage collector unharmed, resulting in memory leaks.

`tracemalloc` (trace_memory_allocation) to detect leaks, `gc.set_debug`
