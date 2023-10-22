# Open the file 'words.txt' for reading.
file = open('words.txt')

# Read the entire contents of the file into a string.
fread = file.read()

# Initialize a counter to count the number of characters in the file.
count = 0

# Iterate over each line in the file.
for line in fread:
  # Increment the counter by the number of characters in the line.
  count += len(line)

  # Strip any leading or trailing whitespace from the line.
  word = line.strip()

  # Split the line into a list of words.
  word = line.split()

# Print the contents of the file.
print(fread)

# Print the number of characters in the file.
print(f"There are {count} characters in this file")

# Print the number of words in the file.
print(f"There are {len(word)} words in this file")
