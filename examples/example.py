from ai_image_tool.enhance import enhance_image
from ai_image_tool.filters import apply_blur

# Enhance the image
enhanced_image = enhance_image("sample_image.jpg", sharpness_factor=2.5, contrast_factor=1.8)
print(f"Enhanced image saved at: {enhanced_image}")

# Apply blur filter
blurred_image = apply_blur("sample_image.jpg", blur_radius=3)
print(f"Blurred image saved at: {blurred_image}")
