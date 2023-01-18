import os
import math

os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'
os.environ["CUDA_DEVICE_ORDER"]= "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]= '0'

dataset_type    = 'llff' # 'synthetic', 'real', 'llff'

if dataset_type == 'synthetic':
	train_camera_path = 'dataset/nerf_synthetic/chair/transforms_train.json' 
	val_camera_path   = 'dataset/nerf_synthetic/chair/transforms_val.json' 
	train_image_path  = 'dataset/nerf_synthetic/chair'
	val_image_path    = 'dataset/nerf_synthetic/chair'

	factor       = 2 # factor
	pre_height   = 800
	pre_width    = 800
	image_height = int(pre_height/factor)
	image_width  = int(pre_width/factor)
	downscale    = pre_width / image_width
	near_plane   = 2.0
	far_plane    = 6.0
	epochs       = 3501
	lrsch_step   = 2500
	pre_epoch    = 50
	pre_crop     = 0.5
	noise_value  = 0.0

elif (dataset_type == 'real') or (dataset_type == 'llff'):
	# train_camera_path = 'dataset/nerf_real_360/vasedeck/poses_bounds.npy'
	# val_camera_path   = 'dataset/nerf_real_360/vasedeck/poses_bounds.npy'
	# train_image_path  = 'dataset/nerf_real_360/vasedeck/images'
	# val_image_path    = 'dataset/nerf_real_360/vasedeck/images'

	train_camera_path = 'dataset/nerf_llff_data/fern/poses_bounds.npy'
	val_camera_path   = 'dataset/nerf_llff_data/fern/poses_bounds.npy'
	train_image_path  = 'dataset/nerf_llff_data/fern/images'
	val_image_path    = 'dataset/nerf_llff_data/fern/images'
	basedir           = 'dataset/nerf_llff_data/fern/'

	factor       = 8 # factor
	pre_height   = 3024
	pre_width    = 4032
	image_height = int(pre_height/factor)
	image_width  = int(pre_width/factor)
	downscale    = pre_width / image_width
	epochs       = 20001
	lrsch_step   = 10000
	pre_epoch    = 0
	pre_crop     = 0.5
	noise_value  = 1.0


device       = 'cuda'
use_ndc      = False
lr           = 5e-4
num_channels = 3
batch_size   = 1
vis_freq     = 10
ckpt_freq    = 10
lrsch_gamma  = 0.1#0.99

pos_enc_dim  = 10
dir_enc_dim  = 4

num_samples  = 64
num_samples_fine  = 128
net_dim      = 256
in_feat      = 2*(3*pos_enc_dim) + 3
dir_feat     = 2*(3*dir_enc_dim) + 3
skip_layer   = 4
net_depth    = 8
num_samples_fine  = 2 * num_samples
n_samples    = 1024#4096