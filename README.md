Take a Twitter list and convert it to a CSV

## Getting started

1. Clone this repo and set up a virtualenv
1. `pip install tweepy`
1. Go out to [Twitter](https://apps.twitter.com/) and get you some API keys
1. Make a file called `config.py` using the `example-config.py` as a template and add your API keys
1. Run `python list.py`
1. Plug in a Twitter list URL when prompted
1. Enjoy that beautiful CSV of Twitter list data goodness

## Notes

* I've included an example CSV from [this NICAR list](https://twitter.com/HeatherSaidTHAT/lists/nicar-speakers-2014) to prove that it can be done
* If you want to get different info than what I'm providing you can see what else is available from the [Twitter API here](https://dev.twitter.com/rest/reference/get/lists/members)
* This basic template should be extendable for different types of Twitter API things

## Links and such

* [Tweepy](http://tweepy.readthedocs.io/en/v3.5.0/getting_started.html)
* [Twitter API docs](https://dev.twitter.com/rest/public)

