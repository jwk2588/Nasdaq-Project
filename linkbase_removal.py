import os

# Define the path to the linkbase directory
linkbase_directory = r'C:\Users\jklei\OneDrive - Convergix Automation\Documents\Nasdaq Project\linkbase'

# Step 1: Delete all files in the linkbase directory
def delete_linkbase_files():
    try:
        for root, dirs, files in os.walk(linkbase_directory):
            for file in files:
                file_path = os.path.join(root, file)
                print(f"Deleting {file_path}")
                os.remove(file_path)  # Actually delete the file
        print("All linkbase files deleted successfully.")
    except Exception as e:
        print(f"Error while deleting linkbase files: {e}")

if __name__ == "__main__":
    delete_linkbase_files()
