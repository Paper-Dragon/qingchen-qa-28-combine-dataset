import json
import os
import random
from typing import List, Dict, Any

def read_json_files(directory: str) -> List[Dict[str, Any]]:
    """
    读取指定目录下的所有JSON文件并合并数据
    
    Args:
        directory: 包含JSON文件的目录路径
    
    Returns:
        合并后的数据列表
    """
    all_data = []
    
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            print(f"正在读取文件: {filename}")
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                    # 如果data是列表，直接扩展到all_data
                    if isinstance(data, list):
                        all_data.extend(data)
                        print(f"  从 {filename} 读取了 {len(data)} 条数据")
                    # 如果data是字典，作为单个条目添加
                    elif isinstance(data, dict):
                        all_data.append(data)
                        print(f"  从 {filename} 读取了 1 条数据")
                        
            except Exception as e:
                print(f"读取文件 {filename} 时出错: {e}")
    
    return all_data

def split_data(data: List[Dict[str, Any]], test_ratio: float = 0.2) -> tuple:
    """
    将数据按指定比例分割为训练集和测试集
    
    Args:
        data: 要分割的数据列表
        test_ratio: 测试集比例（默认0.2，即2:8分割）
    
    Returns:
        (训练集, 测试集) 的元组
    """
    # 打乱数据顺序以确保随机性
    data_copy = data.copy()
    random.shuffle(data_copy)
    
    # 计算分割点
    total_size = len(data_copy)
    test_size = int(total_size * test_ratio)
    train_size = total_size - test_size
    
    # 分割数据
    test_data = data_copy[:test_size]
    train_data = data_copy[test_size:]
    
    print(f"数据分割完成:")
    print(f"  总数据量: {total_size}")
    print(f"  训练集: {train_size} 条 ({train_size/total_size*100:.1f}%)")
    print(f"  测试集: {test_size} 条 ({test_size/total_size*100:.1f}%)")
    
    return train_data, test_data

def save_json_file(data: List[Dict[str, Any]], filename: str) -> None:
    """
    将数据保存为JSON文件
    
    Args:
        data: 要保存的数据
        filename: 文件名
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"成功保存文件: {filename}")
    except Exception as e:
        print(f"保存文件 {filename} 时出错: {e}")

def main():
    """
    主函数：读取origin目录下的JSON文件，合并并按2:8比例分割为训练集和测试集
    """
    # 设置随机种子以确保结果可重复
    random.seed(42)
    
    # 原始数据目录
    origin_dir = "origin"
    
    # 检查目录是否存在
    if not os.path.exists(origin_dir):
        print(f"错误: 目录 '{origin_dir}' 不存在")
        return
    
    print("开始读取JSON文件...")
    
    # 读取所有JSON文件
    all_data = read_json_files(origin_dir)
    
    if not all_data:
        print("没有读取到任何数据")
        return
    
    print(f"\n总共读取到 {len(all_data)} 条数据")
    
    # 按2:8比例分割数据（测试集:训练集 = 2:8）
    train_data, test_data = split_data(all_data, test_ratio=0.2)
    
    # 保存训练集
    train_filename = "train_data.json"
    save_json_file(train_data, train_filename)
    
    # 保存测试集
    test_filename = "test_data.json"
    save_json_file(test_data, test_filename)
    
    print("\n数据处理完成！")
    print(f"训练集文件: {train_filename}")
    print(f"测试集文件: {test_filename}")

if __name__ == "__main__":
    main()