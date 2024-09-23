from setuptools import setup,find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requiriments = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    license="MIT License",
    author="Marcos Roberto",
    description="image processing package using skimage",
    long_description="page_description",
    long_description_content_type="text/markdown",
    url="https://github.com/Marcosestudy",
    keywords="prcessamento de imagem",
    packages=find_packages(),
    install_requires=requiriments,
    python_requires='>=3.5',
)
