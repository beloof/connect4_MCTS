from setuptools import setup, find_packages

setup(
    name="connect4_mcts",
    version="1.0.0",
    description="A Connect4 game implementation with MCTS AI players and tournament functionality",
    author="LASSIOUED Badis",
    url="https://github.com/beloof/connect4_MCTS",
    packages=find_packages(),
    install_requires=[
        "pygame",
        "numpy",
        "matplotlib",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
