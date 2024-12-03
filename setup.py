from setuptools import setup, find_packages

setup(
    name="finances",
    version="1.0.0",
    description="A personal finance management backend for transactions, accounts, and investments.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="João Marcus, Almir Sérgio",
    author_email="joaosenareis@gmail.com, almirsergio.a@gmail.com",
    url="https://github.com/seuusuario/finances",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "pytest>=7.0.0"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    keywords="finance, transactions, investments, accounts",
    project_urls={
        "Source": "https://github.com/seuusuario/finances",
        "Bug Tracker": "https://github.com/seuusuario/finances/issues",
    },
)
