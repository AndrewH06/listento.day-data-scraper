# ListenTo.day: Data Scraper

The [CSV File](https://github.com/Currie32/500-Greatest-Albums/blob/master/albumlist.csv) based on the [Rolling Stone's The 500 Greatest Albums of All Time](https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/) used for [ListenTo.day](https://listento.day) didn't contain all the data needed for the website.

Using [Pandas](https://pandas.pydata.org) and the [Spotipy library](https://spotipy.readthedocs.io/en/2.21.0/), I created a way to search and add the necessary data.

The [python file](https://github.com/AndrewH06/listento.day-data-scraper/blob/master/main.py) updates [data.csv](https://github.com/AndrewH06/listento.day-data-scraper/blob/master/data.csv) with additional columns containing data for the `image` and `link` for each album.

> Note: Some albums are not on Spotify, that data was manually added.
