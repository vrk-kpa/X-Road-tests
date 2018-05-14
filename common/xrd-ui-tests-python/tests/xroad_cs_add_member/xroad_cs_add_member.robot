*** Settings ***

Suite Setup     Test suite setup
Suite Teardown  Test suite teardown
Test Setup      setup
Test Teardown   teardown

Library     QautoRobot  ""

Library     XroadAddCsMember

*** Test Cases ***

Test a xroad add cs member
    XroadAddCsMember.test_a_xroad_add_cs_member

Test b xroad add cs existing member
    XroadAddCsMember.test_b_xroad_add_cs_existing_member

*** Keywords ***
setup
    Start recording  ${TEST NAME}

teardown
    ${documentation}=  Generate failure documentation  ${TEST_DOCUMENTATION}  ${TEST NAME}
    Run Keyword If Test Failed  Set test documentation  ${documentation}

    Stop recording

Test suite setup
    log  log suite setup

Test suite teardown
    log  log suite teardown
