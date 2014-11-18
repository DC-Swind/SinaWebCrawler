#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
      
import weiboLogin  
import urllib  
import urllib.request  
    
username = ''  
pwd = ''  
      
WBLogin = weiboLogin.weiboLogin()  
WBLogin.login(username, pwd)  
