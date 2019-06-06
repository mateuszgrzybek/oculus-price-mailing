# oculus-price-mailing
Python script for scraping and mailing price drops of Oculus Rift S headset from different sources.

## General app info
The application consists of two basic components:
1. Web-scraper - based on `BeautifulSoup4` and `requests` libraries. Uses functions defined in `functions.py`. Currently scrapes only the official oculus store and amazon.de.
2. Mailing module - function `send_prices` creates a secure connection with Gmail's SMTP server using Python's standard `smtplib` library, creates a multipart message, encrypts the attachment and sends the e-mail as specified.

## Installation
1. Clone this repository
2. Navigate to the root directory and run:
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
3. Open `venv/bin/activate` and add the following statements:
```
export OCULUS_PASS=put_your_app_specific_pass_here
export OCULUS_MAIL=put_your_email_here
```
`OCULUS_PASS` is the Gmail's application specific password aquired via your gmail account.  
`OCULUS_MAIL` is the sender's/receiver's e-mail address.

4. Deactivate and activate the virtualenv again
5. Run `python3 main.py` and let the script do it's work.
6. URLs and prices from each source are stored as `key:value` pairs in `prices.json`.

## Automation
For the purpose of automating the program, author has a set up cron job. In order to replicate it, first run:
```
chmod +x path/to/oculus-price-mailing/shell_automation.sh
```
The shell wrapper is now an executable.  
Now run `crontab -e` and add the following:
```
0 * * * * /absolute/path/to/oculus-price-mailing/shell_automation.sh >> /absolute/path/to/oculus-price-mailing/cron.log 2>&1
```
This will run the bash wrapper script every hour.  
Adjust the absolute paths so that they reflect the actual location of the repository on your local machine. You can also adjust the frequency of the cron job.
The `cron.log` will be created at first execution of the script. It's contents will be updated at each consecutive execution.
