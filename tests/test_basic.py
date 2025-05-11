import pytest
from homeassistant.setup import async_setup_component


async def test_load_custom_component(hass):
    assert await async_setup_component(hass, "hassio_s3_backup", {})
