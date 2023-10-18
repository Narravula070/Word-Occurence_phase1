# Function to count word occurrences in a text file
def count_word_occurrences(file_path):
    word_counts = {}  # Dictionary to store word occurrences

    # Open the file in read mode
    with open(file_path, 'r') as file:
       
        for line in file:
       
            words = line.split()

            for word in words:
                # Remove punctuation and convert to lowercase
                cleaned_word = word.strip('.,!?()[]{}":;').lower()

                # Update word counts in the dictionary
                if cleaned_word in word_counts:
                    word_counts[cleaned_word] += 1
                else:
                    word_counts[cleaned_word] = 1

    return word_counts

# Main function to read a text file and count word occurrences
def main():
    file_path = input("Enter the path of the text file: ")

    try:
        # Call the function to count word occurrences
        word_counts = count_word_occurrences(file_path)

        # Print unique words and their occurrences
        print("Unique words and their occurrences:")
        for word, count in word_counts.items():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
