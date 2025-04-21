def read_and_write_file():
    try:
        # Ask the user for the filename
        filename = input("Enter the filename to read: ")

        # Open the existing file for reading
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content (for example, converting text to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"The file has been successfully read and written to {new_filename}.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{filename}' cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_and_write_file()
