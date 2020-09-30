import setuptools

setuptools.setup(
    name='seneca',
    version='1.0.7',
    author="Wyatt Sell",
    author_email="wyatt@wyattsell.com",
    packages=["seneca"],
    install_requires=["requests"],
    license='MIT License',
    description='A small, unofficial python API for SenecaLearning',
    url="https://github.com/wyatt/seneca",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
    ]
)