Title: Interesting links - WK 18
Date: 2025-05-04 12:00
Category: Links
Tags: AI, vibe-coding, tools, open-graph, textual
Lang: en
Summary: Week 18

* [Free screen recorder](https://www.screenrecorder.me/): pretty unusual setup, you need to share your screen with a web application.

* [Falsehoods about user feedback](https://thoughtbot.com/blog/falsehoods-software-teams-believe-about-user-feedback#falsehoods-about-user-feedback): pretty funny!

> The list below may seem absurd at times, but rest assured that they are based on real life circumstances. The common thread is that people in the detail (software teams) communicate very carefully about their software, and lose sight of communication patterns in other spheres.

* ChatGPT 4o becomes [a little "too nice" (to stay polite) after last update](https://openai.com/index/sycophancy-in-gpt-4o/). That's why I can't trust these generative tools for real analysis. The update process is way too shady and impossible to control. Even the [OpenAI post-mortem](https://openai.com/index/expanding-on-sycophancy/) is not really reassuring:

> But we **believe** in aggregate, these changes weakened the influence of our primary reward signal, which had been holding sycophancy in check. User feedback in particular can **sometimes** favor more agreeable responses, likely amplifying the shift we saw. We have also **seen** that in **some cases**, user memory contributes to exacerbating the effects of sycophancy, although **we don’t have evidence** that it broadly increases it.

* A [Wikipedia hotspot](https://kiwix.org/en/kiwix-hotspot/). To spread knowledge and facts around you, when there's no Internet. A preppers package exists also: only problem is when the apocalypse comes, few people will have electricity (right, [Spain](https://www.bbc.com/news/articles/cd6jenl581vo)?). But ok. They sell the hardware AND the SD card with the data they downloaded from the Internet. Hmmm.

* [Jan](https://jan.ai/) is an open-source alternative to LMStudio. Tried it. Works. Will see it I ditch totally LMStudio in favor of it. I realize I do not use often LLMs locally.

{% img {static}/images/jan-ai.png 800 "Screenshot of Jan" "Screenshot of Jan" %}

* Simon Willison, who blogs non-stop about AI and its usages, is frustrated: there are books being released about vibe-coding, and they are missing an opportunity, [according to him](https://simonwillison.net/2025/May/1/not-vibe-coding/).

* A [simple CLI tool](https://gist.github.com/tkellogg/04c59a56f0a5b574447e58caa7ae7abb) for asking questions to qwen3, made by [Tim Kellog](https://timkellogg.me/blog/). He has it aliased to `qw`, so he  can do:

        :::bash
        qw "what time is it in Tokyo?"  
        cat stderr.log | qw "have you seen anything like this before?"

* [wrkflw](https://github.com/bahdotsh/wrkflw/releases/tag/v0.4.0) has released a version 0.4. Still not entirely convinced, but I'll follow the progress!

* A [Kickstarter](https://www.kickstarter.com/projects/driscollis/creating-tui-applications-with-textual-and-python/) for a book about the Python TUI library [Textual](https://www.textualize.io/). It seems a bit obsolete to learn a tech with a book nowadays, but if it avoids countless paying subscriptions on Substack, Medium... I might pay the 15$ 🤔

* Learned a bit about [Open Graph](https://ogp.me/) meta tags. I dislike a bit that it comes from FB but all my applications (Bluesky, Signal) support it today and the preview is nicer when you share a link. I modified the blog template to set them correctly, thanks to [this post from Liz Denys](https://lizdenys.com/journal/articles/adding-open-graph-to-pelican.html).
