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

import gi
try:
    gi.require_version('Gio', '2.0')
except Exception as e:
    print(e)
    exit(-1)
from gi.repository import Gio
from gi.repository import GLib

SCHEMA_PATH = '/apps/touchpad-indicator/'

class DConfManager(object):
    def __init__(self, schema_id):
        schema_source = Gio.SettingsSchemaSource.get_default()
        if schema_source.lookup(schema_id, True) is None:
            # 스키마가 없는 경우 기본 설정을 사용
            self.setting = None
        else:
            self.setting = Gio.Settings.new(schema_id)

    def get_keys(self):
        if self.setting is None:
            return []
        return self.setting.list_keys()

    def set_value(self, entry, value):
        if self.setting is None:
            return False
            
        try:
            if isinstance(value, str):
                self.setting.set_string(entry, value)
            elif isinstance(value, bool):
                self.setting.set_boolean(entry, value)
            elif isinstance(value, int):
                self.setting.set_int(entry, value)
            elif isinstance(value, list):
                if all(isinstance(x, str) for x in value):
                    self.setting.set_strv(entry, value)
                else:
                    return False
            else:
                return False
            return True
        except Exception as e:
            print(f"Error setting value: {e}")
            return False

    def get_value(self, entry):
        if self.setting is None:
            return None
            
        try:
            value = self.setting.get_value(entry)
            if value.get_type_string().endswith('as'):
                return self.setting.get_strv(entry)
            elif value.get_type_string().endswith('s'):
                return self.setting.get_string(entry)
            elif value.get_type_string().endswith('b'):
                return self.setting.get_boolean(entry)
            elif value.get_type_string().endswith('i'):
                return self.setting.get_int(entry)
        except Exception as e:
            print(f"Error getting value: {e}")
        return None

    def get_values(self):
        if self.setting is None:
            return []
        values = []
        for entry in self.setting.list_keys():
            values.append(self.get_value(entry))
        return values

    def get_children(self):
        if self.setting is None:
            return []
        return self.setting.list_children()


if __name__ == '__main__':
    dcm = DConfManager('org.mate.SettingsDaemon.plugins.media-keys')
    for key in dcm.get_keys():
        print(key, dcm.get_value(key))
    dcm = DConfManager('org.mate.desktop.keybindings.touchpad-indicator')
    print('action', dcm.get_value('action'))
    print('binding', dcm.get_value('binding'))
    print('name', dcm.get_value('name'))
