from setuptools import setup, find_packages

setup(
    name="simple-flask-app",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "simple-flask-app=app.main:main",
        ],
    },
)
