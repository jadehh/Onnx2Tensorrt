# Onnx2Tensorrt
ONNX模型转Tensorrt模型，支持ONNX的动态模型


## Docker打包

```bash
docker run -it --name  packing --gpus=all   -v ${PWD}:/app -w /app   jadehh/python:3.8.16-ubuntu18.04
```

```bash
python packing.py --full True  --app_name onnx2trt
```


## Docker启动

```bash
docker run -it --name tensorrt --gpus=all -v /usr/lib/x86_64-linux-gnu/libnvcuvid.so.1:/usr/lib/x86_64-linux-gnu/libnvcuvid.so.1 -v  /usr/lib/x86_64-linux-gnu/libnvidia-encode.so.1:/usr/lib/x86_64-linux-gnu/libnvidia-encode.so.1   -v ${PWD}:/app -w /app   jadehh/tensorrt:cuda-11.6.2-arch8.6-devel-py3.8 
```

> 需要挂载模型路径和onnx2trt文件路径

```bash
./onnx2trt \
         --key="key" \
         --onnx=../../../model_en.onnx \
         --fp16 \
         --tacticSources="+cublas,-cublasLt"
```

