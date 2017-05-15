# Python image scrapper

Python image scrapper is simple script to download images from groups on Facebook.

## Getting Started

This is just a demo app. This could be done a lot easier and better. Actually, this is my first python script ever written.

### Installing & using

What do you need to play with this?

Download awesome script from  - [**minimaxir**](https://github.com/minimaxir/facebook-page-post-scraper)

```
facebook-page-post-scraper
```

Fill with data ( ID, APP secret and page name ), put it in same folder and run script:

```
python get_fb_posts_fb_page.py
```

After some time you will end with .csv file.

Create folder **images** in project root.

Rename file .csv file to .txt and change inside index.py line **7**.

```
with open('__YOUR_FILE_NAME.txt__') as f:
```

Run script:

```
python index.py
```

Check folder **images** for images. 

## Authors

* **Valentino Kožinec** - [vkozinec](https://github.com/vkozinec)

## License

This project is licensed under the MIT License

## Acknowledgments

* Thanks to [**minimaxir**](https://github.com/minimaxir/) for awesome code, check his github.