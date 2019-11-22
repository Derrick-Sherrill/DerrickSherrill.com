'''
Video Tutorial:
https://youtu.be/Dq7yHiCjKrA

Description:
Automatically visit certain websites, wait so long, then close the tabs.
'''


import webbrowser
import time
from pykeyboard import PyKeyboard

count = 0
urls = ['https://pypi.org/project/pyobjc-framework-Quartz/','https://github.com/SavinaRoja/PyKeyboard','http://www.derricksherrill.com/django/multiple-database-query/']
k = PyKeyboard()

while count < 100:
    for url in urls:
        webbrowser.open(url, new=0)
        time.sleep(10)
        k.press_keys(['Command','W'])
        count = count + 1

else:
    pass
