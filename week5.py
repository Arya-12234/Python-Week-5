# file_handling_assignment.py

# File Creation and Writing
try:
    # Open the file in write mode ('w') and create it if it doesn't exist
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is line 1.\n")
        file.write("This is line 2 with a number: 123.\n")
        file.write("Line 3, welcome to Python file handling.\n")
    print("File created and initial content written successfully.")

except PermissionError:
    print("Error: You don't have permission to write to the file.")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

# File Reading and Displaying
try:
    # Open the file in read mode ('r') and read its content
    with open("my_file.txt", "r") as file:
        content = file.read()
    print("\nContents of 'my_file.txt':")
    print(content)

except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending
try:
    # Open the file in append mode ('a') and add more content
    with open("my_file.txt", "a") as file:
        file.write("Appending line 4: Another text.\n")
        file.write("Appending line 5: Adding more data with a number: 456.\n")
        file.write("Appending line 6: File handling is easy!\n")
    print("\nAdditional content appended successfully.")

except PermissionError:
    print("Error: You don't have permission to append to the file.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

# Final Reading and Display after Appending
try:
    # Open the file in read mode ('r') and read its content after appending
    with open("my_file.txt", "r") as file:
        content = file.read()
    print("\nUpdated contents of 'my_file.txt':")
    print(content)

except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except Exception as e:
    print(f"An error occurred while reading the file after appending: {e}")
finally:
    print("\nFile operations completed.")
