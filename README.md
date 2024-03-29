## Coding-with-AI
My journey on exploring the possibilities of coding with a locally hosted AI

### Abstract
A short exploration of 2 weeks was conducted to evaluate and report the feasibility of leveraging local versions of large language models to develop applications as a software engineering team would do in a business context. Open source software was leveraged to convert natural language into a python codebase for the purpose of building a simplistic carbon accounting tool to identify the carbon footprint caused by assets registered in a configuration management database. During the exploration, a grossly limited version has been 'developed' as Proof of Feasibility. Building an application is found to be feasible although it does take time and requires innevitable sacrifices on security. Context is currently the biggest bottleneck and requires a spoon feeding approach to be productive. During the coarse of the exploration, conviction was developed that this bottleneck will disappear in due time. 

### Introduction
My name is Wynand Huizinga, I work at Accenture's custom engineering entity (Liquid Studio & Sustainability) in NL where I've been granted some time in between projects to adopt knowledge in AI. I have a background in product design and frequently fulfilled a role as product owner/manager. In that role, the goal is always to have a low total cost of ownership (TCO). Converting 'user stories' into code with a partly automated team is hence an interesting topic. Working with online gen-ai tools is already a inconceivable, but does come with consequences and added risk. I already worked on my local machine (offline) with latent stable diffusion (image generation) for more than a year. New to me was the feasibility of running language models (GPT's) locally. Below my journey on exploring the possibilities of gen-ai in relation to programming using a large language model: To what extend, can AI replace development capabilities? 

### Gen-AI in short 
You provide context (a prompt), in return you get 'completion' of your context. This works with Q&A, but also for regular conversations. Depending on the sophistication-level of your model, you can expect more sophisticated response. Telling a complex model about 'having had a good night rest' leads to a complex response telling you about the importance of quality sleep and how that raises productivity during the day. A simple model would merely respond with "good for you". The race for the most sophisticated models has begun, and all the bigger enterprises are in it.

Their models however, may have downsides for 'us' consumers:
- May cost money to use
- May be censored
- Whatever context you provide, is handed over to the supplier of the model. 

> "Imagine sending code snippets which give away authentication methodologies used in your ecosystem." ~ what is your workforce actually supplying to third parties (i.e. openai/chatgpt, github/co-pilot, ...)? are you even monitoring that?

Now especially for the latter reason, I conducted a study on running open source language models on your local machine. And more particularly, can I with close to 0 knowledge make an application by giving it textual functional requirements and prompt engineer it so that it returns code to me?

### Subject
Given our planetary challenges with regards to maintaining our planet, for this project I chose the topic of carbon accounting. It's not new or innovative, but it's certainly not getting enough attention. At Accenture where I currently work, we provide clients with insights on their carbon footprints caused by owning/leasing equipment (i.e. Laptops, phones, network switches, routers, access points, monitors, etc.). Suppliers of such equipment usually provide tech doc which ideally includes product lifecycle emissions. They usually also provide lifetime expectations, hence you have some metrics to base your own cause for annual emissions. When having those numbers, it's interesting to see if you can somehow stimulate yourself to compensate or sequester those emissions. 
 
> "For language model I experimented with a few, but ultimately found a leaderboard and went for LosslessMegaCoder."

### The journey
After a few open source initiatives, I ended up with codebooga and silly tavern as a shell on top of it. Although silly tavern is actually a Waifu / RPG platform, I foresaw potential to mimic a software engineering team. Most platforms allow to provide a character to your assistant. A character essentially enriches content of your own prompt. Silly tavern enables you to have more than 1 character in a chat room. That implies you can create characters for all the roles in your software team (Architect, Backend developer, Scrum master, UX designers, business analyst, security architects, testers, etc.). The theory being: provide context of for example my carbon accounting application: Let them figure out how to make a solution. That might come in handy during my study.

I initially assembled a team, which I asked to come with a solution for my product. As expected, my architect started drafting a data model, and various microservice definitions. That was for me already the first learning experience: "how would you distribute subcomponents into an architecture?" It started with services for: user, assets, calculation & reporting. It even got accompanied by some definitions for an MVP with critical use cases. 

[![Image1](https://github.com/wynandhuizinga/Screenshots/blob/main/thumbs/01%20Arch%20services.JPG)](https://github.com/wynandhuizinga/Screenshots/blob/main/01%20Arch%20services.JPG)

Swiftly enough I got supplied with instructions on how to setup project bones, as well as extensions on first API Endpoints and instructions on how to run my application. And upon trying, it at first even seemed to work. 

[![Image2](https://github.com/wynandhuizinga/Screenshots/blob/main/thumbs/02%20First%20code.JPG)](https://github.com/wynandhuizinga/Screenshots/blob/main/02%20First%20code.JPG)

Soon enough, I found out that authentication did not really authenticate me, or at least... it didn't remember for very long that I was authenticated. Either way, I learned that authentication either ways is not very valuable: it relied on outdated technology. My fresh python installation did not allow me to run specific encryption methods (SH256) anymore as it was beyond deprecation. No problem, let me proceed without encryption & login. Specifics are not in scope of my goal anyway. 

After quite a bit of fiddling around, I picked up a lot of learnings. Every time I ask for a code snippet, if  it wouldn't run, I would simply paste the issue in chat, and in response I'd get an answer which actually tought me more about the details of python. For 95% of the time, this local language model is enough to solve issues, in rare occasions I had to google / stackoverflow something. I in the meanwhile also learned about various ways in which you can set up a repository, data models, build data bases, invoke API endpoints and insert data into your database, etc. 

I also learned how to 'break down' complex work to simpler questions, and extend it to more complexion later on. Although I wanted as much as possible to only copy paste code blocks, it sometimes felt very hard to persist on high complexity levels. Certainly this will improve in due time. The AI hype started only a few months back really. 

I ultimately managed to get a DB and back-end 'engine' up and running. It would take a API endpoints to insert my assets, import reference assets, and compare the 2 for matches, and then look up the reference assets tech specs for a global warming potential. Although far from supportive towards my use cases, slow in performance, it's surely good enough to build on to meet my goals. 

[![Image3](https://github.com/wynandhuizinga/Screenshots/blob/main/thumbs/03%20Proof%20of%20endpoints.JPG)](https://github.com/wynandhuizinga/Screenshots/blob/main/03%20Proof%20of%20endpoints.JPG)

What I was still missing at this moment was a front-end. I expected this to be fairly easy, however, what I underestimated was the amount of lines of code involved in front-end. The more lines of code, the more context you're adding, and the clumsier your model can get in its interaction & responses

[![Image4](https://github.com/wynandhuizinga/Screenshots/blob/main/thumbs/04%20Creation%20of%20front-end.JPG)](https://github.com/wynandhuizinga/Screenshots/blob/main/04%20Creation%20of%20front-end.JPG)

After a while of wiggling around about styling, I managed to get a simple page with 2 buttons. Again, goal is to figure out if it 'can' work. End result is far from 'pretty', but it does work (provided you use a creative way to with curl commands to fill the database). Can we insert data through front-end? I'm 100% convinced of that, but it would be helpful if the model was just a little bit smarter. The learning curve + the results so far took about 2 weeks. 

| [![Image5](https://github.com/wynandhuizinga/Screenshots/blob/main/thumbs/06a%20-%20startscreen.JPG)](https://github.com/wynandhuizinga/Screenshots/blob/main/06a%20-%20startscreen.JPG) | [![Image6](https://github.com/wynandhuizinga/Screenshots/blob/main/thumbs/06b%20-%20device%20overview.JPG)](https://github.com/wynandhuizinga/Screenshots/blob/main/06b%20-%20device%20overview.JPG) | [![Image7](https://github.com/wynandhuizinga/Screenshots/blob/main/thumbs/06c%20-%20calculation%20outcome.JPG)](https://github.com/wynandhuizinga/Screenshots/blob/main/06c%20-%20calculation%20outcome.JPG) |

### Findings
- At this moment, you have to be patient: feed small blocks of context. Occasionally start a new chat, and provide minimum code snippets to let it expand on. 
- Forget about user authentication: I tried a couple of different approaches with a.o. JWT. It's very hard for 'new' software engineers to grasp the concepts of salt & pepper which makes it very challenging to test the work. For now: Leave this to the experts. 
- Consideration: level of security standards is at best the standards known at the time the model was made
- I'm 100% convinced that in a timespan probably sooner than later (2 years?) significant improvements will be made with regards to sophistication. 
- Having ai behave as a team does work, but only very shortly. Already after about 2 rounds of discussion, the message streams become too long, and it gets 'confused' / 'forgetful'. Concepts such as an architectural design need to be re-iterated for ai to work at this moment in time. I am convinced however that this 'challenge' will get resolved probably rather sooner than later. For now, you have to be safesome with 'wasting space' with unnecessary context. I let it work out a few unit-testing, it was quite verbose, but I'd certainly evaluate those. Furthermore I tried out test driven development (TDD), but I swiftly ran into context size issues. Same for user stories, Gherkin and Domain driven development. All these can help you break down the work though. 
- Often your model doesn't provide the 'right' answer, but you do have to copy paste code to try that. Especially when you need to change multiple blocks in multiple files, it's easy to loose track. For this reason it's super important to have a versioning system where you can easily commit and reset branches. 
- It took me a significant number of attempts to build the first 'working application' on which I had confidence that my first features would work. In my experience, it doesn't hurt to throw something away, or to re-insert the same prompt/context and let it provide an answer on a different seed. Every request takes a random number (seed), which leads to different response. Sometimes the prompt is fine, but the model simply fails. I observed that running the materials locally give you a significant advantage in terms of control over the conversation. Especially Silly Tavern is very good at regenerating messages and even branching off from previous quotes. 

### Conclusion
I'm having mixed feelings about this being impressive. On one hand, it's way off from enterprise software quality, not even close. I did however not know anything about python, and I did manage to draw out a basic web app with a very high confidence of being able to improve it to more acceptable standards. Certainly, I've been overwhelmed by the sheer power of what it can do for people with limited engineering skills. The technology is definitely here to stay. Hopefully by writing this guide, I managed to provide insights on the feasibility and accessibility of the technology. You're most welcome to reach out in case of questions. You are welcome to do so by mail / linkedin / phone.

### Trying out my end result
Assuming you're having GIT installed (and added to your environment variables)
In command prompt: 
```
git clone git@github.com:wynandhuizinga/Coding-with-AI.git
```
Once downloaded, browse to the newly created folder and open ["run scripts.txt"](https://github.com/wynandhuizinga/Coding-with-AI/blob/main/run%20scripts.txt)

### Getting started with AI yourself
For those inspired and interested in getting started:
Start by installing python, oobabooga, optionally silly tavern and git.
Get some sort of development environment: notepad++ or LiClipse
Hardware: NVIDIA graphics card - mine: 3060 TI 12gb, >32GB ram -> half of the modern gaming PC's suffice. 

| [![Image8](https://github.com/wynandhuizinga/Screenshots/blob/main/thumbs/08%20my%20settings%20for%20lossless.JPG)](https://github.com/wynandhuizinga/Screenshots/blob/main/08%20my%20settings%20for%20lossless.JPG) | [![Image9](https://github.com/wynandhuizinga/Screenshots/blob/main/thumbs/08%20my%20settings%20for%20lossless-model-loader.JPG)](https://github.com/wynandhuizinga/Screenshots/blob/main/08%20my%20settings%20for%20lossless-model-loader.JPG) |

My settings for loading a LLM as well as configuring an LLM. This can be a study on its own, my settings certainly weren't perfect. Sometimes my architect would start saying that I approved certain proposals which would then get followed up by an implementation by other 'characters'.

### A few more examples to visualize how it worked for me:
| [![Image10](https://github.com/wynandhuizinga/Screenshots/blob/main/thumbs/07%20-%20another%20impression%20of%20how%20a%20session%20with%20a%20team%20goes.JPG)](https://github.com/wynandhuizinga/Screenshots/blob/main/07%20-%20another%20impression%20of%20how%20a%20session%20with%20a%20team%20goes.JPG) | [![Image11](https://github.com/wynandhuizinga/Screenshots/blob/main/thumbs/07%20-%20bonus%20example%20of%20quering%20for%20simplistic%20hardcoded%20updates.JPG)](https://github.com/wynandhuizinga/Screenshots/blob/main/07%20-%20bonus%20example%20of%20quering%20for%20simplistic%20hardcoded%20updates.JPG) | [![Image12](https://github.com/wynandhuizinga/Screenshots/blob/main/thumbs/07%20-%20bonus%20providing%20detailed%20context.JPG)](https://github.com/wynandhuizinga/Screenshots/blob/main/07%20-%20bonus%20providing%20detailed%20context.JPG) | [![Image13](https://github.com/wynandhuizinga/Screenshots/blob/main/thumbs/07%20-%20bonus%20spoonfeed%20example.JPG)](https://github.com/wynandhuizinga/Screenshots/blob/main/07%20-%20bonus%20spoonfeed%20example.JPG) | [![Image14](https://github.com/wynandhuizinga/Screenshots/blob/main/thumbs/07%20-%20getting%20scolded%20by%20my%20virtual%20architect.JPG)](https://github.com/wynandhuizinga/Screenshots/blob/main/07%20-%20getting%20scolded%20by%20my%20virtual%20architect.JPG) |

### Acknolegdement
Special thanks to the good people contributing to projects in sources.

#### sources:
- https://github.com/oobabooga/text-generation-webui
- https://github.com/sillytavern
- https://github.com/Boavizta/environmental-footprint-data/tree/main
- https://huggingface.co/spaces/mike-ravkine/can-ai-code-results

#### Additional resources:
- https://git-scm.com/downloads/ 
- https://gitextensions.github.io/
- https://www.python.org/downloads/ 