import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="msaconverter",
    version="0.0.4",
    author='Guanliang Meng',
    author_email='mengguanliang@genomics.cn',
    description="To convert multiple alignment sequences (msa) to different format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3',
    url='http://mengguanliang.com',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['biopython>=1.54'],

    entry_points={
        'console_scripts': [
            'msaconverter=msaconverter.msaconverter:main',
        ],
    },
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ),
)
