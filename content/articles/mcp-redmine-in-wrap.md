Title: Adding a Redmine MCP server to Warp
Date: 2025-07-02 20:38
Status: draft
Category: Tech
Lang: en
Tags: warp, mcp-server, tips
Summary: How to add a Redmine MCP server to Warp

Following my previous article [Adding a Playwright MCP server to Warp]({filename}/articles/playwright-in-warp.md), here is another MCP server I find useful. Not a lot of people are still using Redmine I guess, but honestly it works, so several made a MCP for it. I chose this [one](https://github.com/yonaka15/mcp-server-redmine), based on recent activity and downloads.

Here are the steps to set this up.

**Note**: I didn't set it up with npx.

* Clone the [repo](https://github.com/yonaka15/mcp-server-redmine)
* Create an local .env in the directory where you installed the tool and fill the `REDMINE_API_KEY` and `REDMINE_HOST` values in there.
* Open Warp
* Ctrl-Shift-P and type "MCP"
* Pick the "Open MCP Servers"
* Press the "Add" button
* Paste the following code:

        :::json
        {
        "mcp-server-redmine": {
            "command": "node",
            "args": [
            "<dir where you installed>/dist/index.js"
            ],
            "env": {
            "REDMINE_API_KEY": "",
            "REDMINE_HOST": ""
            },
            "working_directory": null
          }
        }

The MCP server will start automatically and you can now retrieve a Redmine bug report from Warp and  ask the agent to fix the bug in one prompt 😁
