Now, let's try asking an agent to write come code and commit the resulting code to the current branch of this repository.

To do that, let's give the agent the necessary tools it will need which in this case will be python functions that perform different github actions using the `subprocess` package.
We'll follow the basic steps for building a langchain agent:

# Steps for building a simple agent:
- Set up the LLM
- Define the tool or toolkit (list of tools)
- Set up a prompt template
- Connect llm with your tools
- Define your agent as a dict with keys: input, and agent scratchpad 
- Use the Langchain LCEL language to pipe agent, prompt the llm_with_tools variable and the output parser (which can use OpenAI function calling parser)
- Create the agent loop
- Wrap everything into the AgentExecutor
- Invoke the agent with some query input

# setup the llm
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0)