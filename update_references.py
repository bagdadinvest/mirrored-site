import os
import re

# Base directory path
base_directory = "/home/lofa/Desktop/baking/mirrored_site/"

# Regex patterns to find CSS and JS file references
css_pattern = r'(<link\s+[^>]*href\s*=\s*["\'])([^"\']+\.css)(["\'][^>]*>)'
js_pattern = r'(<script\s+[^>]*src\s*=\s*["\'])([^"\']+\.js)(["\'][^>]*>\s*</script>)'

# Function to update file references
def update_references(file_path):
    # Read the content of the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Store modifications and file path for reporting
    changes_made = False
    updated_content = content

    # Replace CSS references
    def replace_css(match):
        nonlocal changes_made
        original_reference = match.group(2)
        if not original_reference.endswith(".min.css"):
            minified_reference = original_reference.replace(".css", ".min.css")
            print(f"File: {file_path}")
            print(f"CSS - Original: {original_reference}")
            print(f"CSS - Updated: {minified_reference}\n")
            changes_made = True
            return match.group(1) + minified_reference + match.group(3)
        return match.group(0)

    # Replace JS references
    def replace_js(match):
        nonlocal changes_made
        original_reference = match.group(2)
        if not original_reference.endswith(".min.js"):
            minified_reference = original_reference.replace(".js", ".min.js")
            print(f"File: {file_path}")
            print(f"JS - Original: {original_reference}")
            print(f"JS - Updated: {minified_reference}\n")
            changes_made = True
            return match.group(1) + minified_reference + match.group(3)
        return match.group(0)

    # Apply replacements for CSS and JS
    updated_content = re.sub(css_pattern, replace_css, updated_content)
    updated_content = re.sub(js_pattern, replace_js, updated_content)

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
                update_references(file_path)

# Run the script
update_html_files_in_directory(base_directory)
print("CSS and JS references update completed.")
