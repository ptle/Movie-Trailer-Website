# Movie-Trailer-Website

**Movie-Trailer-Website** is a movie trailer application in Python

Submitted by: **Peter Le**

## Functionality

The following **required** functionality is complete:
* [x] Page is dynamically generated from Python data structure (media.py)
* [x] Page is full of favorite movie images
* [x] When image is clicked on trailer appears

The following **optional** features are implemented:
* [x] Used API call to help populate data (images and plot)

## Video Walkthrough

Here's a walkthrough of functionality:

<img src='http://i.imgur.com/XFG9ITz.gif' title='Video Walkthrough' width='' alt='Video Walkthrough' />

GIF created with [LiceCap](http://www.cockos.com/licecap/).

## How to run
1. Make sure Python is downloaded. If not downloaded, go to https://www.python.org/downloads/ to download
2. Download entertainment_center.py, fresh_tomatoes.py, and media.py
3. Make sure all files are in same folder location **Note: WIll NOT WORK IF FILES ARE NOT IN SAME FOLDER**
4. Run entertainment_center.py (command: "python entertainment_center.py")

## Notes

Implements The Open Movie Database API call. Some limitations are that if movies are incorrectly
spelled then the data will not properly populate. Also right now this implementation only uses
six of my favorite movies. If you want to change the data you must change the favorite_movie_names
and trailers lists accordingly. **MAKE SURE THESE LISTS ARE THE SAME SIZE OR ERRORS WILL OCCUR**
