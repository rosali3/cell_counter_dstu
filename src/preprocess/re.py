import os

# Define the source directory, destination directory, and the prefix to remove
source_directory = '/home/rosalie/Desktop/livecell_bot/image'
destination_directory = '/home/rosalie/Desktop/livecell_bot/renamed_images'
prefix = 'dust_'

# Ensure the destination directory exists
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Iterate over all files in the source directory
for filename in os.listdir(source_directory):
    # Check if the file starts with the prefix
    if filename.startswith(prefix):
        # Create the new filename by removing the prefix
        new_filename = filename[len(prefix):]
        # Create the full path for the old and new filenames
        old_filepath = os.path.join(source_directory, filename)
        new_filepath = os.path.join(destination_directory, new_filename)
        # Rename (move) the file
        os.rename(old_filepath, new_filepath)
        print(f'Renamed and moved: {old_filepath} to {new_filepath}')

