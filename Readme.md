# Cleanup Large Files Script

This script helps you to identify and optionally delete large files from a specified directory and its subdirectories. It scans through all the files and prompts you to delete any files that are larger than a specified size in GB.

## Features

- **Customizable Size Threshold**: You can specify the minimum file size (in GB) for files to be considered for deletion.
- **User Confirmation**: The script prompts you before deleting each large file, with a default option to delete if no input is provided.
- **Silent Error Handling**: Any errors encountered while accessing files are skipped without interrupting the script's execution or outputting error messages.

## Usage

### Prerequisites

- Python 3.x installed on your system.

### Running the Script

1. **Download or Clone the Script**:
   ```bash
   git clone [<repository-url>](https://github.com/stefanwuthrich/cleanup-bigfiles.git)
   cd [<repository-directory>](https://github.com/stefanwuthrich/cleanup-bigfiles.git)
   ```

2. **Run the Script**:
   ```bash
   python cleanup.py <directory> <size_in_gb>
   ```

   Replace `<directory>` with the path to the directory you want to clean up, and `<size_in_gb>` with the file size threshold in gigabytes.

### Example

To search for files larger than 2 GB in the `/home/user/Downloads` directory, run:

```bash
python cleanup.py /home/user/Downloads 2
```

The script will display each file it finds that exceeds the specified size and prompt you to delete it. Press `Enter` to confirm deletion (default is `Y`), or type `n` to skip.

### Script Details

- **Default Deletion Behavior**: If you press `Enter` without typing `Y` or `n`, the script will assume `Y` and delete the file.
- **Silent Error Handling**: If the script encounters an issue accessing a file (e.g., due to permissions), it will skip the file without displaying an error.

## License

This script is provided "as-is" without any warranty. You are free to use, modify, and distribute it as you see fit.

---

**Note**: Always ensure that you have backups of important data before running deletion scripts.
