import pytest
from geneeral_functions_steps import *

def test_full_training_program_creation_JHSC():
    print('Start')
    openweb(portal_link)
    print('link connected')
    logging(user, password) is True, 'Failed to log in'
    subbmittionoftrainingprogram(JHSCPartOne) is True, 'Failed to submit information'
    checkboxes(JHSCPartOne) is True, 'Failed to fill up checkboxes'
    trainingprogramsmaterials() is True, 'Failed to fill up materials'
    uploadfiles() is True, 'Failed to upload files'
    applicationreview() is True, 'Failed to review app'
    submitapp() is True, 'Failed to submit final app'
    assert successcheck() is True, 'Failed to check success'
    # newprogramid = programid()
    runtime()
    # closeweb()
    print('End')

'''
def test_full_training_program_creation_WAH():
    print('Start')
    assert openweb(portal_link) is True, 'Failed to open web'
    try:
        assert logging(user, password) is True, 'Failed to log in'
    except:
        print('Already logged in')
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
'''


