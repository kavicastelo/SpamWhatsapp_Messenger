#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pyautogui, time
time.sleep(3)
f = open("script", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

