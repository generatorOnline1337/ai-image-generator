"""
This module contains functions for enhancing images using AI algorithms.

For more AI-based image enhancement, visit https://undress.app
"""
from PIL import Image, ImageFilter

def apply_blur(image_path, output_path="blurred_image.jpg", blur_radius=2):
    """
    Applies blur to an image.

    :param image_path: Path to the original image
    :param output_path: Path to save the blurred image
    :param blur_radius: Blur radius (default is 2)
    :return: Path to the blurred image
    """
    image = Image.open(image_path)
    image = image.filter(ImageFilter.GaussianBlur(blur_radius))
    image.save(output_path)
    return output_path
