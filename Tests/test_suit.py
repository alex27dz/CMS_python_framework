import pytest
from Training_program_steps_delays import *


def test_full_training_program_creation_WAH():
    print('Start')
    assert openweb(portal_link) is True, 'Failed to open web'
    assert logging(user, password) is True, 'Failed to log in'
    assert subbmittionoftrainingprogram(WorkingatHeights) is True, 'Failed to submit information'
    assert checkboxes(JHSCPartOne) is True, 'Failed to fill up checkboxes'
    assert trainingprogramsmaterials() is True, 'Failed to fill up materials'
    assert uploadfiles() is True, 'Failed to upload files'
    assert applicationreview() is True, 'Failed to review app'
    assert submitapp() is True, 'Failed to submit final app'
    assert successcheck() is True, 'Failed to check success'
    # newprogramid = programid()
    runtime()
    # closeweb()
    print('End')


def test_full_training_program_creation_JHSC():
    print('Start')
    assert openweb(portal_link) is True, 'Failed to open web'
    assert logging(user, password) is True, 'Failed to log in'
    assert subbmittionoftrainingprogram(JHSCPartOne) is True, 'Failed to submit information'
    assert checkboxes(JHSCPartOne) is True, 'Failed to fill up checkboxes'
    assert trainingprogramsmaterials() is True, 'Failed to fill up materials'
    assert uploadfiles() is True, 'Failed to upload files'
    assert applicationreview() is True, 'Failed to review app'
    assert submitapp() is True, 'Failed to submit final app'
    assert successcheck() is True, 'Failed to check success'
    # newprogramid = programid()
    runtime()
    # closeweb()
    print('End')


