import os
from PIL import Image

# Base directory containing images
base_directory = "/home/lofa/Desktop/baking/mirrored_site/media/images/"

# Supported image extensions for conversion
supported_extensions = (".png", ".jpg", ".jpeg")

# Function to convert images to WebP format
def convert_to_webp(image_path):
    # Create WebP image path
    webp_image_path = os.path.splitext(image_path)[0] + ".webp"

    # Open the image and convert it
    with Image.open(image_path) as image:
        image.save(webp_image_path, "webp")
        print(f"Converted: {image_path} -> {webp_image_path}")

# Function to traverse the directory and convert images
def convert_images_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(supported_extensions):
                file_path = os.path.join(root, file)
                convert_to_webp(file_path)

# Run the script to convert images
convert_images_in_directory(base_directory)
print("Image conversion to WebP completed.")
