from distutils.core import setup
setup(
	name='pyprofyler',
	version='1.0.0',
	author='Aly Shmahell',
	author_email='aly.shmahell@gmail.com',
	description='a simple memory profiler for python programs.',
	packages=['pyprofyler'],
	install_requires=[
			  "psutil==5.6.1",
			  "cython==0.29.6",
			  "numpy==1.16.2"
			],
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)