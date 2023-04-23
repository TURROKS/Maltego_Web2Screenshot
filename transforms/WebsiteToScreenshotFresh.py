from datetime import datetime as dt
import os
from urllib import parse

from dotenv import load_dotenv
import requests

from extensions import registry, web2screenshot_set
from maltego_trx.maltego import MaltegoMsg, MaltegoTransform, UIM_FATAL, UIM_PARTIAL
from maltego_trx.transform import DiscoverableTransform
from maltego_trx.overlays import OverlayType, OverlayPosition

# Load Environment Variables
load_dotenv()


def api_handler(api_url, target_url, api, custom_agent):

    data = requests.get(api_url+f"?access_key={api}&url=https://{target_url}&fresh=true&user_agent={custom_agent}")

    return data


def api_info(api):

    data = requests.get(f"https://api.apiflash.com/v1/urltoimage/quota?access_key={api}")
    parsed = data.json()

    if data.status_code == 200:
        return parsed


@registry.register_transform(display_name="To Screenshot - Live [API Flash]", input_entity="maltego.Website",
                             description='Take a live screenshot from an Website, will consume 1 credit.',
                             output_entities=["maltego.Image"],
                             transform_set=web2screenshot_set)
class WebsiteToScreenshotFresh(DiscoverableTransform):

    @classmethod
    def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):
        # Access Environment Variables
        api_key = os.getenv("API_KEY")
        user_agent = os.getenv("USER_AGENT")
        api_baseurl = os.getenv("API_URL")

        input_url = request.Value
        clean_url = parse.quote_plus(input_url)

        screenshot = api_handler(api_url=api_baseurl, target_url=clean_url, api=api_key, custom_agent=user_agent)

        if screenshot.status_code == 200:
            api_check = api_info(api=api_key)

            if screenshot:
                ent = response.addEntity("maltego.Image", str(input_url).lower())
                ent.addProperty("url", "URL", "strict", screenshot.url)
                ent.addDisplayInformation(content=f'<a href="{screenshot.url}">Open in Browser</a>', title="Screenshot")
                ent.addProperty(fieldName="captureType", displayName="Capture Type", matchingRule='strict', value="Live")
                ent.addProperty(fieldName="captureSize", displayName="Capture Size", matchingRule='strict', value="Standard")
                ent.addOverlay("#00b506", OverlayPosition.NORTH_WEST, OverlayType.COLOUR)
                response.addUIMessage(f"API Flash Transform runs: {api_check.get('remaining')} of {api_check.get('limit')} "
                                      f"credits remaining. Current quota period ends at "
                                      f"{dt.fromtimestamp(api_check.get('reset'))}")
        elif screenshot.status_code == 401:
            response.addUIMessage("The access key used to make this API call has been revoked or is invalid!",
                                  messageType=UIM_FATAL)
        elif screenshot.status_code == 402:
            response.addUIMessage("Payment Required", messageType=UIM_PARTIAL)
        elif screenshot.status_code == 403:
            response.addUIMessage("TForbidden!", messageType=UIM_PARTIAL)
        elif screenshot.status_code == 429:
            response.addUIMessage("Too Many Requests!", messageType=UIM_PARTIAL)
        elif screenshot.status_code == 500:
            response.addUIMessage("Internal Server Error!", messageType=UIM_PARTIAL)
        else:
            response.addUIMessage("Unknown Error", messageType=UIM_PARTIAL)
