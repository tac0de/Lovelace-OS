from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="lovelace_os",
    version="0.0.1",
    author="Wonyoung Choi",
    description="Minimal ethical terminal-based OS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "lovelace_os=main:main",
        ],
    },
    python_requires=">=3.7",
    license="MIT",
    include_package_data=True,
    zip_safe=False,
)

