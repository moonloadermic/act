chrome_path=$(which google-chrome)

# 如果找到了路径，输出路径；否则输出未找到的消息
if [ -n "$chrome_path" ]; then
    echo "Google Chrome 安装路径: $chrome_path"
else
    echo "未找到 Google Chrome 的安装路径"
fi

sudo find / -name google-chrome

sudo locate google-chrome

sudo ls -l /usr/bin/google-chrome
