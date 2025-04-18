import json


def export_sorted_terms(input_file, output_file):
    """
    Extracts terms from the JSON file, sorts them alphabetically, and writes them to a text file.

    :param input_file: Path to the input JSON file.
    :param output_file: Path to the output text file.
    """
    try:
        # Load the JSON data from the input file
        with open(input_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Extract and sort the terms
        terms = sorted(item["term"] for item in data if "term" in item)

        # Write the sorted terms to the output file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write("\n".join(terms))

        print(f"Sorted terms written to '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Define the input and output file paths
    input_file = "vocab.json"
    output_file = "sorted_terms.txt"

    # Call the function to export sorted terms
    export_sorted_terms(input_file, output_file)
