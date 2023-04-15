# Maltego Web2Screenshot Transforms

The Maltego Web2Screenshot Transforms allow you to capture screenshots from both websites and URLs 
in a secure and anonymous manner. 

I developed these transforms to enhance my operational security 
(OPSEC) by avoiding exposing my public or VPN's IP address. With these Transforms, you can generate high-quality 
screenshots while keeping your identity and location hidden. 

To use the Maltego Web2Screenshot Transforms, simply obtain an API Key from API Flash's Free tier, which provides 100 
credits per month (1 credit per screenshot). 

Experience the power and convenience of the Web2Screenshot Transforms for your investigative needs.

## The Transforms

There are 8 available Transforms (4 per input type)

- **To Screenshot - Cache [API Flash]** : Retrieve a cached screenshot of a URL or Website, will consume 1 credit if not 
available in cache.
- **To Screenshot - Live [API Flash]** : Take a live screenshot from a URL or Website, will consume 1 credit.
- **To Screenshot XL - Cache [API Flash]** : Retrieve a cached full page screenshot from a URL or Website, will consume 1 
credit if not available in cache.
- **To Screenshot XL - Live [API Flash]** : Take a live full page screenshot from a URL or Website, will consume 1 credit.

## Capture Type

There are 2 capture types available.

1. **Live**: This will request a live screenshot from API Flash which will consume 1 credit.
2. **Cache**: This will check first if you have taken the screenshot for the specific input before, if available it will 
retrieve that copy without consuming credits, if not available, a live screenshot will be taken consuming 1 credit.

![credits.png](misc/credits.png)

After a screenshot is retrieved, you can visually distinguish between the live and cached captures by the overlay colors 

- **Green:** Live capture
- **Yellow:** Cache capture

## Capture Size

There are 2 capture sizes available, both cost 1 credit each.

1. **Standard**: This will take a screenshot of the target without scrolling down the page.
2. **XL**: This is a full page screenshot, API Flash will attempt to scroll down the page before saving the image.

Both Transforms will give you the option to open the image on your Browser, which can be found in the Detail View

![open_browser.png](misc/open_browser.png)

This would be specially useful for the XL screenshots.

![fullsite_browser.png](misc/fullsite_browser.png)

Zooming in will allow you to view the capture as if it was the original site's size.

## Installation

Install the required libraries by running

`pip install -r requirements.txt`

A Maltego configuration file **web2screenshot.mtz** can be automatically generated to easily import the Transforms and 
Transform Set into your client.

First you need to update your ENV file with your API Key and the Path to your Python Interpreter.

1. Open the project's directory "Maltego_Web2Screenshot".
2. Locate the **.env** file (Enable show Hidden files if using your OS explorer) and add your key and the path to 
your Python interpreter without spaces.

![interpreter.png](misc%2Finterpreter.png)

Now we are ready to generate the web2screenshot.mtz configuration file

1. Open your Terminal and go to your project's main directory.
2. Run `python3 project.py list`

![project.png](misc%2Fproject.png)

That's all you need, you should now have the new configuration file inside your project.

![conf_file.png](misc%2Fconf_file.png)

Simply import the file into your client by going to Import | Export > Import Config > Select mtz file.

![import.png](misc/import.png)

Your new configuration file includes a Transform set called "Web2Screenshot" which will arrange your new Transforms into a 
submenu, making them easier to find and use.

If you are a more advanced user and want to manually add the Transforms to your client, you can follow this 
[instructions](https://docs.maltego.com/support/solutions/articles/15000017605-local-transforms-example-#adding-the-transform-to-maltego-0-6)

**Note:** At the time of writing the Transforms I noticed the URL Entity's property that hold the url has changed it's 
unique name from url to theurl, if you don't get any results when running the URL to Screenshot Transforms could be due 
that change.

To fix this issue you can try refreshing your client or simply change the property name called **input_url** inside the 
Transforms (it's below the line where you added your API Key)

Happy OSINTing!