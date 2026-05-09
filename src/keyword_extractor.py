def extract_keywords(client, model, text):
    """
    Extract clean technical keywords from text using an LLM.

    Parameters:
        client (OpenAI): Initialized LLM client
        model (str): Model name
        text (str): Input text from PDF

    Returns:
        list[str]: List of extracted keywords (max 20)
    """

    # Input size (by considering efficiency and cost)
    short_text = " ".join(text.split()[:400])

    # LLM request for keyword extraction
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "Extract ONLY 15-20 technical keywords.\n"
                    "Return ONLY comma-separated words.\n"
                    "NO explanations. NO sentences."
                )
            },
            {"role": "user", "content": short_text}
        ],
        temperature=0,
        max_tokens=120
    )

    # Normalize and clean output
    raw = response.choices[0].message.content.strip().lower()
    raw = raw.replace("here are", "")
    raw = raw.replace("keywords", "")
    raw = raw.replace(":", "")

    # Split into keyword list
    keywords = [
        k.strip()
        for k in raw.split(",")
        if len(k.strip()) > 3
    ]

    return list(set(keywords))[:20]  # Remove duplicates and limit size