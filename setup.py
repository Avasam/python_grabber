from setuptools import setup

setup(name='pygrabber',
      version='0.1',
      description='Module for grabbing live video images using DirectShow',
      long_description='Module for grabbing live video images using DirectShow',
      url='https://github.com/andreaschiavinato/python_grabber',
      author='andreaschiavinato',
      author_email='',
      license='MIT',
      packages=['pygrabber'],
      package_data={"pygrabber": ["py.typed"]},
      install_requires=[
          "comtypes>=1.1.7",
          "numpy>=1.17.3"
      ],
      zip_safe=False)
