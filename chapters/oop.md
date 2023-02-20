<!-- TOC -->
* [OOP](#oop)
  * [SOLID](#solid)
  * [The four basics of object-oriented programming](#the-four-basics-of-object-oriented-programming)
  * [abstract base class](#abstract-base-class)
  * [getattr, setattr functions](#getattr-setattr-functions)
  * [getattr, setattr, delattr magic methods](#getattr-setattr-delattr-magic-methods)
  * [getattribute magic method](#getattribute-magic-method)
  * [Name mangling](#name-mangling)
  * [Property](#property)
  * [init, repr, str, cmp, new , del, hash, nonzero, unicode, class operators](#init-repr-str-cmp-new--del-hash-nonzero-unicode-class-operators)
  * [Rich comparison methods](#rich-comparison-methods)
  * [call magic method](#call-magic-method)
  * [Multiple inheritance](#multiple-inheritance)
  * [Classic algorithm](#classic-algorithm)
  * [Diamond problem](#diamond-problem)
  * [MRO, super](#mro-super)
  * [Mixins](#mixins)
  * [Metaclass definition](#metaclass-definition)
  * [type, isinstance, issubclass functions](#type-isinstance-issubclass-functions)
    * [type parameters](#type-parameters)
    * [type return value](#type-return-value)
  * [slots](#slots)
<!-- TOC -->

# OOP

## SOLID

In software engineering, SOLID is a mnemonic acronym for five design principles intended to make software designs more
understandable, flexible, and maintainable. The principles are a subset of many principles promoted by American software
engineer and instructor Robert C. Martin, first introduced in his 2000 paper Design Principles and Design Patterns.

The SOLID ideas are

- The single-responsibility principle: "There should never be more than one reason for a class to change." In other
  words, every class should have only one responsibility.
- The open–closed principle: "Software entities ... should be open for extension, but closed for modification."
- The Liskov substitution principle: "Functions that use pointers or references to base classes must be able to use
  objects of derived classes without knowing it." See also design by contract.
- The interface segregation principle: "Many client-specific interfaces are better than one general-purpose interface."
- The dependency inversion principle: "Depend upon abstractions, not concretions."

The SOLID acronym was introduced later, around 2004, by Michael Feathers.

https://github.com/heykarimoff/solid.python

## The four basics of object-oriented programming

- Encapsulation - binding the data and functions which operate on that data into a single unit, the class

- Abstraction - treating a system as a “black box,” where it’s not important to understand the gory inner workings in
  order to reap the benefits of using it.

- Inheritance - if a class inherits from another class, it automatically obtains a lot of the same functionality and
  properties from that class and can be extended to contain separate code and data. A nice feature of inheritance is
  that it often leads to good code reuse since a parent class’ functions don’t need to be re-defined in any of its child
  classes.

- Polymorphism - Because derived objects share the same interface as their parents, the calling code can call any
  function in that class’ interface. At run-time, the appropriate function will be called depending on the type of
  object passed leading to possibly different behaviors.

## abstract base class

They make sure that derived classes implement methods and properties dictated in the abstract base class.
Abstract base classes separate the interface from the implementation. They define generic methods and properties that
must be used in subclasses. Implementation is handled by the concrete subclasses where we can create objects that can
handle tasks.
They help to avoid bugs and make the class hierarchies easier to maintain by providing a strict recipe to follow for
creating subclasses.

```python
from abc import ABCMeta, abstractmethod

class AbstractClassCSV(metaclass = ABCMeta):  # or just inherits from ABC, helper class
    def __init__(self, path, file_name):
       self._path = path
       self._file_name = file_name
        
    @property
    @abstractmethod
    def path(self):
        pass
```

## getattr, setattr functions

`hasattr(object, name)` function:

Determines whether an object has a name attribute or a name method, returns a bool value, returns True with a name
attribute, or returns False.

`getattr(object, name[,default])` function:

Gets the property or method of the object, prints it if it exists, or prints the default value if it does not exist,
which is optional.

`setattr(object, name, values)` function:

Assign a value to an object's property. If the property does not exist, create it before assigning it.

## getattr, setattr, delattr magic methods

```python
# this example uses __setattr__ to dynamically change attribute value to uppercase
class Frob:
    def __setattr__(self, name, value):
        self.__dict__[name] = value.upper()

f = Frob()
f.bamf = "bamf"
print(f.bamf)
# 'BAMF'
```

Note that if the attribute is found through the normal mechanism, `__getattr__()` is not called. (This is an intentional
asymmetry between `__getattr__()` and `__setattr__()`.) This is done both for efficiency reasons and because
otherwise `__getattr__()` would have no way to access other attributes of the instance.

```python
class Frob:
    def __init__(self, bamf):
        self.bamf = bamf
    def __getattr__(self, name):
        return 'Frob does not have `{}` attribute.'.format(str(name))

f = Frob("bamf")
print(f.bar)
# 'Frob does not have `bar` attribute.'
print(f.bamf)
# 'bamf'
```

## getattribute magic method

If the class also defines `__getattr__()`, the latter will not be called unless `__getattribute__()` either calls it
explicitly or raises an AttributeError.

```python
class Frob(object):
    def __getattribute__(self, name):
        print("getting `{}`".format(str(name)))
        object.__getattribute__(self, name)

f = Frob()
f.bamf = 10
print(f.bamf)
# getting `bamf`
```

## Name mangling

In name mangling process any identifier with two leading underscore and one trailing underscore is textually replaced
with `_classname__identifier` where classname is the name of the current class. It means that any identifier of the
form `__geek` (at least two leading underscores or at most one trailing underscore) is replaced with `_classname__geek`,
where classname is the current class name with leading underscore(s) stripped.

```python
class Student:
    def __init__(self, name):
        self.__name = name
  
s1 = Student("Santhosh")
print(s1._Student__name)
```

## Property

`@property(getter, setter, deleter)`

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('Getting name')
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name

p = Person('Adam')
print('The name is:', p.name)
p.name = 'John'
del p.name
```

## init, repr, str, cmp, new , del, hash, nonzero, unicode, class operators

- `__init__` The task of constructors is to initialize(assign values) to the data members of the class when an object of
  class is created.
- `repr()` The repr() function returns a printable representation of the given object.
- The `__str__` method in Python represents the class objects as a string – it can be used for classes. The __str__
  method should be defined in a way that is easy to read and outputs all the members of the class. This method is also
  used as a debugging tool when the members of a class need to be checked.
- `__cmp__` is no longer used.
- `__mew__` Whenever a class is instantiated `__new__` and `__init__` methods are called. `__new__` method will be
  called when an object is created and `__init__` method will be called to initialize the object.

```python
class A(object):
    def __new__(cls):
        print("Creating instance")
        return super(A, cls).__new__(cls)
  
    def __init__(self):
        print("Init is called")
```

Output:

- Creating instance
- Init is called

- `__del__` The `__del__()` method is a known as a destructor method in Python. It is called when all references to the
  object have been deleted i.e when an object is garbage collected. Note : A reference to objects is also deleted when
  the object goes out of reference or when the program ends
- `__hash__()`

```python
class A(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def __eq__(self, othr):
        return (isinstance(othr, type(self))
                and (self._a, self._b, self._c) ==
                    (othr._a, othr._b, othr._c))

    def __hash__(self):
        return hash((self._a, self._b, self._c))
```

## Rich comparison methods

`__lt__`, `__gt__`, `__le__`, `__ge__`, `__eq__`, and `__ne__`

```python
def __lt__(self, other):
    ...
def __le__(self, other):
    ...
def __gt__(self, other):
    ...
def __ge__(self, other):
    ...
def __eq__(self, other):
    ...
def __ne__(self, other):
    ...
```

## call magic method

`object()` is shorthand for `object.__call__()`

```python
class Product:
    def __init__(self):
        print("Instance Created")
  
    # Defining __call__ method
    def __call__(self, a, b):
        print(a * b)
  
# Instance created
ans = Product()
  
# __call__ method will be called
ans(10, 20)
```

## Multiple inheritance

Python has known at least three different MRO algorithms: classic, Python 2.2 new-style, and Python 2.3 new-style (
a.k.a. C3). Only the latter survives in Python 3.

## Classic algorithm

Classic classes used a simple MRO scheme: when looking up a method, base classes were searched using a simple
depth-first left-to-right scheme. The first matching object found during this search would be returned. For example,
consider these classes:

```python
class A:
  def save(self): pass

class B(A): pass

class C:
  def save(self): pass

class D(B, C): pass
```

If we created an instance x of class D, the classic method resolution order would order the classes as D, B, A, C. Thus,
a search for the method x.save() would produce A.save() (and not C.save()).

## Diamond problem

One problem concerns method lookup under "diamond inheritance." For example:

```python
class A:
  def save(self): pass

class B(A): pass

class C(A):
  def save(self): pass

class D(B, C): pass
```

Here, class D inherits from B and C, both of which inherit from class A. Using the classic MRO, methods would be found
by searching the classes in the order D, B, A, C, A. Thus, a reference to x.save() will call A.save() as before.
However, this is unlikely what you want in this case! Since both B and C inherit from A, one can argue that the
redefined method C.save() is actually the method that you want to call, since it can be viewed as being "more
specialized" than the method in A (in fact, it probably calls A.save() anyways). For instance, if the save() method is
being used to save the state of an object, not calling C.save() would break the program since the state of C would be
ignored.

Although this kind of multiple inheritance was rare in existing code, new-style classes would make it commonplace. This
is because all new-style classes were defined by inheriting from a base class object. Thus, any use of multiple
inheritance in new-style classes would always create the diamond relationship described above. For example:

````python
class B(object): pass

class C(object):
  def __setattr__(self, name, value): pass

class D(B, C): pass
````

Moreover, since object defined a number of methods that are sometimes extended by subtypes (e.g., __setattr__()), the
resolution order becomes critical. For example, in the above code, the method C.__setattr__ should apply to instances of
class D.

To fix the method resolution order for new-style classes in Python 2.2, G. adopted a scheme where the MRO would be
pre-computed when a class was defined and stored as an attribute of each class object. The computation of the MRO was
officially documented as using a depth-first left-to-right traversal of the classes as before. If any class was
duplicated in this search, all but the last occurrence would be deleted from the MRO list. So, for our earlier example,
the search order would be D, B, C, A (as opposed to D, B, A, C, A with classic classes).

In reality, the computation of the MRO was more complex than this. Guido discovered a few cases where this new MRO
algorithm didn't seem to work. Thus, there was a special case to deal with a situation when two bases classes occurred
in a different order in the inheritance list of two different derived classes, and both of those classes are inherited
by yet another class. For example:

```python
class A(object): pass
class B(object): pass
class X(A, B): pass
class Y(B, A): pass
class Z(X, Y): pass
```

Using the tentative new MRO algorithm, the MRO for these classes would be Z, X, Y, B, A, object. (Here 'object' is the
universal base class.) However, I didn't like the fact that B and A were in reversed order. Thus, the real MRO would
interchange their order to produce Z, X, Y, A, B, object.

## MRO, super

Thus, in Python 2.3, we abandoned my home-grown 2.2 MRO algorithm in favor of the academically vetted C3 algorithm. One
outcome of this is that Python will now reject any inheritance hierarchy that has an inconsistent ordering of base
classes. For instance, in the previous example, there is an ordering conflict between class X and Y. For class X, there
is a rule that says class A should be checked before class B. However, for class Y, the rule says that class B should be
checked before A. In isolation, this discrepancy is fine, but if X and Y are ever combined together in the same
inheritance hierarchy for another class (such as in the definition of class Z), that class will be rejected by the C3
algorithm. This, of course, matches the Zen of Python's "errors should never pass silently" rule.

**In Python, the MRO is from bottom to top and left to right. This means that, first, the method is searched in the
class of the object. If it’s not found, it is searched in the immediate super class. In the case of multiple super
classes, it is searched left to right, in the order by which was declared by the developer. For example:**

## Mixins

A mixin is a special kind of multiple inheritance. There are two main situations where mixins are used:

- You want to provide a lot of optional features for a class.
- You want to use one particular feature in a lot of different classes.

## Metaclass definition

Metaclasses are the 'stuff' that creates classes.

You define classes in order to create objects, right?

But we learned that Python classes are objects.

Well, metaclasses are what create these objects. They are the classes' classes, you can picture them this way:

```python
MyClass = MetaClass()
my_object = MyClass()

# You've seen that type lets you do something like this:

MyClass = type('MyClass', (), {})
```

## type, isinstance, issubclass functions

### type parameters
The `type()` function either takes a single object parameter.

Or, it takes 3 parameters

`name` - a class name; becomes the `__name__` attribute
`bases` - a tuple that itemizes the base class; becomes the `__bases__` attribute
`dict` - a dictionary which is the namespace containing definitions for the class body; becomes the `__dict__` attribute

### type return value

The `type()` function returns

type of the object, if only one object parameter is passed
a new type, if 3 parameters passed

The isinstance() function returns True if the specified object is of the specified type, otherwise False.

If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.

The issubclass() function checks if the class argument (first argument) is a subclass of classinfo class (second
argument).

The syntax of issubclass() is:

`issubclass(class, classinfo)`

## slots

The special attribute `__slots__` allows you to explicitly state which instance attributes you expect your object
instances to have, with the expected results:

- faster attribute access.
- space savings in memory.

The space savings is from Storing value references in slots instead of __dict__.

Denying `__dict__` and `__weakref__` creation if parent classes deny them and you declare `__slots__`.
Quick Caveats

```python
class Base:
    __slots__ = 'foo', 'bar'

class Right(Base):
    __slots__ = 'baz', 
```
