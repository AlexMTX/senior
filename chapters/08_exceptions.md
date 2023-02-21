* [^ Contents](../README.md)

<!-- TOC -->
* [Exceptions](#exceptions)
  * [Context managers, contextlib decorator, with-enabled class](#context-managers-contextlib-decorator-with-enabled-class)
    * [Links](#links)
  * [traces](#traces)
<!-- TOC -->

# Exceptions

## Context managers, contextlib decorator, with-enabled class

The with statement in Python is a quite useful tool for properly managing external resources in your programs. It allows
you to take advantage of existing context managers to automatically handle the setup and teardown phases whenever you’re
dealing with external resources or with operations that require those phases.

Besides, the context management protocol allows you to create your own context managers, and you can customize the way you
deal with system resources.

```python
class WritableFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.file_obj = open(self.file_path, mode="w")
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_obj:
            self.file_obj.close()
```

```python
from contextlib import contextmanager

@contextmanager
def writable_file(file_path):
    file = open(file_path, mode="w")
    try:
        yield file
    finally:
        file.close()

with writable_file("hello.txt") as file:
    file.write("Hello, World!")
```

```python
import aiohttp
import asyncio

class AsyncSession:
    def __init__(self, url):
        self._url = url

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        response = await self.session.get(self._url)
        return response

    async def __aexit__(self, exc_type, exc_value, exc_tb):
        await self.session.close()

async def check(url):
    async with AsyncSession(url) as response:
        print(f"{url}: status -> {response.status}")
        html = await response.text()
        print(f"{url}: type -> {html[:17].strip()}")

async def main():
    await asyncio.gather(
        check("https://realpython.com"),
        check("https://pycoders.com"),
    )

asyncio.run(main())
```

```python
from contextlib import AbstractContextManager

class MyContextManager(AbstractContextManager):
    def __enter__(self):
        print("entering context manager")
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        print("exiting context manager")
        return None

with MyContextManager() as cm:
    print("something")
```

### Links
- https://realpython.com/python-with-statement/
- https://docs.python.org/3/library/contextlib.html


## traces
todo