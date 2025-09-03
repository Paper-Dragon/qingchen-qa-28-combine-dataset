# QA数据集合

## 项目结构

```txt
qingchen-qa-28-combind-dataset/
├── origin/                          # 原始数据目录
│   ├── QA数据(人工).json
│   ├── 环境管理体系汇总20241208_QA.json
│   ├── 职业健康汇总_QA.json
│   └── 质量管理体系汇总_QA.json
├── main.py                          # 主处理脚本
├── train_data.json                  # 训练集（80%，6,238条）
├── test_data.json                   # 测试集（20%，1,559条）
└── README.md                        # 项目说明文档
```

### 运行示例

```bash
$ python main.py
开始读取JSON文件...
正在读取文件: QA数据(人工).json
  从 QA数据(人工).json 读取了 49 条数据
正在读取文件: 环境管理体系汇总20241208_QA.json
  从 环境管理体系汇总20241208_QA.json 读取了 3158 条数据
正在读取文件: 职业健康汇总_QA.json
  从 职业健康汇总_QA.json 读取了 2197 条数据
正在读取文件: 质量管理体系汇总_QA.json
  从 质量管理体系汇总_QA.json 读取了 2393 条数据

总共读取到 7797 条数据
数据分割完成:
  总数据量: 7797
  训练集: 6238 条 (80.0%)
  测试集: 1559 条 (20.0%)
成功保存文件: train_data.json
成功保存文件: test_data.json

数据处理完成！
训练集文件: train_data.json
测试集文件: test_data.json
```
