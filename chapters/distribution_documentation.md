<!-- TOC -->
* [Distribution and documentation](#distribution-and-documentation)
  * [distutils, setup.py](#distutils-setuppy)
  * [code publishing](#code-publishing)
  * [Documentation autogeneration, sphinx, pydoc, etc](#documentation-autogeneration-sphinx-pydoc-etc)
<!-- TOC -->

# Distribution and documentation

## distutils, setup.py

`distutils` is deprecated with removal planned for Python 3.12. See the What’s New entry for more information.

Most Python users will not want to use this module directly, but instead use the cross-version tools maintained by the
Python Packaging Authority. In particular, `setuptools` is an enhanced alternative to distutils that provides:

- support for declaring project dependencies

- additional mechanisms for configuring which files to include in source releases (including plugins for integration
  with version control systems)

- the ability to declare project “entry points”, which can be used as the basis for application plugin systems

- the ability to automatically generate Windows command line executables at installation time rather than needing to
  prebuild them

`Setuptools` is a fully-featured, actively-maintained, and stable library designed to facilitate packaging Python
projects.

For basic use of setuptools, you will need a `pyproject.toml` with the exact following info, which declares you want to
use setuptools to package your project:

```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
```

Then, you will need a setup.cfg or setup.py to specify your package information, such as metadata, contents,
dependencies, etc. Here we demonstrate the minimum

```python
from setuptools import setup

setup(
    name='mypackage',
    version='0.0.1',
    packages=['mypackage'],
    install_requires=[
        'requests',
        'importlib; python_version == "2.6"',
    ],
)
```

```sh
~/mypackage/
    pyproject.toml
    setup.cfg # or setup.py
    mypackage/__init__.py
```

```
python -m build
```

## code publishing

https://packaging.python.org/en/latest/tutorials/packaging-projects/

```sh
packaging_tutorial/
├── LICENSE
├── pyproject.toml
├── README.md
├── setup.cfg
├── src/
│   └── example_package/
│       ├── __init__.py
│       └── example.py
└── tests/
```

## Documentation autogeneration, sphinx, pydoc, etc

- `autosummary`, an extension for the Sphinx documentation tool.
- `autodoc`, a Sphinx-based processor that processes/allows reST doc strings.
- `pdoc`, a simple Python 3 command line tool and library to auto-generate API documentation for Python modules. Supports
Numpydoc / Google-style docstrings, doctests, reST directives, PEP 484 type annotations, custom templates ...
- `pdoc3`, a fork of pdoc for Python 3 with support for Numpydoc / Google-style docstrings, doctests, LaTeX math, reST
directives, PEP 484 type annotations, custom templates ...
- `PyDoc`, a documentation browser (in HTML) and/or an off-line reference manual. Also in the standard library as pydoc.
- `pydoctor`, a replacement for now inactive Epydoc, born for the needs of Twisted project.
- `Doxygen` can create documentation in various formats (HTML, LaTeX, PDF, ...) and you can include formulas in your
documentation (great for technical/mathematical software). Together with Graphviz, it can create diagrams of your code (
inheritance diagram, call graph, ...). Another benefit is that it handles not only Python, but also several other
programming languages like C, C++, Java, etc.
