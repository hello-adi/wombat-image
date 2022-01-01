# wombat-image
Wombat image scrapes certain webistes for images of Wombats and downloads them to the computer. It utilises multiple threads to download multiple images at once.

## Introduction
Wombat-image scrapes Unsplash.com using BeautifulSoup4 for images of wombats and downloads them to the computer using Wget. Since downloading is an I/O heavy process which involves communication between the computer and the server where the images are hosted, downloading each image after another can take some time. Therefore, utilising a ThreadPool can speed up the process. In one of the trial runs, downloading 8 images without using multiple threads took 200s while it only took 8s when utilising multiple threads.

## Inspiration
Training an A.I model to recognize certain images requires compiling a large data set of images. Sequentially downloading thousands or more images would be quite tedious and require a lot of waiting time. As a result, Multithreading can be used to optimize the tast and make it quicker.
The images are renamed and stored in a user-defined directory.

## Requirements
Project uses:
* Python version: 3.8.10
* Requests version: 2.22.0
* BeautifulSoup4 version: 4.8.2
* Wget version: 3.2
	
## Installing on local machine
The application uses BeautifulSoup, Requests and Wget which are not availible in the standard python library, therefore they must be downloaded using [pip](https://pip.pypa.io/en/stable/). 

``` bash
pip install beautifulsoup4
pip install requests
pip install wget
```

## Using Wombat-image
The application does not require any special inputs. Simply running it will download the scraped images into the file directory. 

## Future Scope
As of now, the project is hardcoded to search for wombat images. I believe in the future it can be modified or optimized to take the search key word from the user and then scrape the website based on the query made by the user.
