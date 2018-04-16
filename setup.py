import setuptools

setuptools.setup(
    name="mn_topo",
    version="0.1.0",
    url="https://github.com/luminanetworks/mn_topo",

    author="Lumina NetDev",
    author_email="dev@luminanetworks.com",

    description="Mininet specific topology generator",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=['click', 'topology'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    entry_points='''
        [topology.plugins]
        mininet=mn_topo.cli:mininet
    ''',
)
