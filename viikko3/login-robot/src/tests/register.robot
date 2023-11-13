*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  aaaa  aaaaa123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  Username already in use

Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123
    Output Should Contain  Invalid username: Username must be at least three characters long

Register With Long Enough But Invalid Username And Valid Password
    Input Credentials  kalle123  kalle123
    Output Should Contain  Invalid username: Username must contain only characters a-z

Register With Valid Username And Too Short Password
    Input Credentials  kallee  kalle1
    Output Should Contain  Invalid password: Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kallee  kalleeee
    Output Should Contain  Invalid password: Password cannot consist only of letters


*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command
