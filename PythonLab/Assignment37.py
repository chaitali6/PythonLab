def count_words_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            # Initialize word count
            word_count = 0
            # Read each line from the file
            for line in file:
                # Split the line into words and count them
                words = line.split()
                word_count += len(words)
        
        # Display the total number of words
        print(f"Total number of words in {file_name}: {word_count}")
    
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
count_words_in_file('ABC.txt')

#Output
#Total number of words in ABC.txt: 0

