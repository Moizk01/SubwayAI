from PIL import Image, ImageEnhance
import os

def adjust_contrast(image_path, output_path, contrast_value):
    """Adjusts the contrast of an image."""
    with Image.open(image_path) as img:
        enhancer = ImageEnhance.Contrast(img)
        enhanced_img = enhancer.enhance(contrast_value)
        enhanced_img.save(output_path)

def process_images(folder_path, output_folder):
    """Processes all images in a folder."""
    for image_name in os.listdir(folder_path):
        if image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(folder_path, image_name)
            output_path = os.path.join(output_folder, image_name)
            adjust_contrast(image_path, output_path, 0.75)  # Lowering contrast by -100%

# Example usage
input_folder = 'C:\\Users\\moizk\\Documents\\SYDE\\4A\\461\\trainingset'
output_folder = 'C:\\Users\\moizk\\Documents\\SYDE\\4A\\461\\modified_set'
os.makedirs(output_folder, exist_ok=True)
process_images(input_folder, output_folder)
