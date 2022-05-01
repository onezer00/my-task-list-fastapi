from setuptools import find_packages, setup
import load_envs

from os import getenv

load_envs.load()

last_updated = None

packages = [
    "pytest<7,>=5",
    "pytest-timeout",
]

setup(
    name="python-task-list",
    version=getenv("VERSION", "FALILED TO LOAD VERSION"),
    author="Oner",
    author_email="caimbebr@gmail.com",
    description='A simple task list with fastapi',
    packages=find_packages(),
    python_requires=">=3.5",
    include_package_data=True,
    zip_safe=False,
    install_requires=packages + ["wheel", "setuptools"],
    setup_requires=["pytest-runner"],
    tests_require=packages,
)
