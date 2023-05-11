from setuptools import setup, Extension
from torch.utils import cpp_extension
import os 

os.environ["CUDA_HOME"] = "/usr/local/cuda"

setup(
    name='quant_cuda',
    ext_modules=[cpp_extension.CUDAExtension(
        'quant_cuda', ['quant_cuda.cpp', 'quant_cuda_kernel.cu']
    )],
    cmdclass={'build_ext': cpp_extension.BuildExtension},
    install_requires=['torch']
)
