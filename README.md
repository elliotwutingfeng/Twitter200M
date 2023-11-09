# Twitter200M

[![GitHub license](https://img.shields.io/badge/LICENSE-BSD--3--CLAUSE-GREEN?style=for-the-badge)](LICENSE)

Simple analysis of the [Twitter 200M Data Dump](https://haveibeenpwned.com/PwnedWebsites#Twitter200M) of January 2023.

Download links for the data dump are **not** included in this repository.

## Background

Quote from haveibeenpwned.com,

> In early 2023, over 200M records scraped from Twitter appeared on a popular hacking forum. The data was obtained sometime in 2021 by abusing an API that enabled email addresses to be resolved to Twitter profiles. The subsequent results were then composed into a corpus of data containing email addresses alongside public Twitter profile information including names, usernames and follower counts.

The data dump analysed in this repository is a "cleaned-up" version by a user on the aforementioned forum.

## Findings

### Caveats

- Not all user accounts have been leaked; Twitter has much more than 200 million accounts.
- It is impossible to verify that the leaked datasets have not been tampered with falsified data.

The following findings are made on the assumption that this dataset is representative of Twitter's actual userbase.

### Most popular email providers

```bash
┌────────────────┬─────────────────┐
│ Email Provider ┆ Number of Users │
│ ---            ┆ ---             │
│ str            ┆ i64             │
╞════════════════╪═════════════════╡
│ gmail.com      ┆ 73314131        │
│ hotmail.com    ┆ 40509492        │
│ yahoo.com      ┆ 33051713        │
│ aol.com        ┆ 4025882         │
│ hotmail.co.uk  ┆ 3298152         │
│ mail.ru        ┆ 3289923         │
│ hotmail.fr     ┆ 3128568         │
│ live.com       ┆ 1945940         │
│ msn.com        ┆ 1321923         │
│ yahoo.co.uk    ┆ 1313553         │
│ yahoo.fr       ┆ 1245996         │
│ ymail.com      ┆ 1142144         │
│ yandex.ru      ┆ 1125810         │
│ icloud.com     ┆ 1093533         │
│ comcast.net    ┆ 1091726         │
└────────────────┴─────────────────┘
```

Over **75%** of Twitter users use either Google, Microsoft, or Yahoo email addresses.

### Account creation times

Twitter first experienced rapid user growth in 2009, with its highest new account signup rates from 2011 to 2013.

From 2016 onwards, new account signups dipped below 2009 levels, and have been on a constant decline ever since.

## Requirements

Tested on Linux x64

- Fast multicore CPU
- At least 64 GB RAM
- Python 3.11
- [7zip](https://7-zip.org)

## Setup

```shell
pip3 install -r requirements.txt
```

## Formatting

```shell
black .
```
