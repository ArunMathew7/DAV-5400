from setuptools import setup

setup(
    name="analysis_Packages",
    version=0.1,
    description="Analysis of death by selected causes from 2014 to 2019",
    author="Arun Mathew",
    packages=["data_summary", "EDA", "inference"],
    zip_safe=False,
)
