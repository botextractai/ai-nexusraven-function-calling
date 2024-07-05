# Using the open source NexusRaven LLM for function calling

[NexusRaven](https://github.com/nexusflowai/) is an open source and commercially viable function calling Large Language Model (LLM). NexusRaven is small enough (13B) to be deployed locally using a local LLM server platform like [Ollama](https://ollama.com/). The NexusRaven LLM can be downloaded from [Hugging Face](https://huggingface.co/).

Most LLMs are trained to generate text, image, video, or audio output. NexusRaven is specialised in generating valid function calls as output. These function calls can be API calls, SQL statements, and many more.

These function call outputs from NexusRaven can then be used for further processing in agentic workflows. Note that NexusRaven cannot execute generated functions directly. This must be done with program code.

It would of course also be possible to write function calls directly using program code, but the advantage of using specialised function calling LLMs like NexusRaven is that LLMs can understand natural language (unstructured text). As an example, NexusRaven can therefore automatically extract information from customer support conversations and generate matching SQL statements to store information from these conversations (such as customer details, products, problems, sentiments etc.) in a SQL database.

NexusRaven is therefore often an important part of agentic workflows. Because it is an open source LLM that can be used locally, it is particularly helpful when data should be kept private and therefore not sent to large LLM providers like Microsoft, Google, or Amazon Web Services. Using NexusRaven locally is also a good solution to minimise costs.

This example works directly with the public NexusRaven endpoint and does not require an API key. It can be executed by running the `main.py` script.

In this example, NexusRaven generates a valid function call that will then call the [JokeAPI](https://jokeapi.dev/), a free public API that answers with jokes from various categories in multiple languages.

1. In this example, the NexusRaven LLM is asked:  
   `Can you tell me a joke about computers?`
2. The NexusRaven LLM generates a function call as answer. In this example, the NexusRaven LLM output function  
   `give_joke(category='Programming')`  
   then calls the JokeAPI:  
   `https://v2.jokeapi.dev/joke/Programming?safe-mode&type=twopart`
3. The JSON formatted answer from the JokeAPI contains a joke setup and joke delivery similar to this:  
   Joke setup: `Why did the database administrator leave his wife?`  
   Joke delivery: `She had one-to-many relationships.`
