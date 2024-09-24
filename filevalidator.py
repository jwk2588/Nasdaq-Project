import os
import hashlib

def get_file_hash(filepath):
    """Generate a hash for the file content to check if two files are identical."""
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def gather_files_with_paths(root_dir, skip_folders=[]):
    """Gather all files from a directory and its subdirectories, skipping specific subfolders."""
    file_dict = {}
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip any unwanted subfolders
        dirnames[:] = [d for d in dirnames if d not in skip_folders]
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            file_dict[file] = file_path  # Store the file name as key and path as value
    return file_dict

def compare_folders(org_dir, flat_dir, skip_folders=[]):
    """Compare files in two directories, accounting for subfolder differences."""
    
    # Get files from both directories
    org_files = gather_files_with_paths(org_dir, skip_folders)  # Organized folder structure
    flat_files = gather_files_with_paths(flat_dir)  # Flat folder structure (with subfolders like dis, elts, etc.)

    # Check for missing files or different content
    missing_in_org = []
    missing_in_flat = []
    different_files = []

    for flat_file, flat_path in flat_files.items():
        if flat_file in org_files:
            org_path = org_files[flat_file]
            # Compare the content via hash
            if get_file_hash(org_path) != get_file_hash(flat_path):
                different_files.append(flat_file)
        else:
            missing_in_org.append(flat_file)
    
    for org_file in org_files.keys():
        if org_file not in flat_files:
            missing_in_flat.append(org_file)

    # Print the results
    print("\n=== Comparison Report ===")
    
    if missing_in_org:
        print(f"Files in the flat folder but missing in the organized folder: {missing_in_org}")
    else:
        print("No files missing in the organized folder.")
    
    if missing_in_flat:
        print(f"Files in the organized folder but missing in the flat folder: {missing_in_flat}")
    else:
        print("No files missing in the flat folder.")
    
    if different_files:
        print(f"Files that exist in both folders but differ in content: {different_files}")
    else:
        print("No differing files found.")

# Paths to both directories
organized_folder = r"C:\Users\jklei\OneDrive - Convergix Automation\Documents\Nasdaq Project\us-gaap-2024"
flat_folder = r"C:\Users\jklei\OneDrive - Convergix Automation\Documents\Bizfinx XBRL Tagging\us-gaap-2024"

# Folders to skip in the organized structure (like linkbase and schema, if applicable)
skip_folders = ['linkbase', 'schema']

# Run the comparison
compare_folders(organized_folder, flat_folder, skip_folders)
