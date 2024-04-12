#!/usr/bin/env python3
import sys

import polars as pl


def main(filename):
    with open(filename, "rb") as f, pl.Config(tbl_cols=-1, tbl_rows=-1):
        df = pl.read_excel(f, sheet_id=0)
        for k, v in df.items():
            v = v.with_columns([pl.col(column).cast(pl.Utf8) for column in v.columns])
            v = v.with_columns([pl.col(column).fill_null("") for column in v.columns])

            print("Table Name:", k)
            print(v)


if __name__ == "__main__":
    main(sys.argv[1])
