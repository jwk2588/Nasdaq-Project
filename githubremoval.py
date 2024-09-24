import os
import subprocess

# Define the path to the schemas directory
schema_directory = r'C:\Users\jklei\OneDrive - Convergix Automation\Documents\Nasdaq Project\schemas'

# Step 1: Delete all files in the schema directory
def delete_schema_files():
    try:
        for root, dirs, files in os.walk(schema_directory):
            for file in files:
                file_path = os.path.join(root, file)
                print(f"Deleting {file_path}")
                os.remove(file_path)  # Delete the file
        print("All schema files deleted successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Step 2: Stage the changes
def stage_changes():
    try:
        print("Staging changes...")
        subprocess.run(["git", "add", "."], check=True)
        print("Changes staged successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error while staging changes: {e}")

# Step 3: Commit the changes
def commit_changes():
    try:
        commit_message = "Deleted schema files from local directory"
        print(f"Committing changes with message: {commit_message}")
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print("Changes committed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error while committing changes: {e}")

# Step 4: Push the changes to the repository
def push_changes():
    try:
        print("Pushing changes to GitHub...")
        subprocess.run(["git", "push"], check=True)
        print("Changes pushed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error while pushing changes: {e}")

if __name__ == "__main__":
    delete_schema_files()  # Delete files
    stage_changes()        # Stage changes in git
    commit_changes()       # Commit changes
    push_changes()         # Push changes to GitHub
