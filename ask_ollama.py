import datetime

import ollama

SYSTEM = (
    "You are a sarcastic but brilliant Senior AI Engineer. "
    "Answer the user's question briefly, but always end with a piece of advice for a junior developer."
)


def get_current_time() -> str:
    """Return the current date and time."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


question = input("What do you want to know? ")
print("Thinking...", flush=True)

messages = [
    {"role": "system", "content": SYSTEM},
    {"role": "user", "content": question},
]

response = ollama.chat(
    model="llama3.2",
    messages=messages,
    tools=[get_current_time],
)
messages.append(response.message)

if response.message.tool_calls:
    for call in response.message.tool_calls:
        if call.function.name == "get_current_time":
            result = get_current_time()
        else:
            result = "Unknown tool"
        messages.append(
            {"role": "tool", "tool_name": call.function.name, "content": str(result)}
        )

    response = ollama.chat(
        model="llama3.2",
        messages=messages,
        tools=[get_current_time],
    )

print(response.message.content)
