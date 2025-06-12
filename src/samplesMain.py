# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File     : samplesMain.py
# @Author   : jade
# @Date     : 2025/6/12 10:41
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     : samplesMain.py
"""
import os.path
import subprocess
from jade import decryption_model,Exit,GetLastDir,GetPreviousDir,encryption_model

def build_engine(args):
    save_name = ( GetLastDir(args.onnx).split('.')[0] + '.engine' ).replace("_en","")
    save_dir = GetPreviousDir(args.onnx)
    if args.key:
        print(args.key.encode("utf-8"))
        print("正在解密ONNX模型...")
        try:
            args.onnx = decryption_model(args.onnx,key=args.key)
        except Exception as e:
            print(e)
            print("解密出错，请确认密钥")
            Exit(-5)
    print(f"正在生成Tensorrt模型{save_name}...")
    cmd_str = f"trtexec --onnx={args.onnx} --saveEngine={os.path.join(save_dir,save_name)} "
    if args.shapes:
        cmd_str +=  f"--shapes={args.shapes} "
    if args.fp16:
        cmd_str += "--fp16 "
    if args.tacticSources:
        cmd_str += f"--tacticSources={args.tacticSources} "
     # 执行命令并捕获输出
    result = subprocess.run(cmd_str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # 逐行读取输出
    for line in result.stdout.splitlines():
        print(line)
    if args.key:
        os.remove(args.onnx)
        encryption_model(os.path.join(save_dir,save_name))
        os.remove(os.path.join(save_dir,save_name))

def main(args):
    build_engine(args)


