import os

def shorten_files(base_dir, start_line, end_line):
    # Walk through all directories and files in base_dir
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('_streamflow_qc.txt'):
                file_path = os.path.join(root, file)
                print(f"Processing {file_path}...")
                
                # Read the specified range of lines from the file
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                
                # The line numbers in Python are zero-indexed, hence the -1 adjustment
                selected_lines = lines[start_line-1:end_line]
                
                # Write the selected lines back to the same file
                with open(file_path, 'w') as file:
                    file.writelines(selected_lines)
                print(f"Updated {file_path}")

# Specify the base directory where the files are located
base_directory = '.'
start = 5021
end = 12328

# Call the function
shorten_files(base_directory, start, end)
