import json 

def generate(packages, name, version, depends):
    packages[f"{name}-{version}-0.tar.bz2"] = {
        "build": "0",
        "build_number": 0,
        "depends": depends,
        "license": "MIT",
        "md5": "01aec23216fa8f6731e5a1c7e07743cd",
        "name": name,
        "noarch": "generic",
        "sha256": "b6298acc2a1a03b5df97c27eb6692e3145c3193141751ad7461492d211e9efd5",
        "size": 5512,
        "subdir": "noarch",
        "timestamp": 1711774913896,
        "version": version
    }
    return packages

packages = {}
packages = generate(packages, "foo", "1.0", ["python"])
packages = generate(packages, "foo", "2.0", ["python", "bar <2.0", "baz <2.0"])

packages = generate(packages, "bar", "1.0", ["python"])
packages = generate(packages, "bar", "2.0", ["python", "foo <2.0", "baz <2.0"])

packages = generate(packages, "baz", "1.0", ["python"])
packages = generate(packages, "baz", "2.0", ["python", "foo <2.0", "bar <2.0"])

packages = generate(packages, "qux", "1.0", ["python"])
packages = generate(packages, "qux", "2.0", ["python", "a <2.0", "b <2.0"])

packages = generate(packages, "a", "1.0", ["python"])
packages = generate(packages, "a", "2.0", ["python", "b <2.0", "qux <2.0"])

packages = generate(packages, "b", "1.0", ["python"])
packages = generate(packages, "b", "2.0", ["python", "a <2.0", "qux <2.0"])

packages = generate(packages, "c", "1.0", ["python"])
packages = generate(packages, "c", "2.0", ["python", "d <2.0", "e <2.0"])

packages = generate(packages, "d", "1.0", ["python"])
packages = generate(packages, "d", "2.0", ["python", "c <2.0", "e <2.0"])

packages = generate(packages, "e", "1.0", ["python"])
packages = generate(packages, "e", "2.0", ["python", "c <2.0", "d <2.0"])

packages = generate(packages, "dumb", "1.0", ["python", "a <2.0", "foo <2.0"])

root = {
    "info": {
        "subdir": "noarch"
    },
    "packages": packages,
    "packages.conda": {},
    "removed": [],
    "repodata_version": 1
}

with open("output.json", "w") as outfile: 
    json.dump(root, outfile)