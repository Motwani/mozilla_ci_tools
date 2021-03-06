from setuptools import setup, find_packages

setup(
    name='mozci',
    version=' .dev0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mozci-trigger = mozci.scripts.trigger:main'
        ],
    },
    install_requires=[
        'buildapi_client>=0.2.2',
        'ijson>=2.2',
        'keyring>=5.3',
        'progressbar>=2.3',
        'pushlog_client>=0.5.0',
        'requests>=2.8.1',
        'taskcluster>=0.0.28',
        'treeherder-client>=2.0.1',
        'jsonschema>=2.5.1'
    ],

    # Meta-data for upload to PyPI
    author='Armen Zambrano G.',
    author_email='armenzg@mozilla.com',
    description="It is a commandline client and python library to interact with \
                 Mozilla's Buildbot CI (and TaskCluster in the future). \
                 It simplifies and unifies querying and triggering jobs.",
    license='MPL',
    url='https://github.com/mozilla/mozilla_ci_tools',
)
