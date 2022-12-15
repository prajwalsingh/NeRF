import os
import math

os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'
os.environ["CUDA_DEVICE_ORDER"]= "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]= '0,1'

train_json_path = 'dataset/nerf_synthetic/materials/transforms_train.json' 
val_json_path   = 'dataset/nerf_synthetic/materials/transforms_val.json' 
image_path      = 'dataset/nerf_synthetic/materials'
device       = 'cuda'
lr           = 3e-4
image_height = 128
image_width  = 128
batch_size   = 5
epochs       = 300

pos_enc_dim  = 10
dir_enc_dim  = 4
focal        = (image_width/2)/(math.tan(0.6911112070083618/2.0)) # f =  (p/2) / tan(theta/2)

near_plane   = 2.0
far_plane    = 6.0
num_samples  = 32
net_dim      = 128
in_feat      = 63
skip_layer   = 4
net_depth    = 8