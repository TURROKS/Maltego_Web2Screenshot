from datetime import datetime as dt
from urllib import parse
import requests

from extensions import registry
from maltego_trx.maltego import MaltegoMsg, MaltegoTransform
from maltego_trx.transform import DiscoverableTransform
from maltego_trx.overlays import OverlayType, OverlayPosition


def api_handler(api_url, target_url, api):

    data = requests.get(api_url+f"urltoimage?access_key={api}&url=https://{target_url}&fresh=true")

    if data.status_code == 200:
        return data.url


def api_info(api_url, api):

    data = requests.get(api_url+f"urltoimage/quota?access_key={api}")
    parsed = data.json()

    if data.status_code == 200:
        return parsed


@registry.register_transform(display_name="Greet Person", input_entity="maltego.Phrase",
                             description='Returns a Phrase greeting a Person on the Graph.',
                             output_entities=["maltego.Phrase"])
class WebsiteToScreenshotFresh(DiscoverableTransform):

    @classmethod
    def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):

        api_key = ''
        api_baseurl = 'https://api.apiflash.com/v1/'
        input_url = request.Value
        clean_url = parse.quote_plus(input_url)

        screenshot = api_handler(api_url=api_baseurl, target_url=clean_url, api=api_key)
        api_check = api_info(api_url=api_baseurl, api=api_key)

        ent = response.addEntity("maltego.Image", str(input_url).lower())
        ent.addProperty("url", "URL", "strict", screenshot)
        ent.addDisplayInformation(content=f'<a href="{screenshot}">Open in Browser</a>', title="Screenshot")
        ent.addProperty(fieldName="captureType", displayName="Capture Type", matchingRule='strict', value="Live")
        ent.addProperty(fieldName="captureSize", displayName="Capture Size", matchingRule='strict', value="Standard")
        ent.addOverlay("#00b506", OverlayPosition.NORTH_WEST, OverlayType.COLOUR)
        response.addUIMessage(f"API Flash Transform runs: {api_check.get('remaining')} of {api_check.get('limit')} "
                              f"credits remaining. Current quota period ends at "
                              f"{dt.fromtimestamp(api_check.get('reset'))}")
