Title: Antigravity
Date: 2025-11-24
Category: Tech
Lang: en
Tags: google, ai, gemini
Summary: First impressions about Antigravity, the new agentic IDE from Google

## What is it?

Not a sequel of the (good) movie [Gravity](https://www.imdb.com/title/tt1454468/), but yet another piece of AI software from Google. Contrary to Microsoft which pushes Copilot everywhere in its applications, Google prefers to release another app every couple of months and confuse its users.

I don't mind, I love to test that kind of free stuff!

## Install

It's fairly easy on Linux: add the new repo in apt sources and here you go ([details here](https://antigravity.google/download/linux)).

*Note: I'm surprised they didn't go for the `curl` approach like Warp and uv, but let's not discuss the hypest and most insecure ways to install applications on Linux systems.*

On Windows it's simpler, as usual. Download the .exe, run the installer, check/uncheck a few options.

After launching it the first time, you have to answer a couple of questions on preferences and foreseen usage, login with your google account (yes it's mandatory) and you're good to go.

{% img {static}/images/antigravity-setup.png 800 "Setup screen" %}

## First look

Disappointing. If you choose to open a folder, it looks like a fresh VS Code install without all my customizations. But that means it's  actually cleaner 😬. 

Very classical layout too: a browser explorer, an editor view, and of course the AI panel, where you can interact in Agent mode.

What's obvious is that it's made to test **Gemini 3**. It's selected by default. The timing is good, it has just been released 😉!

So far it smells like Google acquired Windsurf (which was a VS Code fork), rebranded it and released it with another Google logo.

## The Twist

The twist comes later, once you start exploring a few unusual options in the Antigravity UI.

* First: the Agent Manager. There is a small icon in the top bar or you can use `Ctrl-E` that will open the Agent Manager. In the Agent Manager, you can start agents on tasks like research, or background tasks and you can monitor the progress of these agents in the Inbox, check the changes in the editor view, and finally review their work when they're done. This view looks a bit like the chat version of GitHub Copilot and I like its syntax highlights and colors.

{% img {static}/images/antigravity-agent-manager.png 800 "Agent Manager" %}

* The Inbox is like your notification center in Warp, but the UI is simpler and easier to grasp.
In the left pane of the Agent Manager, you also see your workspace, i.e. the projects you run the agents onto, and that simple panel is very handy.

* Agents will produce "artifacts": its the output of their work. It can be an implementation plan, a summary of the changes... Nice thing is that you can comment on these "artifacts". I see it as a sort of code review, or agent tasks review. You can select content within artifacts and leave a comment for the agent and ask the agent to process it after submitting.

* You can decide if you want to follow or not the agent's work, thanks to the small "Following" button/badge on top of the Agent Manager. This is quite handy when you realize Gemini 3 takes its time.

## The Bad

I had a couple of issues. Gemini 3 got stuck several times and the only solution I had was to kill the application and relaunch it. Antigravity was eating all my precious RAM and the fan started to blow hard: I killed it.

I think Gemini didn't react well in some situations where the tools were not installed.

## Conclusion

I find Antigravity a very interesting product. I'm a big fan of Warp and its terminal integration, but I like the overview Antigravity provides on the agents tasks and the fact that you can comment on the "artifacts" produced by the agents. The user experience is rich, even a little too rich! I have the feeling I touched only 5% of the capabilities of the tool.

With regards to Gemini 3, I'm not really convinced. I think its output is good, but it crashed/failed too often during my sessions.
