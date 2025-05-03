Title: Vibe coding, is it for real?
Date: 2025-05-03 12:00
Category: Tech
Tags: vibe-coding, coding-agents, AI
Lang: en
Summary: My view on vibe coding, based on a real life example

## The challenge

At work we have a timesheet management web application. Entirely internal, buggy for years, and with the usability of a badly designed SAP UI. Of course, my fellow C++ colleagues have coded an application to circumvent the limitations of the web UI and communicate with the time management application.

### Problem #1

It's written in C++, and it uses the Qt framework. I know close to nothing now about C++ (last time I wrote something with it was around 2004-2005) and really nothing about Qt (and I don't have time to learn it).

### Problem #2

The way to communicate with the time management backend is extremely hacky: there is no REST API. The C++ code to create, update and delete events or tasks is the results of countless hours of reverse-engineering the web application.

### Goal

So, my goal was to convert this C++ application into a web UI **or** a **Python** equivalent CLI tool, using the various agents I have at my disposal, namely Copilot, ChatGPT and Warp. The end user would be primarily me, but if I could offer something useful to my colleagues, why not?

All this with a minimum investment in learning and coding. That's why I considered *vibe coding*: is the promise real? Can I implement an application "automatically", just by giving instructions to a coding LLM?

## Attempt 1

<div class="summary">
Goal: Build a web interface
<br>
Tool: PyCharm
<br>
LLM: GPT-4o
<br>
Workflow: Vibe coding
</div>

### Observations on ChatGPT

* The LLM gave good recommendation about components to use.

* The initial scaffolding was good.

* Design was pretty bad. Without direction, it didn't look pretty. When I asked to make it prettier it proposed some questionable choices.

* It forgot some previous instructions and lost pieces of the design after some iterations, which was pretty annoying.

I stopped after 1h: I don't know enough about javascript to check properly the code. Also designing web applications is a job and I didn't really know how the web application should look like.

## Attempt 2

<div class="summary">
Goal: Build a Python CLI
<br>
Tool: Warp Terminal
<br>
LLM: o1
<br>
Workflow: Vibe coding
</div>

### Observations on Warp and o1

* I gave the general context and asked for a conversion.

* The LLM made several assumptions.

* It delivered a local configuration mechanism while not asked.

* It built a nice CLI but failed completely to deliver the communication interface, assuming it was a standard REST API.

* I got stuck in a loop after 45 min, noticing it didn't properly modify the code after each pass.

* When there were too many issues, it seems it couldn't handle it.

* It restarted from scratch several times (good) without success (bad).

* Not having an IDE on the side to double-check is a bad idea.

For me it was mesmerizing (and a bit magical, to be honest) to see the sequence of steps done automatically and the thinking of the agent.
But I gave up because first I got out of credits in Warp (I use the free tier) and secondly, I was a bit frustrated that it needed so many rounds to fix small things like duplicated code.

## Attempt 3

<div class="summary">
Goal: Build a Python CLI
<br>
Tool: VS Code
<br>
LLM: Gemini 2.5 (preview)
<br>
Workflow: Chat with AI agent
</div>

### Observations on Gemini 2.5

* I focused primarily on the communication interface. I asked first to analyze the existing C++ code and what it does. **I saved the output.**

* Then *method per method*, I asked for a conversion from C++ to Python.

* I asked early on to create test code, either in the main method or in dedicated test files, so I could double-check after each couple of iterations.

* The responses were precise and successfully handled the conversion of complex C++ code.

* It used the right Python packages, the ones I would have chosen.

* At the end the module works and could communicate properly with the other system.

* There was much more typing involved for me, much more direction given.

* Ended up with a working piece of code.

## Last steps

After this success I decided to connect the two modules together.

<div class="summary">
Goal: Connect the CLI to the communication module
<br>
Tool: PyCharm
<br>
LLM: Gemini 2.5 (preview)
<br>
Workflow: Chat with AI agent
</div>

* I renamed the module, changed all occurrences with a good old "Replace" and created a proper local git repository.

* I worked on the details (credentials storage, data model extension), often manually. It was tedious work.

After a couple of hours, the project was clean and I could create an event in the remote application with my CLI, and have a "decent" code quality level, that I could push to a new GitHub repository.

## Conclusions

As we start seeing [books on vibe coding](https://simonwillison.net/2025/May/1/not-vibe-coding/) and have endless debates on whether or not vibe coding / coding with agents is useful, if it's good for production code or only hobby projects, my point of view is the following.

**Vibe coding as a non-software person is impossible for real world challenges.**

You need to be able to assess the output of the LLM, even if you don't know the language. You need to have the habits of breaking down the logical structure into incremental steps. You need to have an idea about software quality.

It is very easy to forget all these things even for software developers, because the agents "look" smart.

**I am not drawing any conclusion on any tools or LLMs**. I adapted my workflow in every iteration until I found one that worked **for me**. I can't say if Gemini 2.5 is better than o1, for example.

The progress made since I started looking into coding LLMs is incredible (and scary). I'm also convinced they will continue to improve.

So, to conclude:

* Can you achieve something without knowing how to code? **No**, at least not based in my experience.

* Can you speed up your development? **Yes, tremendously**. I would never have started this on my own, due to my lack of time.

* Does it lower the barrier for rusty/average programmers? **Yes**, I admit without shame that I'm in this category, and it helps a lot.

* Does it lower the barrier / learning investment if you don't master a language or a tech? **Yes**, but you need to be literate with software development.

All in all it was a very useful experience: I now know better how to use these tools!
