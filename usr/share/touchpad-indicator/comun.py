#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is part of Touchpad-Indicator
#
# Copyright (C) 2010-2019 Lorenzo Carbonell<lorenzo.carbonell.cerezo@gmail.com>
# Copyright (C) 2010-2012 Miguel Angel Santamaría Rogado<leibag@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import locale
import gettext

USRDIR = '/usr'


def is_package():
    return (__file__.startswith(USRDIR) or os.getcwd().startswith(USRDIR))


APPNAME = 'Touchpad Indicator'
APP = 'touchpad-indicator'
APPCONF = APP + '.conf'


PARAMS = {
    'first-time': True,
    'version': '',
    'is_working': False,
    'autostart': False,
    'on_mouse_plugged': False,
    'on_start': 1,
    'on_end': 1,
    'disable_on_typing': False,
    'interval': 800,
    'start_hidden': False,
    'show_notifications': True,
    'theme': 'light',
    'touchpad_enabled': True,
    'natural_scrolling': True,
    'speed': 0.0,
    'tapping': True,
    'two_finger_scrolling': True,
    'edge_scrolling': False,
    'cicular_scrolling': True,
    'right-top-corner': 0,
    'right-bottom-corner': 0,
    'left-top-corner': 0,
    'left-bottom-corner': 0,
    'one-finger-tap': 0,
    'two-finger-tap': 0,
    'three-finger-tap': 0,
    'faulty-devices' : ['11/2/a/0',  # TPPS/2 IBM TrackPoint
                  '11/2/5/7326',  # ImPS/2 ALPS GlidePoint
                  '11/2/1/0',
                  '11/2/6/0', # ImExPS/2
                  ]
}

# check if running from source
STATUS_ICON = {}
if is_package():
    ROOTDIR = '/usr/share/'
    LANGDIR = os.path.join(ROOTDIR, 'locale')
    APPDIR = os.path.join(ROOTDIR, APP)
    AUTOSTART_SOURCE_DIR = APPDIR
    ICONDIR = '/usr/share/icons/hicolor/scalable/apps'
    SOCIALDIR = os.path.join(APPDIR, 'social')
    CHANGELOG = os.path.join(APPDIR, 'changelog')
else:
    ROOTDIR = os.path.dirname(__file__)
    LANGDIR = os.path.normpath(os.path.join(ROOTDIR, '../po'))
    APPDIR = ROOTDIR
    AUTOSTART_SOURCE_DIR = os.path.normpath(os.path.join(APPDIR, '../data'))
    ICONDIR = os.path.normpath(os.path.join(APPDIR, '../data/icons'))
    DEBIANDIR = os.path.normpath(os.path.join(ROOTDIR, '../debian'))
    CHANGELOG = os.path.join(DEBIANDIR, 'changelog')

ICON = os.path.join(ICONDIR, 'touchpad-indicator.svg')
STATUS_ICON['normal'] = (os.path.join(ICONDIR, 'touchpad-indicator-normal-enabled.svg'),
                        os.path.join(ICONDIR, 'touchpad-indicator-normal-disabled.svg'))
STATUS_ICON['light'] = (os.path.join(ICONDIR, 'touchpad-indicator-light-enabled.svg'),
                       os.path.join(ICONDIR, 'touchpad-indicator-light-disabled.svg'))
STATUS_ICON['dark'] = (os.path.join(ICONDIR, 'touchpad-indicator-dark-enabled.svg'),
                      os.path.join(ICONDIR, 'touchpad-indicator-dark-disabled.svg'))


CONFIG_DIR = os.path.join(os.path.expanduser('~'), '.config')
CONFIG_APP_DIR = os.path.join(CONFIG_DIR, APP)
CONFIG_FILE = os.path.join(CONFIG_APP_DIR, APPCONF)

AUTOSTART_DIR = os.path.join(CONFIG_DIR, 'autostart')
FILE_AUTO_START_NAME = 'touchpad-indicator-autostart.desktop'
FILE_AUTO_START_SRC = os.path.join(AUTOSTART_SOURCE_DIR, FILE_AUTO_START_NAME)
FILE_AUTO_START = os.path.join(AUTOSTART_DIR, FILE_AUTO_START_NAME)
WATCHDOG = os.path.join(APPDIR, 'watchdog.py')

VERSION = 'unknown'
try:
    if os.path.exists(CHANGELOG):
        with open(CHANGELOG, 'r') as f:
            line = f.readline()
            pos = line.find('(')
            posf = line.find(')', pos)
            if pos > -1 and posf > -1:
                VERSION = line[pos + 1: posf].strip()
                if not is_package():
                    VERSION = VERSION + '-src'
except Exception as e:
    print(f"Warning: Could not read changelog: {str(e)}")

try:
    current_locale, encoding = locale.getdefaultlocale()
    if current_locale is None:
        current_locale = 'en_US'
    print(f"Current locale: {current_locale}")
    language = gettext.translation(APP, LANGDIR, [current_locale], fallback=True)
    language.install()
    print(f"Loaded language: {language}")
    _ = language.gettext
except Exception as e:
    print(f"Error loading language: {str(e)}")
    _ = str
