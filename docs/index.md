---
layout: page
title: Medisana Weights
subtitle: This is where I will tell the world way too much about me
use-site-title: true
---

A colleague told me that he and his team had a common challenge. Lose weight as much as possible between April and December.

He told me that he was not yet able to do it, but was going to do everything to lose weight.

And that triggered me to participate.

I have had this Health site [40enfit.nl](https://www.40enfit.nl) for a long time ... actually it is still mine. But since my last post on that site I have not lived as healthily as I wanted.

Challenge accepted !!

## Medisana VitaDock and Scale

I've got this Medisana scale that uploads my data into the Medisana VitaDock Cloud. That environment had a API but that does not work anymore.

They still have the VitaDock online portal, but I wanted direct access to my own data.

At first the idea was to scrape the data out of my own personal pages on the VitaDock site. But after some digging I found out that they are filling the site with a JSON.

So I created a Python script that actually get's this data from the VitaDock Portal.

## Medisana Weights script

You can also easily grab your Medisana weight data with my script. The script can be found on my [github account](https://github.com/tvdsluijs/medisana_weights)

The only thing you need is a login to the VitaDock site and be able to run Python on your machine.

The json you get out of the python script is like this

`{"bodyWater": [{"bodyWater": 50.2, "muscleMass": 28.8, "mood": 0, "bmi": 0, "note": null, "activityStatus": 2, "y": 50.2,`

Trust me, there is more data, this is just part of the data.

You can find a complete data file on the [data]({{ site.baseurl }}/data) page

## How does it work

To get the data from the Medisana Vita Dock site I had to do some steps in order to get it.

In short my python script:
1. Goes to the login page to get a hidden secret key (the is regenerated every so many minutes)
2. Login to the page, together with the hidden secret key and data from some other hidden fields
3. Go to the weights page where the the data was beeing generated 
4. Go to the url where the actual data is (JSON Data)

Maybe there is an easier way... but I did not find it yet!

I use these urls to get to the data

- https://cloud.vitadock.com/signin
- https://cloud.vitadock.com/resources/j_spring_security_check
- https://cloud.vitadock.com/portal/target.php?lang=nl_NL
- https://cloud.vitadock.com/portal/server/target_server.php?lang=nl_NL&rnd=12345

To get to the data I use to libraries from pip

* requests
* BeautifulSoup
* pyyaml

You can install them easily by:

```bash
pip install requests
pip install beautifulsoup4
pip install pyyaml
```

With beautifulsoup I get the so called secret key from the signin page:

The field is called: `_csrf`

The other hidden fields grab and use to login are: 
- oauth_token
- marketingid
- code

Next to that use the normal field (username, password & button) to login into the j_spring_security_check page.

With all these pages I also grab the user cookie sessions with the code `requests.Session()`

Complicated..... YES! 
But I did all the work for you.

So just grab my [repository](https://github.com/tvdsluijs/medisana_weights) and 

`python medisana.py`

Oh... don't forget to create a config.yml file in the config folder with your login credentials. There is a sample file you can use.
