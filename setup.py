import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="numba_timer",
    version="0.1.2",
    author="Mihir Patel",
    author_email="abc55abc55@gmail.com",
    description="A helper package to easily time Numba CUDA GPU events",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mihi-r/numba_timer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['numba>=0.51.0']
)