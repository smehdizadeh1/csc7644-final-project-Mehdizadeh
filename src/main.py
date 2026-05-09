import os
from dotenv import load_dotenv
from llm_client import create_client
from processor import process_folder
from search import search_papers
from utils import save_jsonl, save_excel

# ==========================
# LOAD ENVIRONMENT VARIABLES
# ==========================
load_dotenv()

# Initialize LLM client and model
client, MODEL = create_client()

# ==========================
# CONFIGURATION
# ==========================
DATA_FOLDER = "data"
OUTPUT_JSONL = "publications.jsonl"

# ==========================
# MAIN PROGRAM LOOP
# ==========================
if __name__ == "__main__":

    while True:

        # Menu display
        print("\n==============================")
        print("1 - Build database")
        print("2 - Search papers")
        print("0 - Exit")
        print("==============================")

        choice = input("Select option: ")

        # Exit program
        if choice == "0":
            print("Exiting program...")
            break

        # Build database from PDFs
        elif choice == "1":

            if not os.path.exists(DATA_FOLDER):
                print(f"Error: '{DATA_FOLDER}' folder not found.")
                continue

            data = process_folder(client, MODEL, DATA_FOLDER)

            save_jsonl(data, OUTPUT_JSONL)

            # Optional Excel export
            if input("Save Excel file? (y/n): ").lower() == "y":
                save_excel(data, "publications.xlsx")

            print("\nDatabase build complete.")

        # Search functionality
        elif choice == "2":

            query = input("Enter keyword(s): ")
            jsonl_path = os.path.join("outputs", OUTPUT_JSONL)

            if not os.path.exists(jsonl_path):
                print("Error: Database not found. Run option 1 first.")
                continue

            results = search_papers(jsonl_path, query)

            if results:
                print("\nResults:\n")

                for r in results:
                    print(f"Score: {r['score']}")
                    print("File:", r["file_name"])
                    print("Title:", r["title"])
                    print("Keywords:", r["keywords"])
                    print("-" * 40)

                # Optional Excel export
                if input("Save results to Excel? (y/n): ").lower() == "y":
                    file_name = f"search_results_{query.replace(' ', '_')}.xlsx"
                    save_excel(results, file_name)

            else:
                print("No matching papers found.")

        else:
            print("Invalid option. Please try again.")