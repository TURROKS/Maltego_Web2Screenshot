# Maltego Web2Screenshot Transforms

The Maltego Web2Screenshot Transforms allow you to generate screenshots from both Websites and URLS.

To use these Transforms you will need an API Key from [API Flash](https://apiflash.com/) they have a Free tier that
gives you 100 Credits per month (1 credit per screenshot).

## The Transforms

There are 4 available Transforms (8 total 1 per Entity type)

- **To Screenshot - Cache [API Flash]** : Take a cache screenshot from a URL or Website, will consume 1 credit if not 
available in cache.
- **To Screenshot - Live [API Flash]** : Take a live screenshot from a URL or Website, will consume 1 credit.
- **To Screenshot XL - Cache [API Flash]** : Take a cache full page screenshot from a URL or Website, will consume 1 
credit if not available in cache.
- **To Screenshot XL - Live [API Flash]** : Take a live full page screenshot from a URL or Website, will consume 1 credit.

## Capture Type

There are Capture Types for each Transform.

- **Live**: This will request a live screenshot from API Flash which will consume 1 credit.
- **Cache**: This will check first if you have taken the screenshot for the specific input before, if available it will 
retrieve that copy without consuming credits, if not available, a live screenshot will be taken consuming 1 credit.

![credits.png](misc/credits.png)

## Capture Size

There are 2 Capture Sizes for each Transform, both consume only 1 credit.

- **Standard**: This will take a screenshot of the target without scrolling down the page.
- **XL**: This is a full page screenshot, API Flash will scroll down the page before saving the image.

Both Transforms will give you the option to open the image on your Browser; this option can be found in the Detail View

![open_browser.png](misc/open_browser.png)

This would be specially useful for the XL screenshots.

![fullsite_browser.png](misc/fullsite_browser.png)

## Installation

A Maltego configuration file **Web2ScreenshotTransforms.mtz** has been included under the misc folder, you can simply 
import the file into your client by going to Import | Export > Import Config > Select mtz file.

![import.png](misc/import.png)

Once the file has been imported, you will need to update the Command line and Working directory paths for the new 
Transforms.

Go to the Transforms Tab and follow the below steps for each Transform

1. Click Transform Manager
2. Search for Flash
3. Select one Transform at a time to perform step 4
4. Update the following fields
   - Command line: Path to your Python interpreter
   - Working directory: Path to this repository in your machine (should include the folder name) e.g. 
   TURROKS/Documents/Maltego_Web2Screenshot

![Configurations.png](misc/Configurations.png)

Finally, you will need to manually add your API Key to the Transforms. Simply locate the Transform under the transforms
folder, open the file and add your key.

![api_keys.png](misc/api_keys.png)

If you are a more advanced user and want to manually add the Transforms to your client, you can follow this 
[instructions](https://docs.maltego.com/support/solutions/articles/15000017605-local-transforms-example-#adding-the-transform-to-maltego-0-6)