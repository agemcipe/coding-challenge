import setuptools

setuptools.setup(
    name="coding_challenge",
    version="0.1",
    author="Jonathan Haas",
    author_email="jonathan.haas.ger@gmail.com",
    description="",
    url="https://github.com/agemcipe/coding_challenge",
    setup_requires=["setuptools_scm"],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
)
