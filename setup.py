from setuptools import setup, find_packages

setup(
    name="n_queens_solver",
    version="0.1",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "numpy",
        "pygame",
    ],
    python_requires=">=3.8",
)