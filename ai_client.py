from config import AI_PROVIDER

if AI_PROVIDER == "groq":
    from providers.groq_provider import ask_ai

elif AI_PROVIDER == "openai":
    from providers.openai_provider import ask_ai

else:
    raise ValueError("AI_PROVIDER must be 'groq' or 'openai'")