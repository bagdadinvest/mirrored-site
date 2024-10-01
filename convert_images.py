import os
import re

# Base directory containing HTML files
base_directory = "/home/lofa/Desktop/baking/mirrored_site/"

# Regex pattern to find image file references
image_pattern = r'(<img\s+[^>]*src\s*=\s*["\'])([^"\']+\.(png|jpg|jpeg))(["\'][^>]*>)'

# Function to update image references in HTML files
def update_image_references(file_path):
    # Read the content of the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Store modifications and file path for reporting
    changes_made = False

    # Replace image references
    def replace_image(match):
        nonlocal changes_made
        original_reference = match.group(2)
        # Create the new reference with .webp extension
        webp_reference = re.sub(r'\.(png|jpg|jpeg)$', '.webp', original_reference)
        print(f"File: {file_path}")
        print(f"Image - Original: {original_reference}")
        print(f"Image - Updated: {webp_reference}\n")
        changes_made = True
        return match.group(1) + webp_reference + match.group(4)

    # Apply replacements for image references
    updated_content = re.sub(image_pattern, replace_image, content)

    # Write the changes back to the file if modifications were made
    if changes_made:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

# Function to traverse the directory and find all HTML files
def update_html_files_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                update_image_references(file_path)

# Run the script to update HTML references
update_html_files_in_directory(base_directory)
print("Image references update in HTML files completed.")
