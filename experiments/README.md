# How to reproduce the experiment

## conda part

### Environment Setup

-   prerequisite
    -   conda version used by me: 23.3.1
-   create a new environment
    -   `conda create --name test-env`
    -   `conda activate test-env`
-   create fake packages
    -   under conda folder, there is a `generate.py` file that is used to quickly generate fake packages with desired dependency relationship.
    -   Anaconda has a nice feature that after the dependencies has been resolved, it will stop and ask you if you want to install the package. So we do not need to create real package content, just modify the repodata.json and we can fool anaconda to resolve the dependency
    -   find your repodata.json used by anaconda when installing local packages. This might be under `~/anaconda3/conda-bld/noarch`.
    -   **WARMING: make a backup of your repodata.json if you have something important inside it**
    -   run `python3 generate.py > ~/anaconda3/conda-bld/noarch/repodata.json`, replace the destination if your repodata is at different location

### Perform experiment

-   play with `conda install --use-local` to see what it outputs
    -   example: `conda install --use-local foo bar baz qux a b c d e`
-   You can also modify the dependency relationship in `generate.py` to see how anaconda behaves

## pip part

### Environment Setup

-   prerequisite
    -   pip version used by me: 24.0
    -   have **devpi** started on your local machine
        -   [tutorial here](https://www.devpi.net/)
-   create a new environment
    -   `python -m venv .venv`
    -   `source .venv/bin/activate`
-   install setuptools
    -   `pip3 install setuptools`
-   create fake packages
    -   under pip folder, there is a `generate.py` file that is used to quickly generate fake packages with desired dependency relationship.
    -   run `python3 generate.py`

### Perform experiment

-   play with `pip install -i http://localhost:8080` to see what it outputs
    -   example: `pip install -i http://localhost:8080 foo bar baz qux a b c d e`
-   You can also modify the dependency relationship in `generate.py` to see how pip behaves
