Title: Adding a Playwright MCP server to Warp
Date: 2025-07-02 20:38
Category: Tech
Lang: en
Tags: warp, mcp-server, tips
Summary: How to add a Playwright MCP server to Warp

I'm spending quite some time experimenting with [**Warp**](https://www.warp.dev/) since I bought myself a Pro Plan. This agentic coding terminal is so fun and powerful, I couldn't resist.

Right now I'm testing some of the more advanced functionalities and playing with MCP servers. [A recent and very interesting talk by Armin Ronacher](https://youtu.be/nfOVgz_omlU?si=yWDF5EZNjKGl8E1T) called "Agentic Coding: The Future of Software Development with Agents", triggered me to configure in Warp the [Playwright MCP server](https://github.com/microsoft/playwright-mcp) (officially supported by MS, no less!), which provides setup explanations for Claude Code and VSCode but not Warp.

It's not that complicated to install. Here are the steps:

* Ctrl-Shift-P and type "MCP"
* Pick the "Open MCP Servers"
* Press the "Add" button
* Paste the following code:

        :::json
        {
            "mcp-server-playwright": {
                "command": "npx",
                "args": [
                "@playwright/mcp@latest"
                ],
                "env": {},
                "working_directory": null,
                "start_on_launch": true
            }
        }

Thanks to `npx`, you don't need to install anything locally (as long as you have Node.js on your system).

It will now start automatically, and you can see in the UI the methods that Warp will be able to use:

{% img {static}/images/playwright-mcp-warp.png 600 "Methods exposed by the Playwright MCP server in Warp UI" %}

**Note:** I do think the copy/paste feature is _severely broken_ on Linux, which has made me rage a few times, but on Windows it seems... fine?

Anyway, this is a great tool. I showed it to my boss and he loved it.
Next week I will give a demo to a selected audience!
