import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="number2words",
    version="0.0.1",
    author="Mohd. Shfikur Rahman",
    author_email="shafikshaon@gmail.com",
    description="A package which enable convert number to words in Django template.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shafikshaonio/django-number2words",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)