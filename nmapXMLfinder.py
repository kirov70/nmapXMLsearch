import os
import shutil

# Define the source directory and target directory
source_dir = 'results'
target_dir = 'xml'

# Create the target directory if it doesn't exist
os.makedirs(target_dir, exist_ok=True)

# Walk through the directory structure
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file in ["_top_100_udp_nmap.xml", "_full_tcp_nmap.xml"]:
            # Generate the unique name based on the directory structure
            relative_path = os.path.relpath(root, source_dir)
            unique_name = f"{relative_path.replace(os.sep, '_')}_{file}"
            
            # Source file path
            source_file = os.path.join(root, file)
            
            # Destination file path
            destination_file = os.path.join(target_dir, unique_name)
            
            # Copy the file to the target directory with the new unique name
            shutil.copy2(source_file, destination_file)

print("Files have been copied and renamed successfully.")

