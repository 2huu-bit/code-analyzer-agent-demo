# Code Analyzer Agent Demo

这是一个演示项目，展示如何使用 **Cursor + Claude** 构建一个**多 Agent 协作的代码库分析系统**。

## 功能

- 自动扫描文件夹中的所有 Python 文件
- 分析每个文件的功能和职责
- 识别模块间的依赖关系
- 生成架构文档和改进建议

## 示例输出

- [依赖分析结果](./analysis_output.md)
- [架构文档](./architecture_docs.md)

## 工作流程

1. 文件扫描 → 2. 代码理解 → 3. 依赖分析 → 4. 报告生成

## 使用的工具

- Cursor（Agent 编排）
- Claude 系列模型（代码理解与推理）
