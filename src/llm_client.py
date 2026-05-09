import os
from openai import OpenAI


def create_client():
    """
    Create and return an LLM client based on selected provider.

    Uses environment variable:
        LLM_PROVIDER = "openai" or "openrouter"

    Returns:
        tuple: (client instance, model name)
    """

    provider = os.getenv("LLM_PROVIDER", "openai").lower()

    openrouter_key = os.getenv("OPENROUTER_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")

    # Use OpenAI API
    if provider == "openai":
        if not openai_key:
            raise ValueError("OPENAI_API_KEY not set in .env")

        print("Using OpenAI API")
        return OpenAI(api_key=openai_key), "gpt-4o-mini"

    # Use OpenRouter API
    elif provider == "openrouter":
        if not openrouter_key:
            raise ValueError("OPENROUTER_API_KEY not set in .env")

        print("Using OpenRouter API")
        return OpenAI(
            api_key=openrouter_key,
            base_url="https://openrouter.ai/api/v1"
        ), "meta-llama/llama-3.3-70b-instruct"

    else:
        raise ValueError("Invalid LLM_PROVIDER. Use 'openai' or 'openrouter'")