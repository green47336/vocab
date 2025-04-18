import json


def sort_vocab(input_file, sort_key):
    """
    Sorts the JSON data by the specified key and overwrites the input file with the sorted data.

    :param input_file: Path to the input JSON file.
    :param sort_key: The key to sort the JSON data by.
    """
    try:
        # Load the JSON data from the input file
        with open(input_file, "r") as file:
            data = json.load(file)

        # Sort the data by the specified key
        sorted_data = sorted(data, key=lambda x: x.get(sort_key, ""))

        # Overwrite the input file with the sorted data
        with open(input_file, "w") as file:
            json.dump(sorted_data, file, indent=2)

        print(f"Data sorted by '{sort_key}' and written to '{input_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Define the input file path
    input_file = "vocab.json"

    # Define the key to sort by
    sort_key = "term"

    # Call the sort function
    sort_vocab(input_file, sort_key)
