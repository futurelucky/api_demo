# API Auto Test Demo

基于 `requests` + `pytest` 的接口自动化测试框架示例。

## 技术栈
- Python 3.9+
- requests / pytest / pytest-html / pytest-xdist / jsonschema / PyYAML

## 快速开始

```bash
# 1. 克隆项目
git clone https://github.com/futurelucky/api_demo.git
cd api_demo

# 2. 创建虚拟环境
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 运行测试
pytest
pytest -m smoke           # 冒烟
pytest -n 4               # 并行
```

## 目录结构
```
api_demo/
├── config.py
├── conftest.py
├── pytest.ini
├── clients/
└── tests/
```

## 测试报告
运行后自动生成 `reports/report.html`。