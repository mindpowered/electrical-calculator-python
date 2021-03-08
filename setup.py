import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='mindpowered-electricalc',
    version='0.0.2',
    author="Mind Powered Corporation",
    author_email="support@mindpowered.dev",
    license="MIT",
    url="https://mindpowered.dev/",
    description="Calculator for electrical wiring and circuits",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['electricalc'],
    packages=['mindpowered_electricalc'],
    package_dir={'mindpowered_electricalc': 'wrappers'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'mindpowered-maglev',
    ],
)
