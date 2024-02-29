Title: Playing locally with AI models
Date: 2024-02-29 22:00
Category: Tech
Tags: AI
Lang: en

Unless you live under a rock, you've heard about the AI buzz the last 2 years. Since [ChatGPT](https://chat.openai.com/) has entered the game, it has become more concrete for regular people how powerful the generative AI models are.

Every week (if not everyday) there are announcements about a new model released by either Google, OpenAI or Mistral...

So after reading quite a bit about it, I wanted to go over the hype and try the different models locally. I discovered [LM Studio](https://lmstudio.ai/) and it blew my mind. I thought you had to do lots of complicated things to try out the models, like set up advanced integration in GCP or Azure... and in fact no.

LM Studio has a neat interface where you can:

* download different models (Genma, Phi 2, you name it)
* start a web server using one of them
* query the model with a prompt UI

all this **locally** on your machine!

{% img {static}/images/lmstudio.png 600 "Screenshot of LM Studio" "" %}

When it starts a local server, it load the model selected and then you can query it with curl or any REST client.

I used the [REST Client extension for VS code](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) and it works perfectly.

**Note**: if you encounter problems accessing `localhost` from the WSL Ubuntu:

Check this [link](https://learn.microsoft.com/en-us/windows/wsl/networking#accessing-windows-networking-apps-from-linux-host-ip). It comes down to running the following command to know what `localhost` really is for the WSL:

    ip route show | grep -i default | awk '{ print $3}'

Replace `localhost` by the IP the command returned in your REST (or .http) file and you're set.

Happy testing!
