# import torch
# import torch.nn as nn
#
# print(torch.__version__)
#
# print(torch.cuda.is_available())
# print(torch.cuda.current_device())
# print(torch.cuda.get_device_name(0))
#
# a = torch.tensor([1.0, 2.0, 3.5], dtype=torch.float32)
# print(a.device)
#
# print('Checking:')
# try:
#     b = torch.FloatTensor([1.0, 2.0, 3.5]).cuda()
#     print(b.device)
#     print('Works fine!!')
#     c = torch.tensor([1.0,2.0,3.5], dtype=torch.float32,requires_grad=True).cuda()
#     print(c.device)
# except:
#     print('Error occured')

