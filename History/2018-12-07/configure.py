import os


class Config(object):
    train_epoch = int(2 ** 6)
    train_size = int(2 ** 15 * 1.97)
    eval_size = int(2 ** 3)
    batch_size = int(2 ** 5)
    batch_epoch = train_size // batch_size

    size = 2 ** 8
    active_rate = 2 ** 3
    replace_num = int(0.25 * batch_size)

    show_gap = 2 ** 4  # time
    eval_gap = 2 ** 9  # time
    gpu_limit = 0.9  # 0.0 ~ 1.0
    gpu_id = 0

    data_dir = '/mnt/sdb1/data_sets'
    aerial_dir = os.path.join(data_dir, 'AerialImageDataset/train')
    cloud_dir = os.path.join(data_dir, 'ftp.nnvl.noaa.gov_color_IR_2018')
    grey_dir = os.path.join(data_dir, 'CloudGreyDataset')

    def __init__(self, model_dir='mod'):
        self.model_dir = model_dir
        self.model_name = 'mod'
        self.model_path = os.path.join(self.model_dir, self.model_name)
        self.model_npz = os.path.join(self.model_dir, self.model_name + '.npz')
        self.model_log = os.path.join(self.model_dir, 'training_npy.txt')


if __name__ == '__main__':
    # from mod_GAN_circle import run
    # from mod_replace import run
    from mod_AutoEncoder import run
    # from mod_coderGAN_buff import run
    # from beta import run

    run()
