user_memory = {}
chat_history = []

def update_memory(user, topic):
    if user not in user_memory:
        user_memory[user] = {}

    user_memory[user][topic] = user_memory[user].get(topic, 0) + 1


def get_weak_topics(user):
    if user not in user_memory:
        return []

    topics = sorted(user_memory[user].items(), key=lambda x: x[1], reverse=True)
    return [topic for topic, _ in topics]


def add_to_history(user_input, response):
    chat_history.append({
        "user": user_input,
        "assistant": response
    })


def get_history():
    history_text = ""

    for chat in chat_history[-5:]:
        history_text += f"User: {chat['user']}\n"
        history_text += f"Assistant: {chat['assistant']}\n"

    return history_text