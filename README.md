# CovInsta!
The CovInsta is a robot that posts the latest statistics of Covid to Instagram! Here is a sample post: https://www.instagram.com/p/CGwPLHDFquU/

## Requirements
CovInsta is compatible with Windows 10.
This program uses Selenium package, which needs Chrome browswer to be installed and the version of "chromedriver.exe" file must match the version of your chrome. The version that is used here is **ChromeDriver 86.0.4240.22**. Please download the proper version at: https://chromedriver.chromium.org/downloads

The following packages are also used in this project:
- selenium
- string
- time
- datetime
- re
- instapy
- autoit
- pathlib
- numpy
- shutil
- csv
- PIL
- matplotlib


## How to run
For running this program, you need to run **NewPost.py**. Before that, open this file and scroll down to the last two lines of the program. 

```python
copyfile('stat.png', 'c://Users/Masoud/stat.png')
newPost('isuhack','isu123',"#hackathon #IowaStateUniversity #Covid")
```

You need to change the word **Masoud** with your Windows user account.
In the last line, **newPost()** gets three parameters that are your Instagram username, password, and the comments for the new post.
The best way to use this program is to schedule **batch.bat** to be run daily.

## How CovInsta works?
This program scrapes the websites that contain the statistics of Covid, then stores them locally and creates visualizations. Then, it simulates a mobile device in order to send a new post to instagram which contains the visualizations.

## What's next?
In the next step, CovInsta will do further analysis on the records and try to make short-term predictions using LSTM classifier.
