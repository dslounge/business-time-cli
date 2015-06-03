# business-time-cli

This is an elegant business-time cli for a more civilized age, writen in Python. For more information, visit https://github.com/trisweb/business-time

### Installation

1. Make sure you have the python `pyyaml` module installed. You might want to do this with (or however you want, I'm not your boss):

```
sudo easy_install pip
sudo pip install pyyaml
```

2. Clone this repo

3. Copy `config.yml.sample` to `config.yml` and edit the `api-url` key to point to the business-time url

4. Make sure it's executable by running `chmod u+x business-time.py`

### Use

`./business-time.py` - show status of all bathrooms

`./business-time.py men` - show status of men's bathrooms

`./business-time.py women` - works, but doesn't really tell you anything useful as of 6/3/2015 since sensors aren't installed

