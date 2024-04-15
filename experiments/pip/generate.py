import os
import subprocess

dumb = """def hello():
    print("Hello from my_package!")"""

def create_folder(folder_path):
    try:
        os.makedirs(folder_path)
    except OSError as e:
        print(f"Error: {e}")

def generate_file(path, content):
    try:
        with open(path, 'w') as file:
            file.write(content)
    except IOError as e:
        print(f"Error: {e}")

def generate(name, version, depends):
	raw = r"""
from setuptools import setup, find_packages

setup(
    name='{name}',
    version='{version}',
    packages=find_packages(),
    {depends}
)
"""
	raw = raw.replace(r"{name}", name)
	raw = raw.replace(r"{version}", version)
	if depends:
		raw = raw.replace(r"{depends}", f"install_requires={depends},")
	else:
		raw = raw.replace(r"{depends}", "")

	return raw

def generate_module(folder, name, version, depends):
	create_folder(folder)
	os.chdir(folder)
	generate_file("setup.py", generate(name, version, depends))
	create_folder(name)
	os.chdir(name)
	generate_file("__init__.py", "")
	generate_file("module.py", dumb)
	os.chdir("../")
	subprocess.run("python setup.py sdist upload -r local", shell=True, check=True)
	os.chdir("../")

def main():
	generate_module("foo_v1", "foo", "1.0", "")
	generate_module("foo_v2", "foo", "2.0", "['bar<2.0', 'baz<2.0']")
	generate_module("bar_v1", "bar", "1.0", "")
	generate_module("bar_v2", "bar", "2.0", "['foo<2.0', 'baz<2.0']")
	generate_module("baz_v1", "baz", "1.0", "")
	generate_module("baz_v2", "baz", "2.0", "['foo<2.0', 'bar<2.0']")

	generate_module("qux_v1", "qux", "1.0", "")
	generate_module("qux_v2", "qux", "2.0", "['a<2.0', 'b<2.0']")
	generate_module("a_v1", "a", "1.0", "")
	generate_module("a_v2", "a", "2.0", "['qux<2.0', 'b<2.0']")
	generate_module("b_v1", "b", "1.0", "")
	generate_module("b_v2", "b", "2.0", "['qux<2.0', 'a<2.0']")

	generate_module("c_v1", "c", "1.0", "")
	generate_module("c_v2", "c", "2.0", "['d<2.0', 'e<2.0']")
	generate_module("d_v1", "d", "1.0", "")
	generate_module("d_v2", "d", "2.0", "['c<2.0', 'e<2.0']")
	generate_module("e_v1", "e", "1.0", "")
	generate_module("e_v2", "e", "2.0", "['c<2.0', 'd<2.0']")

	generate_module("dumb", "dumb", "1.0", "['a<2.0', 'e<2.0']")

if __name__ == '__main__':
	main()


