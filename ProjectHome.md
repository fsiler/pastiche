The pastiche software framework brings a variety of technologies together, like semantic web, multi-agent and distributed systems. It is designed for ease of use and fun.

![http://pastiche.info/images/pastiche_128.png](http://pastiche.info/images/pastiche_128.png)

This is a continuation of previous work done on [Spyse](http://sf.net/projects/spyse).

Still thinking about a number of [ideas](pastiche.md).

```
#!/usr/bin/env python

"""Hello World example program from the Spyse tutorial"""

from spyse.core.agents.agent import Agent
from spyse.core.behaviours.behaviours import Behaviour
from spyse.app.app import App

# Define a custom behaviour class
class HelloBehaviour(Behaviour):
    # Customize the Behaviour class by overriding action()
    def action(self):
        # The action:
        print "Hello, world"
        # Mark this behaviour as finished so that it will be removed
        # from the agent's behaviour list.
        self.set_done()

# Define a custom agent class
class HelloAgent(Agent):
    # Customize the Agent class by overriding setup()
    def setup(self):
        # Add the custom behaviour for the agent to perform.
        # An agent will die as soon as all its behaviours are complete.
        self.add_behaviour(HelloBehaviour())

# Define a custom application class
class MyApp(App):
    # Customize it by overriding run()
    def run(self, args):
        self.start_agent(HelloAgent)

# Instantiate and run MyApp
if __name__ == "__main__":
    MyApp()
```

![http://pastiche.googlecode.com/files/art.gif](http://pastiche.googlecode.com/files/art.gif)