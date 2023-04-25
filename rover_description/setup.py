import os
from glob import glob
from setuptools import setup

package_name = 'rover_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='devcon',
    maintainer_email='devcon@admantium.com',
    description='Simulation of the RADU robot',
    license='UNLICENSED',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'spawn_rover = rover_description.spawn:main',
        ],
    },
)

