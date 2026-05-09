import json


def search_papers(jsonl_file, query):
    """
    Search papers using keyword matching.

    Parameters:
        jsonl_file (str): Path to database file
        query (str): Search query

    Returns:
        list[dict]: Ranked search results
    """

    query_words = query.lower().split()
    results = []

    with open(jsonl_file, "r", encoding="utf-8") as f:

        for line in f:
            paper = json.loads(line)

            keywords_list = paper.get("keywords", [])
            keywords_str = " ".join(keywords_list).lower()

            # Count matches
            score = sum(word in keywords_str for word in query_words)

            if score > 0:
                results.append({
                    "score": score,
                    "file_name": paper["file_name"],
                    "title": paper["title"],
                    "keywords": ", ".join(keywords_list)
                })

    # Sort by relevance
    results.sort(key=lambda x: x["score"], reverse=True)

    return results