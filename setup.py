import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="getmyweatherbot",  # Replace with the name of your bot
    version="1.0.0",
    author="Ivan",
    author_email="ivan@ivanryan.dev",
    description="Retrieves weather from openweather",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sudo-Ivan/GetMyWeather",  # Replace with the URL of your bot's repository
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
