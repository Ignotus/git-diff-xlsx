# git-diff-xlsx

Implements git diff for the XLSX format.


### Setup

1. ``pip3 install -r requirements.txt``
2. Add ``*.xlsx diff=xlsx`` .gitattributes.
3. ``git config diff.xlsx.textconv <path-to-xlsx2txt>``
4. ``git diff``


### License

MIT
