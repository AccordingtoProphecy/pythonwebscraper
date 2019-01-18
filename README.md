This code is based heavily off of Henry McCreery's code from his Github page.
I typed out all the code in order to understand it better, tweak it to my liking, and to make it my own.
There are 4 options, also heavily influenced from Henry's code. The options are the URL of the page, the interval between the checks, the actual number of checks, and whether you want to cancel the process after a successful check. It only checks for changes in the website.
It works with my information, and, though I haven't tested it with anyone else's, it should work given they input their information into a separate file.
In order for this to work, you need to have your Twilio information available and create a Variables.py file containing the URL of the website you want to scrape, your Twilio account SID, authentification token, Twilio phone number, and the number you want Twilio to text.
