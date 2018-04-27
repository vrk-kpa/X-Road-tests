*** Settings ***

Suite Setup     Test suite setup
Suite Teardown  Test suite teardown
Test Setup      setup
Test Teardown   teardown

Library     XroadAddCentralService
Library     XroadDeleteCentralService

*** Test Cases ***

Test xroad add central service
    XroadAddCentralService.test add central service 2 2 8

Test xroad delete central service
    XroadDeleteCentralService.test add central service 2 2 8


*** Keywords ***
setup
    log  log setup

teardown
    log  log teardown

Test suite setup
    log  log suite setup

Test suite teardown
    log  log suite teardown
