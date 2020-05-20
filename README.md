# Typeform bot -- Lioness giveaway
Simple bot using Selenium webdriver to fill out typeform fields (for a clothing site giveaway).
Also implemented a simple parallel process using `joblib` dependency to multiply number of browsers open.

* still need to implement error handling and see if parallelization can be more efficient

## Usage
In order to use, first download [chromedriver](https://chromedriver.chromium.org/downloads).

Then, run the following commands to install required dependencies.
```
$ pip install selenium
$ pip install joblib
```

Run this program with no arguments.
```
$ python automate.py
```
