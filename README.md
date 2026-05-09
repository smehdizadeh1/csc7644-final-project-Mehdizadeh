# Intelligent Research Paper Analyzer Using Large Language Models

---

## Project Overview

This application is designed to automatically analyze scientific research papers in PDF format using a Large Language Model (LLM). It converts unstructured academic documents into structured data by extracting metadata and identifying important technical concepts.

The system also provides a simple search capability that allows users to retrieve relevant papers based on keywords.

This work is developed as part of the final project for *CSC 7644: Applied LLM Development*.

---

## What This Application Can Do

- Read and process PDF research papers  
- Extract key metadata (title, authors, journal, publication year)  
- Identify important technical keywords using an LLM  
- Store processed results in structured formats (JSONL and Excel)  
- Search across processed papers using user-defined keywords  
- Rank results based on relevance  
- Handle incomplete or malformed LLM responses gracefully  

---

## Technology Stack

The project is implemented using the following tools:

- Python (3.10 or newer)
- OpenRouter / OpenAI API (LLM access)
- PyPDF (for reading PDF files)
- Pandas (data organization and export)
- JSON / JSONL formats
- python-dotenv (environment variable management)

---

## System Design (High-Level)

The application is divided into multiple components:

- PDF Processing --> extracts raw text from documents  
- Metadata Module --> uses LLM to extract structured information  
- Keyword Module --> generates domain-specific keywords  
- Processing Pipeline --> applies extraction to all files  
- Search Engine --> matches user queries with stored keywords  
- Output Manager --> saves results in organized files  
- CLI Interface --> allows user interaction through terminal  

---

## Setup Guide

### Requirements

- Python installed (version 3.10 or higher)
- pip package manager

---

### Installation Steps

1. Clone or download this repository  
2. Open your terminal (Command Prompt / PowerShell / Terminal)  
3. Navigate to the project directory  
4. Install dependencies:
    pip install -r requirements.txt

---

### Important Step: Add Your PDF Files

The system does **not include PDF files by default**.
You must manually add them:
    --> Place your research papers inside the `data/` folder  
Example:
    data/
    paper_A.pdf
    paper_B.pdf
Only files placed in this directory will be processed.

---

### Environment Configuration

1. Copy `.env.example` --> `.env`  
2. Open `.env` file  
You can configure which API to use by setting:
    LLM_PROVIDER=openai
or
    LLM_PROVIDER=openrouter
3. Depending on the selected provider, set the corresponding key:
For OpenAI:
    OPENAI_API_KEY=your_openai_key_here
For OpenRouter:
    OPENROUTER_API_KEY=your_openrouter_key_here
- If `LLM_PROVIDER` is not specified, the system uses *OpenAI by default*
- The program automatically initializes the correct API client at runtime  
- No code modification is required to switch between providers

---

## Running the Program

Run the application using:
    python src/main.py

---

## How to Use

Once the program starts, you will see:
    1 - Build database
    2 - Search papers
    0 - Exit

---

### Option 1: Build Database

- Reads all PDFs from `data/`
- Extracts metadata and keywords
- Creates output files:
    outputs/publications.jsonl
    outputs/publications.xlsx

---

### Option 2: Search

- Enter keywords (example: "cell sorting")
- System returns matching papers ranked by relevance
- Optionally saves results to:
    outputs/search_results_<query>.xlsx

---

## Output Files

All generated results are stored in the `outputs/` directory:

- Structured dataset (JSONL format)
- Excel file for processed papers
- Search results files

---

## Project Structure

src/ --> main program modules
    src/main.py --> program entry point and CLI interface  
    src/llm_client.py --> handles API selection (OpenAI / OpenRouter) and client creation  
    src/pdf_reader.py --> extracts raw text from PDF files  
    src/metadata_extractor.py --> extracts structured metadata using LLM  
    src/keyword_extractor.py --> generates technical keywords using LLM  
    src/processor.py --> main pipeline for processing all PDFs  
    src/search.py --> performs keyword-based search and ranking  
    src/utils.py --> handles saving outputs (JSONL and Excel) and data cleaning  
data/ --> input PDF files (user-provided)  
outputs/ --> generated results (JSONL, Excel, search outputs)  
.env.example --> environment configuration template  
README.md --> project documentation  

---

## Method Summary

The workflow of the system:

1. Extract text from PDF documents  
2. Send text to LLM for structured metadata extraction  
3. Generate keywords using LLM reasoning  
4. Store results in JSONL format  
5. Perform keyword-based matching for search  
6. Rank results based on keyword overlap  

---

## Notes and Limitations

- Some PDFs may not parse correctly due to formatting issues  
- LLM responses may occasionally require validation  
- Keyword matching is based on simple scoring (not semantic similarity)  

---

## References

- OpenAI API documentation  
- OpenRouter API documentation  
- PyPDF documentation  
- Pandas documentation
