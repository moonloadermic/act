#!/bin/bash

# ���� Google Chrome �İ�װ·��
chrome_path=$(which google-chrome)

# ����ҵ���·�������·�����������δ�ҵ�����Ϣ
if [ -n "$chrome_path" ]; then
    echo "Google Chrome ��װ·��: $chrome_path"
else
    echo "δ�ҵ� Google Chrome �İ�װ·��"
fi
