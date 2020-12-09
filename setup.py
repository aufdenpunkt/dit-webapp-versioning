from setuptools import setup

setup(
    name="versioning",
    version="1.0.0",
    description="DIT Web-App Versioning",
    url="git@github.com:rfschubert/ptolemaios-sdk-package.git",
    author="Christian Schweinhardt",
    author_email="are.u.kidding@me.com",
    license="unlicense",
    zip_safe=False,
    packages=["versioning"],
    package_data={"versioning": ["versioning/*"]},
    include_package_data=True,
)
