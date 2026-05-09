import json


def extract_metadata(client, model, text):
    """
    Extract metadata (title, authors, journal, year) using LLM.

    Parameters:
        client (OpenAI): LLM client
        model (str): Model name
        text (str): Input text

    Returns:
        dict: Extracted metadata
    """

    # JSON schema for structured output
    schema = {
        "name": "paper_metadata",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "title": {"type": ["string", "null"]},
                "authors": {"type": ["array", "null"], "items": {"type": "string"}},
                "journal": {"type": ["string", "null"]},
                "year": {"type": ["string", "null"]}
            },
            "required": ["title", "authors", "journal", "year"],
            "additionalProperties": False
        }
    }

    # Prompt to guide LLM extraction
    prompt = (
        "Extract metadata from a scientific paper.\n\n"
        "Return:\n"
        "- Full correct title\n"
        "- Authors list\n"
        "- Journal name\n"
        "- Publication year\n\n"
        "Rules:\n"
        "- Do NOT return broken text\n"
        "- Do NOT return partial words\n"
        "- If uncertain, return null\n"
        "- Return ONLY JSON\n"
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text[:1500]}
        ],
        temperature=0,
        max_tokens=300,
        response_format={"type": "json_schema", "json_schema": schema}
    )

    try:
        return json.loads(response.choices[0].message.content)

    except json.JSONDecodeError:
        print("⚠️ Warning: Invalid JSON. Skipping.")
        return {
            "title": None,
            "authors": None,
            "journal": None,
            "year": None
        }