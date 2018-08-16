from setuptools import setup, find_packages


setup(name='magus',
      version='0.1',
      description='Damage calculation tool for MAGUS',
      url='http://github.com/miklosduma/magus',
      author='Miklos Duma',
      author_email='duma.miklos@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      entry_points={
            "console_scripts": [
                  "maggie=magus_kalkulator.interface:fire_up_interface"]})