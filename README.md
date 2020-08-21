# Snahp.it Downloader
A python script to download files from snahp.it in batch.

## Requirements
- [ChromeDriver](https://chromedriver.chromium.org/)
- [aria2](https://aria2.github.io/)

## Installation
#### 1. Clone repository:
    git clone https://github.com/Jwiggiff/snahp-downloader.git
#### 2. Install requirements
    pip install -r requirements.txt

## Usage
#### Help command:
    python downloader.py --help

## Examples
#### Download links in `links.txt`
    python downloader.py links.txt
#### Download links in `links.txt` to `output` directory
    python downloader.py -o "output" links.txt
#### Download links in `links.txt` to `output` directory in batches of 10
    python downloader.py -o "output" -n 10 links.txt
