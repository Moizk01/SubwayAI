from PIL import Image, ImageOps

def match_histogram(source, template):
    """
    Adjust the pixel values of a grayscale image such that its histogram
    matches that of a target image
    """
    source = source.convert("L")
    template = template.convert("L")
    
    source_histogram = source.histogram()
    template_histogram = template.histogram()

    # Cumulative sum of the histograms (normalized to the interval 0..1)
    source_cumsum = source_histogram.cumsum() / source_histogram.sum()
    template_cumsum = template_histogram.cumsum() / template_histogram.sum()

    # Create a lookup table to map the pixel values from source to those in the template
    lookup_table = np.interp(source_cumsum, template_cumsum, np.arange(256))
    source_matched = source.point(lookup_table)
    
    return source_matched

# Load the images
source_image = Image.open(standard_image_path)
template_image = Image.open(correct_contrast_image_path)

# Match histograms
matched_image = match_histogram(source_image, template_image)

# Convert back to RGB and save the image
matched_image = ImageOps.colorize(matched_image, black="black", white="white")
matched_image_path = '/mnt/data/matched_image.jpg'
matched_image.save(matched_image_path)
