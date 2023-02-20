<!-- TOC -->
* [Unit and API Testing or White box](#unit-and-api-testing-or-white-box)
  * [Test coverage. Understand how to treat this metric](#test-coverage-understand-how-to-treat-this-metric)
  * [TDD and BDD approaches, Implements TDD and BDD from scratch](#tdd-and-bdd-approaches-implements-tdd-and-bdd-from-scratch)
  * [Mutation testing, tools](#mutation-testing-tools)
<!-- TOC -->

# Unit and API Testing or White box

## Test coverage. Understand how to treat this metric

- Finding the area of a requirement not implemented by a set of test cases
- Helps to create additional test cases to increase coverage
- Identifying a quantitative measure of test coverage, which is an indirect method for quality check
- Identifying meaningless test cases that do not increase coverage

To calculate test coverage, you need to follow the below-given steps:

Step 1) The total lines of code in the piece of software quality you are testing

Step 2) The number of lines of code all test cases currently execute

Do realize, though, that getting 100% coverage is not always possible. There could be platform-specific code that simply
will not execute for you, errors in the output, etc. You can use your judgement as to what should and should not be
covered, but being conservative and assuming something should be covered is generally a good rule to follow.

Types of coverage: line, method, class

## TDD and BDD approaches, Implements TDD and BDD from scratch

Test-driven development (TDD) is a software development process relying on software requirements being converted to test
cases before software is fully developed, and tracking all software development by repeatedly testing the software
against all test cases. This is as opposed to software being developed first and test cases created later.

Behavior-driven development (or BDD) is an agile software development technique that encourages collaboration between
developers, QA and non-technical or business participants in a software project.

behave uses tests written in a natural language style, backed up by Python code.

```yaml
# -- FILE: features/example.feature
Feature: Showing off behave

  Scenario: Run a simple test
    Given we have behave installed
     When we implement 5 tests
     Then behave will test them for us!
```

https://github.com/behave/behave

## Mutation testing, tools

Mutation testing, also known as code mutation testing, is a form of white box testing in which testers change specific
components of an application's source code to ensure a software test suite will be able to detect the changes. Changes
introduced to the software are intended to cause errors in the program. Mutation testing is directed to ensure the
quality of a software testing suite, not the applications the suite will go on to test.

`pip install mutmut`
