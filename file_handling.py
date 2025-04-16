def modify_content(content):
    return content.upper()

def main():
    filename = input("Enter filename to read:")

    try:
        with open(filename, 'r') as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist")
        return
    except IOError:
        print(f"Could not read the file '{filename}'.")
        return
    
    modified_content = modify_content(content)
    output_filename = "modified_" + filename

    try:
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Modified content written to '{output_filename}'")
    except IOError:
        print(f"Could not write to the file '{output_filename}'.")

if __name__ == "__main__":
    main()