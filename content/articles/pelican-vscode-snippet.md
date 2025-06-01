Title: VS Code snippet for Pelican
Date: 2025-06-01 17:25
Category: Tech
Lang: en
Tags: pelican, vscode
Summary: A snippet to insert a Pelican post header

A small trick to insert easily the header of a new post in a Pelican blog: use VS Code snippets!

Add this in a file `.vscode/new-pelican-note.code-snippets`:

    :::json
    {
        "New Pelican Note": {
            "scope": "markdown",
            "prefix": "pelican-note",
            "body": [
                "Title: $1",
                "Date: ${2:$CURRENT_YEAR-$CURRENT_MONTH-$CURRENT_DATE $CURRENT_HOUR:$CURRENT_MINUTE}",
                "Category: ${3:${TM_DIRECTORY/(.*[\\/])?([^\\/]+)$/${2:/capitalize}/}}",
                "Lang: fr | en",
                "Tags: ${4:tag1, tag2}",
                "Summary:",
                "",
                "$0"
            ],
            "description": "Create a new note for Pelican"
        }
    }

Every time you want to create a new post, just type Ctrl-Shift-P, "insert snippet", "pelican note".
