import os
import re
from pdf_reader import read_pdf
from metadata_extractor import extract_metadata
from keyword_extractor import extract_keywords


def fix_metadata(meta, text):
    """
    Apply rule-based corrections to extracted metadata.

    Improves robustness beyond LLM output.
    """

    # Remove unrealistic short titles
    if meta["title"] and len(meta["title"].split()) < 3:
        meta["title"] = None

    # Clean author formatting
    if meta["authors"]:
        meta["authors"] = [
            a.replace("\xa0", " ").strip()
            for a in meta["authors"]
        ]

    # Fallback year detection using regex
    if not meta["year"]:
        match = re.search(r"(20\d{2}|19\d{2})", text)
        if match:
            meta["year"] = match.group(0)

    # Fallback journal detection
    if not meta["journal"]:
        journals = [
            "Nature", "Science", "Sensors",
            "Micromachines", "Analyst",
            "Scientific Reports",
            "Microfluidics", "Nanofluidics"
        ]
        for j in journals:
            if j.lower() in text.lower():
                meta["journal"] = j
                break

    return meta


def process_folder(client, model, folder_path):
    """
    Process all PDFs in a folder and extract structured data.
    """

    results = []

    if not os.path.exists(folder_path):
        print(f"Error: '{folder_path}' folder not found.")
        return results

    for file in os.listdir(folder_path):

        if file.endswith(".pdf"):

            file_path = os.path.join(folder_path, file)
            print(f"Processing: {file}")

            try:
                text = read_pdf(file_path)

                # LLM-based extraction
                meta = extract_metadata(client, model, text)

                # Rule-based correction
                meta = fix_metadata(meta, text)

                # Keyword extraction
                keywords = extract_keywords(client, model, text)

                results.append({
                    "file_name": file,
                    "title": meta.get("title"),
                    "authors": meta.get("authors"),
                    "journal": meta.get("journal"),
                    "year": meta.get("year"),
                    "keywords": keywords
                })

            except Exception as e:
                print(f"Error processing {file}: {e}")

    return results