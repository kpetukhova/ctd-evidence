# CTD evidence script

Prepare evidence for CTD in format `<short_commit_id>-<commit_name>.diff`.

```
optional arguments:
  -h, --help            show this help message and exit
  --name NAME           Your github username
  --start_date START_DATE
                        Start date. Default: 21st of previous month.
  --end_date END_DATE   End date. Default: today's date
  --outdir OUTDIR       Output directory.
```

# How to use

Copy `ctd_format.py` to repository of interest and run:

```
python ctd_format.py --name <your github username>
```
e.g.

```
python ctd_format.py --name "Ksenia Petukhova"
```

By default, evidence files will be saved to "CTD_evidencies/<start_date>_<end_date>" folder.