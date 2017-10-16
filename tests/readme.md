requires selenium to be installed in python (via pip)
requires gecko webdriver in path to control firefox

Front End testing

1) Unit tests first sets up self by instantiating web driver and getting homepage
2) tests homepage
3) tests welcome
4) tests Copyright
5) loops through each row in table (and checks name and email requirements) and accesses each user account page
5a) on each account page, run helper function and tests releveant requirements, including copyright

