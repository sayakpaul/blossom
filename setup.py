from setuptools import setup, find_packages

setup(
    name="blossoms_sayak",
    version="0.9.0",
    description="A simple Python package for math operations and geometry calculations.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Sayak Paul",
    author_email="spsayakpaul@gmail.com",
    package_dir={"": "src"},
    packages=find_packages("src"),
    package_data={"blossoms_sayak": ["py.typed"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)