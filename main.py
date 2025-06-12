# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File     : main.py
# @Author   : jade
# @Date     : 2025/6/12 10:42
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     : main.py
'''
import argparse
from src.samplesMain import main
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ONNX 模型转换为 TensorRT 引擎')
    parser.add_argument('--key', type=str, help='ONNX模型Key')
    parser.add_argument('--onnx', required=True, help='ONNX 模型路径')
    parser.add_argument('--shapes', type=str, default=None ,help='输入形状:x:1x3x320x320')
    parser.add_argument('--fp16', action='store_true', default=False,help='启用 FP16 模式')
    parser.add_argument('--tacticSources', type=str, default=None,help='策略源配置: 逗号分隔列表, 使用 + 添加, - 移除. 例如: +cublas,-cublasLt')
    args = parser.parse_args()
    main(args)


