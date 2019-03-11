import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bane",
    version="1.1",
    author="Ala Bouali",
    author_email="trap.leader.123@gmail.com",
    description="cyber security library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlaBouali/bane",
    packages=setuptools.find_packages(),
    python_requires=">=2.7",
    install_requires=['pexpect','paramiko','PySocks','requests','bs4','scapy','stem','MySQL-python'],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: Unix",
    ],
)
