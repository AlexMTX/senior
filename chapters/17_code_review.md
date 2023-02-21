* [^ Contents](../README.md)

<!-- TOC -->
* [Code Review Process](#code-review-process)
  * [Explains Pros and Cons of Pre- and Post-commit Code Reviews](#explains-pros-and-cons-of-pre--and-post-commit-code-reviews)
<!-- TOC -->

# Code Review Process

What to know:

* Code Review Best Practices (aims, feedback, reporting, periodicity, reviewers hierarchy)
* Performs code review for "Merge/Pull requests" in GitLab
* Performs code review with Atlassian Crucible
* Gerrit  (online code
  review) https://gerrit-documentation.storage.googleapis.com/Documentation/3.5.1/intro-how-gerrit-works.html

Gerrit is a Git server that provides access control for the hosted Git repositories and a web front-end for doing code
review. Code review is a core functionality of Gerrit, but still it is optional and teams can decide to work without
code review.

## Explains Pros and Cons of Pre- and Post-commit Code Reviews

In this regard, there are two types of code review: pre-commit and post-commit. Pre- and post-commit review concepts are
quite self-explanatory: pre-commit is a type of review when the code is reviewed before it goes to the main repository
of the version control system. Post-commit review takes place after the code has been submitted to the public
repository.

Have a look at some of the advantages and disadvantages of these two review types before deciding which one to adopt.
Pros of pre-commit:

- Company's coding quality standards are met before the work is committed to the main repository
  This scenario helps to make sure the review has been performed, not postponed or omitted
- Pre-commit reviews ensure other developers in your team won't be affected by bugs that may be found during a review

Cons of pre-commit:

- Decreases productivity of each developer, since further work on the submitted code is impossible until a successful
  review, and takes even longer if multiple reviewers are involved
- After successfully passing a review, the developer could commit a different piece of code , by mistake or otherwise

Pros of post-commit:

- A developer can work and commit changes to the repository continuously
- Other team members see the code changes and can alter their work accordingly
- Some changes can be complex and require multiple steps, so it's convenient to examine each step separately after all
  of them have been committed

Cons of post-commit:

- Increased chances of poor code making it into the main repository, hence affecting the entire team's work
- When defects are found, it may take a while for the developer to switch back to the module they had been working on
