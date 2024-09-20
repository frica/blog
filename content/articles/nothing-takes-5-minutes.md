Title: Nothing ever takes 5 minutes
Date: 2024-09-20 21:00
Category: Tech
Tags: engineering, software, github
Lang: en
Summary: Nothing takes 5 minutes in software engineering. Nothing. Even the simplest things. But why do you still believe you could do it? And why does it consistently fail?

Yesterday I was reworking a test suite when I noticed that the test runner in GitHub was giving a warning:

    :::
    Node.js 16 actions are deprecated. Please update the following actions to use 
    Node.js 20: my_action [...]

I saw it in the past weeks but nobody else in the team ever mentioned it, so I forgot.

But I had an insomnia and my brain was thinking about technical debt in my state of semi-consciousness. I woke up at 6 AM today thinking: I WILL FIX THAT WARNING.

That was **my mission**.

Went to the office, opened my IDE, opened the test yml file of the Python project. AH, an action with a `@v1` version! I probably just need to update to the latest version! Victory, it will be fixed before 9:30!

OK, it looks like an exotic action.

Let's look at the action repository...

Not maintained and **archived**. OK.

BUT look, there are instructions from the former maintainer to use another action `setup-python` and he even provides a proper link! Neat, thanks.

Spend 10 minutes in the (thorough) help page of `setup-python` to be sure I understand the difference between the action currently in use and the new recommended action.

I make the changes (removed 2 lines, add one). Commit and push, create a PR to run the test workflow. Yay, almost ready!

Workflow failure. Tests don't even start. Can't find the requirements.txt.

Spend another 5 minutes reading more carefully in the help page. OK, my requirement.txt is not exactly called like this so I should specify with an extra parameter the exact name of the requirement file. No problem.

Commit and push. Failure.

Sudden Teams message: "Could you please join a call, we need your opinion". Sigh. OK.

30 minutes later, back at the failure.

I realize that probably it's a good idea to **first checkout the source code** before looking for the requirements file. Ahah, dumb me! That's OK, I had a bad night.

Now it will work, I'm sure.

But hey, my senior colleague who wrote the test.yml years ago will review it: I must prove to him that I didn't degrade performance of the workflow...

Let's rerun it 5 times to check the timings.

OK it looks even a bit faster! Nice, it will be a piece of ca-

Email. Comment on the PR from the senior guy. I cached the dependencies from the wrong requirements file (yes there are several, for development, testing and production, I don't know yet why).

He's right, damn it. Another stupid error.

Alright, easy fix.

Commit, push. Rerun 5 times to check the timings.

Looks good now. And my colleagues approved the PR in the meantime.

But... what is this? I can still see a warning message still in the test workflow summary?

Another action later in the workflow seems to trigger the same Node.js deprecation warning.
At that stage I'm not too sure anymore. Will I be done before lunch?

I check the guilty action: a pytest wrapper around `test-summary`, called `pytest-summary`. I check `test-summary`, hooray they fix the warning some months ago! And the `pytest-summary` maintainer even updated this fix! 

But no recent releases of `pytest-summary`, so I can't just upgrade the version.

Hmmm. I decide to reach to the maintainer and humbly ask for a release of his code, that could be used then in my workflow, figure out quickly thanks to StackOverflow that I can use `pytest-summary@main` to bluntly use the code from the main branch.

Update the PR, justifying that choice for my colleague. Land the PR because fuck that, it's better anyway.

Go to lunch.

Speed up after lunch to a meeting where I play half PO, half Scrum master, make a mistake copying a requirement, encounter issues with Teams on Ubuntu Linux (thanks MS for not updating Teams to Wayland + Firefox)... Half of my brain is still thinking about my "quick PR" of the morning. The other half wants to sleep.

Exit the excruciating meeting. A reply from the maintainer of `pytest-summary` saying he made the release! The power of open source software!

Two commits later (typos, typos everywhere), I have a new PR settings the version straight.
I quickly call my colleague reviewer, explain him. But he's busy, he says he will approve next week my (3 characters) change.

It's 16:30. I thank the maintainer, tell him his latest release is working fine.

I sigh, considering my day finished, and looking at my todo list with my 2 main items not touched.

_It was just 5 minutes work._

---