#Memes API
## Because why not

*By [@regenhans](http://twitter.com/regenhans)*

This is a quick project that came out of a [twitter conversation](https://twitter.com/grafofilia/status/834113438381121536) 

... And a couple hours of leisure time


I hope [@escusado](http://twitter.com/escusado) **se ponga chido** and uses it for [his project](https://github.com/escusado/console.meme) .

I scrap the data from all the pages on [http://knowyourmeme.com/memes/popular](http://knowyourmeme.com/memes/popular).


##How it works?

Well, first of all you need to build it on your own server or local machine (I really don't have money to maintain this shit).

I used the following python libs:

- beautiful soup
- pymongo
- tqdm
- python eve

### Scraping the data

First you need to have installed mongoDB in order to store the data and create a db called "memes" (you can name it whatever you want in fact).

Next just run

``` 
> python scraper.py
```

When the scraper finish its magic you can go to the next part.

### Running the API server

Go to the api folder and run

``` 
> python run.py
```

Profit.

Of course this is just for runing on your local machine but you may want to modify it to run on your fancy AWS instance or heroku.


###Consulting the API

To get a random meme just go to:

```
yoururl/popular?where={"memeid": *A random number between 1 and 10320*}
> python run.py
```


