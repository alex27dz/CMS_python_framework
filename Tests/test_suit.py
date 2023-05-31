import pytest
from Training_program_steps import *

@pytest.fixture
def fixture_func_hi():
    return 'hi'
@pytest.fixture
def fixture_func_bye():
    return 'bye'


# testing step before running scenarios - using fixtures
def test_somthing_before(fixture_func_hi, fixture_func_bye):
    print('Before tests run success')
    assert fixture_func_hi is 'hi', 'Was expected to get hi'
    assert fixture_func_bye is 'bye', 'Was expected to get bye'


def test_full_training_program_creation():
    print('Start')
    openweb()
    assert logging() is True, 'Failed to log in'
    assert subbmittionoftrainingprogram() is True, 'Failed to submit information'
    assert checkboxes() is True, 'Failed to fill up checkboxes'
    assert trainingprogramsmaterials() is True, 'Failed to fill up materials'
    assert uploadfiles() is True, 'Failed to upload files'
    assert applicationreview() is True, 'Failed to review app'
    assert submitapp() is True, 'Failed to submit final app'
    assert successcheck() is True, 'Failed to check success'
    assert viewdelaisofcreatedapp() is True, 'Failed to view details of new app'
    print('End')



