Title: Bisect Animations
Date: 2026-02-02
Category: Tech
Lang: en
Tags: git, bisect
Summary: Animation to illustrate git-bisect

The [git-bisect](https://git-scm.com/docs/git-bisect) tool available in `git` can perform a binary search and find which commit in your project’s history introduced a bug.

At work, I had to redesign a binary search web tool. To understand better the behavior of the algorithm, I decided to create an animated timeline to follow step by step the search.

Anyway, here is the typical use case when you're looking for a commit that broke a feature:

<iframe src="{static}/images/bisect-usecase1.html" width="100%" height="800px" style="border:none;"></iframe>

But there is a second use case, which I've learned is also sometimes used in my project: "something starts to work and we don't know why" 😁 In this case, we want to know which commit had the side-effect of fixing another vaguely related feature:

<iframe src="{static}/images/bisect-usecase2.html" width="100%" height="800px" style="border:none;"></iframe>

It's actually amazing what you can do with **HTML**, **CSS**, and a LLM like Sonnet 4.5. I find this sort of small animation a great addition to illustrate requirements and the sequence of events.

Hope this helps!
