# CovInsta!
The CovInsta is a robot that posts the latest statistics of Covid to Instagram!

## Requirements
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
For running this program, you need to execute **NewPost.py**. Before that, open this file and scroll down to the end of the file:
```python
[total_cases, total_death, total_recovered, stat_per_country] = getStat(30)
SaveToCSV(total_cases, total_death, total_recovered)
AddPlot()
createImage(total_cases, total_death, total_recovered, stat_per_country)
copyfile('stat.png', 'c://Users/Masoud/stat.png')
newPost('isuhack','isu123',"#hackathon #IowaStateUniversity #Covid")
```
