<!-- TOC -->
* [Troubleshooting](#troubleshooting)
  * [Types of profilers, static and dynamic profilers](#types-of-profilers-static-and-dynamic-profilers)
    * [`trace` module](#trace-module)
    * [`faulthandler` module](#faulthandler-module)
    * [application performance monitoring or APM, tools that fit](#application-performance-monitoring-or-apm-tools-that-fit)
    * [What part of the code should I profile?](#what-part-of-the-code-should-i-profile)
    * [Typically, we profile](#typically-we-profile)
    * [What metrics should I profile?](#what-metrics-should-i-profile)
    * [Memory profiling](#memory-profiling)
    * [Deterministic profiling versus statistical profiling](#deterministic-profiling-versus-statistical-profiling)
    * [`pyinstrument`](#pyinstrument)
  * [`resource` module](#resource-module)
<!-- TOC -->

# Troubleshooting

## Types of profilers, static and dynamic profilers

Serious software development calls for performance optimization. When you start optimizing application performance, you
can’t escape looking at profilers. Whether monitoring production servers or tracking frequency and duration of method
calls, profilers run the gamut

### `trace` module

You can do several things with trace:

1. Produce a code coverage report to see which lines are run or skipped
   over (`python3 -m trace –count trace_example/main.py`).
2. Report on the relationships between functions that call one
   other (`python3 -m trace –listfuncs trace_example/main.py | grep -v importlib`).
3. Track which function is the
   caller (`python3 -m trace –listfuncs –trackcalls trace_example/main.py | grep -v importlib`).

### `faulthandler` module

By contrast, faulthandler has slightly better Python documentation. It states that its purpose is to dump Python
tracebacks explicitly on a fault, after a timeout, or on a user signal. It also works well with other system fault
handlers like Apport or the Windows fault handler. Both the faulthandler and trace modules provide more tracing
abilities and can help you debug your Python code. For more profiling statistics, see the next section.

If you’re a beginner to tracing, I recommend you start simple with trace.

### application performance monitoring or APM, tools that fit

Datadog in my production

### What part of the code should I profile?

Now let’s delve into profiling specifics. The term “profiling” is mainly used for performance testing, and the purpose
of performance testing is to find bottlenecks by doing deep analysis. So you can use tracing tools to help you with
profiling. Recall that tracing is when software developers log information about a software execution. Therefore,
logging performance metrics is also a way to perform profiling analysis.

But we’re not restricted to tracing. As profiling gains mindshare in the mainstream, we now have tools that perform
profiling directly. Now the question is, what parts of the software do we profile (measure its performance metrics)?

### Typically, we profile

- Method or function (most common)
- Lines (similar to method profiling, but doing it line by line)
- Memory (memory usage)

### What metrics should I profile?

- Speed (time)
- Calls (frequency)
- Method and line profiling

Both cProfile and profile are modules available in the Python 3 language. The numbers produced by these modules can be
formatted into reports via the pstats module.

Here’s an example of cProfile showing the numbers for a script:

```python
import cProfile
import re

cProfile.run('re.compile("foo|bar")')
# 197 function calls (192 primitive calls) in 0.002 seconds
```

### Memory profiling

Another common component to profile is the memory usage. The purpose is to find memory leaks and optimize the memory
usage in your Python programs. In terms of generic Python options, the most recommended tools for memory profiling for
Python 3 are the `pympler` and the `objgraph` libraries.

```python
from pympler import classtracker
tr = classtracker.ClassTracker()
tr.track_class(Document)
tr.create_snapshot()
create_documents()
tr.create_snapshot()
tr.stats.print_summary()
# active 1.42 MB average pct
# Document 1000 195.38 KB 200 B 13%
```

### Deterministic profiling versus statistical profiling

When we do profiling, it means we need to monitor the execution. That in itself may affect the underlying software being
monitored. Either we monitor all the function calls and exception events, or we use random sampling and deduce the
numbers. The former is known as deterministic profiling, and the latter is statistical profiling. Of course, each method
has its pros and cons. Deterministic profiling can be highly precise, but its extra overhead may affect its accuracy.
Statistical profiling has less overhead in comparison, with the drawback being lower precision.

cProfile, which I covered earlier, uses deterministic profiling. Let’s look at another open source Python profiler that
uses statistical profiling: pyinstrument.

### `pyinstrument`

Pyinstrument differentiates itself from other typical profilers in two ways. First, it emphasizes that it uses
statistical profiling instead of deterministic profiling. It argues that while deterministic profiling can give you more
precision than statistical profiling, the extra precision requires more overhead. The extra overhead may affect the
accuracy and lead to optimizing the wrong part of the program. Specifically, it states that using deterministic
profiling means that “code that makes a lot of Python function calls invokes the profiler a lot, making it slower.” This
is how results get distorted and the wrong part of the program gets optimized.

## `resource` module

This module provides basic mechanisms for measuring and controlling system resources utilized by a program.

Symbolic constants are used to specify particular system resources and to request usage information about either the
current process or its children.

`resource.getrusage(who)`
This function returns an object that describes the resources consumed by either the current process or its children, as
specified by the who parameter. The who parameter should be specified using one of the RUSAGE_* constants described
below.

A simple example:

```python
from resource import *
import time

# a non CPU-bound task
time.sleep(3)
print(getrusage(RUSAGE_SELF))

# a CPU-bound task
for i in range(10 ** 8):
    _ = 1 + 1
print(getrusage(RUSAGE_SELF))
```
