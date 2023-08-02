# Install the necessary package
!pip install bing-image-downloader

# Import the required modules
from bing_image_downloader import downloader
from google.colab import files
import shutil

# Define search keywords
search_keywords = [
    "Your queries 1",
    "Your queries 2",
    "Your queries 3",
    "Your queries 4"
]

# Set the download limit for each keyword
download_limit = 25

# Create a directory to save the images
output_dir = "crawled_images"
!mkdir -p $output_dir

# Download images for each keyword
for keyword in search_keywords:
    downloader.download(keyword, limit=download_limit, output_dir=output_dir)

print("Download completed.")

# Zip the crawled_images directory
shutil.make_archive("/content/crawled_images", 'zip', "/content/crawled_images")

# Download the zip file to your local computer
files.download("/content/crawled_images.zip")
