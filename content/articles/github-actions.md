Title: Deploying my Pelican blog with Github actions
Date: 2024-03-13 22:19
Category: Tech
Tags: pelican, github
Lang: en

The Pelican documentation is awesome, if you read it carefully. The **Tips** section contains information about [how to deploy with Github Actions](https://docs.getpelican.com/en/latest/tips.html#publishing-to-github-pages-using-a-custom-github-actions-workflow).

Sounds cool, but what is it exactly?

GitHub introduced GitHub Actions in 2019, and it's a workflow automation tool that allows GitHub users to build their Continuous Delivery pipelines. Basically a workflow pipeline à la Jenkins/GitLab. Soit.

After reading what it was I decided to give it a try to see if I can automate the deployment of my humble blog and spare a few manual steps.

The github actions files are stored in a directory `.github/workflows`. It's a yaml file defining the different steps of your workflow with a declarative syntax.

Mine looks like this:

    :::yaml
    name: Deploy to GitHub Pages
    on:
        push:
            branches: ["master"]
        workflow_dispatch:
    jobs:
        deploy:
            uses: "getpelican/pelican/.github/workflows/github_pages.yml@master"
            permissions:
                contents: "read"
                pages: "write"
                id-token: "write"
            with:
                settings: "publishconf.py"
                requirements: "pelican[markdown] pelican-liquid-tags"

Normally you would need to tell Github to pick an Ubuntu image, install python, pip and Pelican, checkout your Pelican blog files, run the pelican command and deploy to your Github Pages...

The amazing thing is that the Pelican team already provides a workflow that does all the work for you! You can see it in the line `uses:`

So I pushed the yaml file to my `master` repo, and now every time I push new files in my master branch (the one containing the .md files and the pelican settings), the workflow is triggered and after a couple of minutes, I see the new version of my blog online.

If I ever want to see live the action being triggered, I need to go to the Actions tab in my repo (https://github.com/<username>/<repository>/actions) and there I can see a Deploy to GitHub Pages action running, with the commit message I entered when I committed the .md files changes.

Pretty cool & simple!
