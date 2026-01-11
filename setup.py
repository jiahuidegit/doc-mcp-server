from setuptools import setup, find_packages

setup(
    name="doc-mcp-server",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
