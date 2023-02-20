<!-- TOC -->
* [Unit testing in Python](#unit-testing-in-python)
  * [Mock objects](#mock-objects)
  * [Coverage](#coverage)
  * [nosetests, doctests, pytest](#nosetests-doctests-pytest)
<!-- TOC -->

# Unit testing in Python

## Mock objects

A mock object substitutes and imitates a real object within a testing environment. It is a versatile and powerful tool
for improving the quality of your tests.

One reason to use Python mock objects is to control your code’s behavior during testing.

For example, if your code makes HTTP requests to external services, then your tests execute predictably only so far as
the services are behaving as you expected. Sometimes, a temporary change in the behavior of these external services can
cause intermittent failures within your test suite.

```python
from unittest.mock import Mock
mock = Mock()
print(mock)
# <Mock id='4561344720'>
```

A Mock must simulate any object that it replaces. To achieve such flexibility, it creates its attributes when you access
them.

```python
from unittest.mock import Mock

# Create a mock object
json = Mock()

json.loads('{"key": "value"}')
# <Mock name='mock.loads()' id='4550144184'>

# You know that you called loads() so you can
# make assertions to test that expectation
json.loads.assert_called()
json.loads.assert_called_once()
json.loads.assert_called_with('{"key": "value"}')
json.loads.assert_called_once_with('{"key": "value"}')
```

```python
datetime = Mock()
datetime.datetime.today.return_value = "tuesday"
requests = Mock()
requests.get.side_effect = Timeout
```

```python
@patch('my_calendar.requests')
def test_get_holidays_timeout(self, mock_requests):
    mock_requests.get.side_effect = Timeout
```

or

```python
with patch('my_calendar.requests') as mock_requests:
    mock_requests.get.side_effect = Timeout
```

And there are MagicMock and Async Mock as well.

## Coverage

Coverage.py is one of the most popular code coverage tools for Python. It uses code analysis tools and tracing hooks
provided in Python standard library to measure coverage. It runs on major versions of CPython, PyPy, Jython and
IronPython. You can use Coverage.py with both unittest and Pytest.

## nosetests, doctests, pytest

`nose2` is the successor to nose. It’s unittest with plugins.
`nose2` is a new project and does not support all the features of nose. See differences for a thorough rundown.
`nose2`’s purpose is to extend unittest to make testing nicer and easier to understand.

nose2 vs pytest
nose2 may or may not be a good fit for your project.

If you are new to python testing, we encourage you to also consider `pytest`, a popular testing framework.

The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those
sessions to verify that they work exactly as shown. There are several common ways to use doctest:

- To check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as
  documented.
- To perform regression testing by verifying that interactive examples from a test file or a test object work as
  expected.
- To write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether
  the examples or the expository text are emphasized, this has the flavor of “literate testing” or “executable
  documentation”.

`python example.py -v`

