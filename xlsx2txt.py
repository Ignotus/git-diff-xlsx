#!/usr/bin/env python3
import sys
from zipfile import ZipFile
from lxml import etree


def extract_zip(input_zip):
    input_zip=ZipFile(input_zip)
    return {name: input_zip.read(name) for name in input_zip.namelist()}


def main(filename):
    data = extract_zip(filename)
    for f, value in data.items():
        root = etree.fromstring(value)
        print(etree.tostring(root, pretty_print=True).decode())


if __name__ == "__main__":
    main(sys.argv[1])
