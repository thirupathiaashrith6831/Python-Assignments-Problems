from PIL import Image
from PIL.ExifTags import TAGS

def get_image_info(image_path):
    try:
        img = Image.open(image_path)
        info = img.getexif()
        
        if not info:
            print("No metadata found.")
            return

        for tag_id, value in info.items():
            tag = TAGS.get(tag_id, tag_id)
            print(f"{tag:20}: {value}")
            
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
# get_image_info("vacation_photo.jpg")