import requests
from nexusraven_utils import query_raven

# Generates the joke by calling the Joke API https://jokeapi.dev/
def give_joke(category : str):
    """
    Joke categories. Supports: Any, Programming, Misc, Dark, Pun, Spooky, Christmas.
    """
    url = f"https://v2.jokeapi.dev/joke/{category}?safe-mode&type=twopart"
    print("The NexusRaven generated GET request is: " + url)
    response = requests.get(url)
    print("Joke setup: " + response.json()["setup"])
    print("Joke delivery: " + response.json()["delivery"])

USER_QUERY = "Can you tell me a joke about computers?"

# Construct the prompt for the RavenNexus LLM including a function definiton and the user query
raven_prompt = \
f'''
def give_joke(category : str):
    """
    Joke categories. Supports: Any, Programming, Misc, Dark, Pun, Spooky, Christmas.
    """
User Query: {USER_QUERY}<human_end>
'''
# Query the RavenNexus LLM
# The LLM answers with the function call that needs to be executed
# In this example, the LLM answers with "give_joke(category='Programming')"
call = query_raven(raven_prompt)

# Execute the function "give_joke(category='Programming')"
exec(call)
