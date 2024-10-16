from PIL import Image, ImageEnhance

def enhance_image(image_path, output_path="enhanced_image.jpg", sharpness_factor=2.0, contrast_factor=1.5):
    """
    Enhances an image by increasing sharpness and contrast.

    :param image_path: Path to the original image
    :param output_path: Path to save the enhanced image
    :param sharpness_factor: Sharpness factor (default is 2.0)
    :param contrast_factor: Contrast factor (default is 1.5)
    :return: Path to the enhanced image
    """
    # Open the image
    image = Image.open(image_path)

    # Apply sharpness filter
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(sharpness_factor)

    # Apply contrast filter
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast_factor)

    # Save the image
    image.save(output_path)
    return output_path
