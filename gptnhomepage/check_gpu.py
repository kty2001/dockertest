import torch

print("this is gpt file")
print(torch.cuda.is_available())
num_devices = torch.cuda.device_count()
print("num_device:", num_devices)
for device_id in range(num_devices):
    print(f"Device {device_id}: {torch.cuda.get_device_name(device_id)}")