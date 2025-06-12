# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File     : packing.py
# @Author   : jade
# @Date     : 2025/6/12 10:43
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     : packing.py
"""

from jade import *
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--extra_sys_str', type=str,
                        default="")  ## sys.path.append需要额外打包的路径
    parser.add_argument('--extra_path_list', type=list,
                        default=[])  ## 需要额外打包的路径
    ## 引入numpy其他库
    parser.add_argument("--head_str",type=str,default="")
    parser.add_argument('--use_jade_log', type=str,
                        default="True")  ##是否使用JadeLog
    parser.add_argument('--full', type=str,
                        default="True")  ## 打包成一个完成的包
    parser.add_argument('--console', type=str,
                        default="False")  ## 是否显示命令行窗口,只针对与Windows有效

    parser.add_argument('--app_version', type=str,
                        default=get_app_version())  ##需要打包的文件名称
    parser.add_argument('--app_name', type=str,
                        default="Onnx2Trt")  ##需要打包的文件名称
    parser.add_argument('--name', type=str,
                        default="Onnx2Trt")  ##需要打包的文件名称
    parser.add_argument('--appimage', type=str,
                        default="False")  ## 是否打包成AppImage
    parser.add_argument('--lib_path', type=str, default="")  ## 是否lib包分开打包
    parser.add_argument('--is_qt', type=str, default="False")  ## qt 会将controller view src 都进行编译
    parser.add_argument('--specify_files', type=str, default="")  ## 指定编译的文件
    parser.add_argument('--exclude_files', type=str, default="")  ## 指定编译的文件
    parser.add_argument('--remove_specify_files', type=str, default="")  ## 指定编译的文件
    parser.add_argument("--zip_lib",type=str,default='False')
    parser.add_argument('--main', type=str, default="import argparse\n"
                                                    "from src.samplesMain import main\n"
                                                    "if __name__ == '__main__':\n"
                                                    "\tparser = argparse.ArgumentParser(description='ONNX 模型转换为 TensorRT 引擎')\n"
                                                    "\tparser.add_argument('--key', type=str, help='ONNX模型Key')\n"
                                                    "\tparser.add_argument('--onnx', required=True, help='ONNX 模型路径')\n"
                                                    "\tparser.add_argument('--shapes', type=str, default=None ,help='输入形状:x:1x3x320x320')\n"
                                                    "\tparser.add_argument('--fp16', action='store_true', default=False,help='启用 FP16 模式')\n"
                                                    "\tparser.add_argument('--tacticSources', type=str, default=None,help='策略源配置: 逗号分隔列表, 使用 + 添加, - 移除. 例如: +cublas,-cublasLt')\n"
                                                    "\targs = parser.parse_args()\n"
                                                    "\tmain(args)")
    args = parser.parse_args()
    build(args)
    packAPP(args)
    zip_lib_package(args)