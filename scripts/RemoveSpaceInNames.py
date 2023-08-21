import os

def rename_images(folder_path):
    if not os.path.exists(folder_path):
        print("Folder not found.")
        return
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            new_filename = filename.replace(" ", "")
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed '{filename}' to '{new_filename}'")

if __name__ == "__main__":
    target_folder = "images/tutorials/0820"  # Replace with the actual folder path
    rename_images(target_folder)
