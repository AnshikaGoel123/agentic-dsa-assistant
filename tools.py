from llm import call_llm

def generate_hint(query):
    prompt = f"""
    You are a DSA mentor.

    Rules:
    - Do NOT give full solution
    - Give only a small hint

    Problem: {query}
    """
    return call_llm(prompt)


def explain_concept(query):
    prompt = f"""
    Explain this DSA concept in simple terms with an example:

    {query}
    """
    return call_llm(prompt)


def analyze_code(code):
    prompt = f"""
    You are a coding interviewer.

    Analyze this code:

    {code}

    Provide:
    1. Errors (if any)
    2. Edge cases
    3. Optimization suggestions
    4. Time and space complexity
    """
    return call_llm(prompt)


def generate_code(question):
    prompt = f"""
    Give code.
    Write a clean and simple C++ solution.
    Do not add explanation.
    Question: {question}
    """
    return call_llm(prompt)