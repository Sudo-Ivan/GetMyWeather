import setuptools

setuptools.setup(
    name="getmyweatherbot",  # Replace with the name of your bot
    version="1.0.0",
    author="Ivan",
    author_email="ivan@ivanryan.dev",
    description="Retrieves weather from openweather",
    url="https://github.com/Sudo-Ivan/GetMyWeather",  # Replace with the URL of your bot's repository
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
