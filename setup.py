from setuptools import find_packages, setup


packages = [
    "pytest<7,>=5",
    "pytest-timeout",
]

setup(
    name="python-task-list",
    version="1.0.1",
    author="Oner",
    author_email="caimbebr@gmail.com",
    packages=find_packages(),
    python_requires=">=3.5",
    include_package_data=True,
    zip_safe=False,
    install_requires=packages + ["wheel", "setuptools"],
    setup_requires=["pytest-runner"],
    tests_require=packages,
)
