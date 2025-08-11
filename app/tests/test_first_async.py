import asyncio
from unittest.mock import patch

import pytest
from first_asyncio import custom_routine


@pytest.mark.asyncio
async def test_custom_routine_prints_correctly(capsys):
    # Patch asyncio.sleep so it doesn't actually delay
    async def no_sleep(_):
        return None

    with patch("asyncio.sleep", side_effect=no_sleep):
        await custom_routine()

    # Capture printed output
    captured = capsys.readouterr()
    # Expected letters, each on a new line
    expected_output = "\n".join(list("First Asyncio")) + "\n"
    assert captured.out == expected_output
