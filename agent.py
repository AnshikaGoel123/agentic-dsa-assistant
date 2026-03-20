from tools import generate_hint, explain_concept, analyze_code
from llm import call_llm
from memory import update_memory, add_to_history


def extract_topic(user_input):
    topics = [
        "array", "binary search", "stack",
        "queue", "linked list", "tree", "graph", "dp"
    ]

    user_input = user_input.lower()

    for topic in topics:
        if topic in user_input:
            return topic

    return "general"


def decide_action(user_input):
    prompt = f"""
    You are an intelligent DSA assistant.

    Identify ALL intents from the user input.

    Possible intents:
    - hint
    - explain
    - analyze

    Input: {user_input}

    Return intents as a comma-separated list.
    Example: "explain, analyze"
    """

    decision = call_llm(prompt).lower()
    return decision


def run_agent(user_input):

    if not user_input.strip():
        return "Please enter a valid query."

    if len(user_input) > 2000:
        return "Input too long. Please shorten it."

    decision = decide_action(user_input)

    topic = extract_topic(user_input)
    update_memory("user1", topic)

    responses = []

    if "explain" in decision:
        responses.append(explain_concept(user_input))

    if "analyze" in decision:
        responses.append(analyze_code(user_input))

    if "hint" in decision or not responses:
        responses.append(generate_hint(user_input))

    final_response = "\n\n".join(responses)

    add_to_history(user_input, final_response)

    return final_response