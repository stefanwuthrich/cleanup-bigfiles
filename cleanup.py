import os
import sys

def delete_large_files(directory, size_gb):
    size_bytes = size_gb * 1024 ** 3  # Convert GB to Bytes

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
                if file_size > int(size_bytes):
                    print(f"Found: {file_path} ({file_size / (1024 ** 3):.2f} GB)")
                    user_input = input(f"Do you want to delete this file? (Y/n): ").strip().lower()
                    if user_input in ['y', '']:
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")
                    else:
                        print(f"Skipped: {file_path}")
            except OSError:
                # Skip errors accessing the file
                pass

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python cleanup.py <directory> <size_in_gb>")
        sys.exit(1)

    directory = sys.argv[1]
    try:
        size_gb = float(sys.argv[2])
    except ValueError:
        print("The size should be a number representing the size in GB.")
        sys.exit(1)

    delete_large_files(directory, size_gb)
