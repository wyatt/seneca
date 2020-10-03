import setuptools

setuptools.setup(
    name='senecalearning',
    version='1.0.15',
    author="Wyatt Sell",
    author_email="wyatt@wyattsell.com",
    packages=["senecalearning"],
    install_requires=["requests"],
    license='MIT License',
    description='A small, unofficial python API for SenecaLearning',
    url="https://github.com/wyatt/seneca",
    long_description=open('README.md', encoding="utf8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
    ]
)