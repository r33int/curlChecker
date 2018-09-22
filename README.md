# curlChecker

This is a simple python script that checks URLs's availibility on a specified file, using pycurl, and writes the successful ones to a file. This thing was made for a friend, and the code might be a total mess, but it seems to work...

It currently supports:

 - Username & password authentification
 - Configure verbose and timeout delay

Also, don't expect a lot of support for this, this is a very small project.

 ## Usage
First, install the requirements:
```` 
pip install requirements.txt
````
Edit the config file to your convenience:
````
*your favourite editor* config.ini
````
Your input file must contain the URLs line by line. Example:
````
https://google.com
https://github.com
````
Make sure your input and output files exists, then run the script:
````
python curlChecker.py -i input.txt -o output.txt
````