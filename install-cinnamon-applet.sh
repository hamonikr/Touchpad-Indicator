#!/bin/bash

# 스크립트가 있는 디렉토리로 이동
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# 애플릿 UUID
UUID="touchpad-indicator@hamonikr"

# 필요한 디렉토리 생성
echo "Creating directories..."
mkdir -p ~/.local/share/cinnamon/applets/$UUID
mkdir -p ~/.local/share/locale/ko/LC_MESSAGES

# 애플릿 파일 복사
echo "Installing applet files..."
cp -r $UUID/files/$UUID/* ~/.local/share/cinnamon/applets/$UUID/

# 번역 파일 컴파일 및 설치
echo "Installing translation files..."
cd $UUID/files/$UUID/po
msgfmt ko.po -o ~/.local/share/locale/ko/LC_MESSAGES/$UUID.mo

echo "Installation completed!"
echo "Please restart Cinnamon (Alt+F2, then type 'r') and add the applet from System Settings > Applets." 