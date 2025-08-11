import asyncio

import pytest
from first_asyncio import custom_routine


@pytest.mark.asyncio
async def test_custom_routine():
    message = "Hello"
    result = await custom_routine(message)
    assert result == f"Got: {message}"


@pytest.mark.asyncio
async def test_custom_routine_with_empty_string():
    message = ""
    result = await custom_routine(message)
    assert result == "Got: "
