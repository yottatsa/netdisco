"""Discover D-Link cameras."""
from urllib.parse import urlparse

from . import SSDPDiscoverable
from ..const import ATTR_PORT, ATTR_URLBASE


class Discoverable(SSDPDiscoverable):
    """Add support for discovering D-Link cameras."""

    def get_entries(self):
        """Get all the Huawei uPnP entries."""
        return self.find_by_device_description({
            "manufacturer": "D-Link",
            "modelDescription": "Wireless Internet Camera",
            "deviceType": "urn:schemas-upnp-org:device:Basic:1.0"
        })

    def info_from_entry(self, entry):
        """Get most important info, which is name, model and host."""
        info = super().info_from_entry(entry)
        info[ATTR_URLBASE] = entry.description['device']['presentationURL']
        info[ATTR_PORT] = urlparse(info[ATTR_URLBASE]).port
        return info
