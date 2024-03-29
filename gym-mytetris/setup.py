import setuptools

long_description = 'tetris gym environment wrapped to run on ezspark'

setuptools.setup(
    name = 'gym_mytetris',
    version = '0.0.2',
    install_requires = ['gym','gym-tetris', 'numpy', 'pygame'],
    author = 'EzSpark Team',
    author_email = 'team@ezspark.ai',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    description = long_description,
    url = 'https://github.com/ez-spark/gym-mytetris',
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.6",
)
