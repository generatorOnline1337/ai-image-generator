from setuptools import setup, find_packages

setup(
    name="ai_image_tool",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Pillow"
    ],
    description="AI-based image enhancement and filter application tool.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/your-repo-name/ai-image-enhancement-tool",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
