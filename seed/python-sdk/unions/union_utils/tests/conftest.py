# This file was auto-generated by Fern from our API Definition.

import os

import pytest
from seed.client import AsyncSeedUnions, SeedUnions


@pytest.fixture
def client() -> SeedUnions:
    return SeedUnions(base_url=os.getenv("TESTS_BASE_URL", "base_url"))


@pytest.fixture
def async_client() -> AsyncSeedUnions:
    return AsyncSeedUnions(base_url=os.getenv("TESTS_BASE_URL", "base_url"))
