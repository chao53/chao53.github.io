import os
import re # 导入正则表达式模块

# --- 用户配置区 ---

# 1. 设置你要处理的文件夹的绝对路径
#    Windows 示例: r'C:\Users\YourUser\Documents\MyNotes'
#    macOS/Linux 示例: '/home/youruser/notes'
#    请务必替换成你自己的路径！
FOLDER_PATH = r'E:/PF/chao53.github.io/hexo\source/_posts'

# 2. 配置图片URL的基础路径
BASE_URL = "https://chao53.github.io/images/"

# 3. 配置 Markdown 图片链接中要匹配的图片文件夹名
#    脚本会查找形如 `(images/file.jpg)` 或 `(images\file.png)` 的链接
#    这里是 'images'
IMAGE_FOLDER_NAME = "images"

# 4. 配置新 <img/> 标签的宽度和高度
IMG_WIDTH = "70%"
IMG_HEIGHT = "70%"

# --- 正则表达式配置 (通常无需修改) ---

# 正则表达式，用于匹配 ![...](images/filename.ext) 格式
# - r'...'          : Python中的原始字符串，避免反斜杠问题
# - !\[.*?\]       : 匹配 ![alt text]，其中 .*? 匹配任意字符（非贪婪模式）
# - \(             : 匹配左括号 (
# - {re.escape(IMAGE_FOLDER_NAME)} : 匹配你指定的文件夹名，例如 'images'
# - [\\\/]         : 匹配路径分隔符，可以是 \ (Windows) 或 / (macOS/Linux)
# - ([^)]+)        : 这是关键的捕获组 (group 1)，匹配括号内除右括号外的所有字符，即文件名
# - \)             : 匹配右括号 )
FIND_PATTERN = re.compile(
    r'!\[.*?\]\(' + re.escape(IMAGE_FOLDER_NAME) + r'[\\\/]([^)]+)\)'
)

# 替换格式
# - <img src="{BASE_URL}\1" ...> : \1 会被替换为上面正则表达式捕获组 (group 1) 的内容，也就是文件名
REPLACE_FORMAT = f'<img src="{BASE_URL}\\1" width="{IMG_WIDTH}" height="{IMG_HEIGHT}">'


# --- 主程序区 ---

def batch_replace_in_md_files(directory, pattern, replacement_format):
    """
    遍历指定目录下的所有.md文件，使用正则表达式查找并替换内容。
    """
    if not os.path.isdir(directory):
        print(f"错误：路径 '{directory}' 不存在或不是一个文件夹。")
        return

    if 'YOUR_FOLDER_PATH_HERE' in directory:
        print("错误：请先在脚本中配置你的文件夹路径 FOLDER_PATH。")
        return

    print(f"开始扫描文件夹: {directory}")
    print("-" * 40)
    
    processed_count = 0
    updated_count = 0

    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.md'):
                processed_count += 1
                file_path = os.path.join(root, filename)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # 使用 re.subn 进行查找和替换
                    # subn 会返回新字符串和替换次数的元组
                    new_content, num_replacements = pattern.subn(replacement_format, content)

                    if num_replacements > 0:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        print(f"  [已更新] -> {file_path} ({num_replacements} 处替换)")
                        updated_count += 1

                except Exception as e:
                    print(f"处理文件 {file_path} 时发生错误: {e}")

    print("-" * 40)
    print("处理完成！")
    print(f"总共检查了 {processed_count} 个 .md 文件。")
    print(f"成功更新了 {updated_count} 个文件。")

# 程序主入口
if __name__ == "__main__":
    batch_replace_in_md_files(FOLDER_PATH, FIND_PATTERN, REPLACE_FORMAT)