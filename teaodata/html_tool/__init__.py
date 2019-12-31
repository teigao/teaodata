#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
This module is used to handle and generate html files. 
-- 
"""

import os
import webbrowser
import winreg

def _get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
    return winreg.QueryValueEx(key, "Desktop")[0]


def create_html(content = "This is a sample page", result_saved_path=_get_desktop() + '\\result.html'):
    temp_html_file = open(result_saved_path,'w', encoding='UTF-8')
    temp_html_file.write(content)
    temp_html_file.close()
    saved_html_path = 'file:///' + result_saved_path

    webbrowser.open_new_tab(saved_html_path)
    
    message = "The html has been generated to " + result_saved_path
    print(message)
    return None

def open_html(path = None):
    if path == None:
        print("please provide the link of html")
    else:
        webbrowser.open_new_tab(path)

if __name__ == '__main__':
    print('Welcome to use "teaodata" library, please use it with the import command!')
