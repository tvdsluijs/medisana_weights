---
layout: page
title: Medisana Weights
subtitle: This is where I will tell the world way too much about me
use-site-title: true
---

A colleague told me that they and their team had a common challenge. Lose weight as much as possible between April and December.

He told me that he was not yet able to do it, but was going to do everything to lose weight.

And that triggered me to participate.

I have had this Health site [40enfit.nl](https://www.40enfit.nl) for a long time ... actually it is still mine. But since my last post on that site I have not lived as healthily as I wanted.

Challenge accepted !!

## Medisana VitaDock and Scale

I've got this medisana scale that uploads my data into the Medisana VitaDock Cloud. That environment had a API but that does not work anymore.

They still have the VitaDock online portal, but I wanted direct access to my own data.

So I created a Python script that actually get's this data from the VitaDock Portal.

## Medisana Weights script

You can get the data also with my free to use script. The script can be found on my [github account](https://github.com/tvdsluijs/medisana_weights)

The only thing you need is a login to the VitaDock site and be able to run Python on your machine.

The json you get out of the python script is like this

`{"bodyWater": [{"bodyWater": 50.2, "muscleMass": 28.8, "mood": 0, "bmi": 0, "note": null, "activityStatus": 2, "y": 50.2,`

Trust me, there is more data, this is just part of the data.

You can find a complete data file on the [data](/medisana_weights/data) page


**Here is some bold text**

## Here is a secondary heading

Here's a useless table:

| Number | Next number | Previous number |
| :------ |:--- | :--- |
| Five | Six | Four |
| Ten | Eleven | Nine |
| Seven | Eight | Six |
| Two | Three | One |


How about a yummy crepe?

![Crepe](https://s3-media3.fl.yelpcdn.com/bphoto/cQ1Yoa75m2yUFFbY2xwuqw/348s.jpg)

Here's a code chunk:

~~~
var foo = function(x) {
  return(x + 5);
}
foo(3)
~~~

And here is the same code with syntax highlighting:

```javascript
var foo = function(x) {
  return(x + 5);
}
foo(3)
```

And here is the same code yet again but with line numbers:

{% highlight javascript linenos %}
var foo = function(x) {
  return(x + 5);
}
foo(3)
{% endhighlight %}

## Boxes
You can add notification, warning and error boxes like this:

### Notification

{: .box-note}
**Note:** This is a notification box.

### Warning

{: .box-warning}
**Warning:** This is a warning box.

### Error

{: .box-error}
**Error:** This is an error box.
