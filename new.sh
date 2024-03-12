#!/bin/bash

root_dir="D:/git-clone/data8-2023/lab"

# 遍历根目录
find "$root_dir" -type d -name "tests" | while read -r test_dir; do
    # 遍历测试目录下的所有 Python 文件
    find "$test_dir" -type f -name "*.py" | while read -r file_path; do
        # 创建临时文件，用于保存添加代码后的内容
        temp_file=$(mktemp)
        
        # 在临时文件中先写入要添加的代码行
        echo "OK_FORMAT = True" > "$temp_file"
        
        # 将原文件的内容追加到临时文件中
        cat "$file_path" >> "$temp_file"
        
        # 将临时文件替换为原文件
        mv "$temp_file" "$file_path"
        echo "success"
    done
done

root_dir="D:/git-clone/data8-2023/project"

# 遍历根目录
find "$root_dir" -type d -name "tests" | while read -r test_dir; do
    # 遍历测试目录下的所有 Python 文件
    find "$test_dir" -type f -name "*.py" | while read -r file_path; do
        # 创建临时文件，用于保存添加代码后的内容
        temp_file=$(mktemp)
        
        # 在临时文件中先写入要添加的代码行
        echo "OK_FORMAT = True" > "$temp_file"
        
        # 将原文件的内容追加到临时文件中
        cat "$file_path" >> "$temp_file"
        
        # 将临时文件替换为原文件
        mv "$temp_file" "$file_path"
        echo "success"
    done
done