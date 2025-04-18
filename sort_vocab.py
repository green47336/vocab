import json


def sort_vocab(input_file, output_file, sort_key):
    """
    Sorts the JSON data by the specified key and writes the sorted data to a new file.

    :param input_file: Path to the input JSON file.
    :param output_file: Path to the output JSON file.
    :param sort_key: The key to sort the JSON data by.
    """
    try:
        # Load the JSON data from the input file
        with open(input_file, "r") as file:
            data = json.load(file)

        # Sort the data by the specified key
        sorted_data = sorted(data, key=lambda x: x.get(sort_key, ""))

        # Write the sorted data to the output file
        with open(output_file, "w") as file:
            json.dump(sorted_data, file, indent=2)

        print(f"Data sorted by '{sort_key}' and written to '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Define the input and output file paths
    input_file = "vocab.json"
    output_file = "sorted_vocab.json"

    # Specify the field to sort by (e.g., "term", "noun", "year")
    sort_key = "term"

    # Call the sort function
    sort_vocab(input_file, output_file, sort_key)
