import torch

print(f"Torch version : {torch.__version__}")
print(f"Is CUDA available : {torch.cuda.is_available()}")
print(f"CUDA Device count : {torch.cuda.device_count()}")
print(f"CUDA Device Name : {torch.cuda.get_device_name(0)}")
