import os


class Config(object):
    train_epoch = 2 ** 11
    train_size = int(2 ** 11 * 1.8)
    eval_size = 2 ** 3
    batch_size = 2 ** 4
    batch_epoch = train_size // batch_size

    size = int(2 ** 7)
    replace_num = int(0.368 * batch_size)

    show_gap = 2 ** 4  # time
    eval_gap = 2 ** 4  # time
    gpu_limit = 0.48  # 0.0 ~ 1.0
    gpu_id = 1

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


def run():
    pass


if __name__ == '__main__':
    # from mod_haze_unet import run
    # from mod_mend_GAN_resize import run
    from mod_mend_GAN_buff import run

    # from beta import run
    run()
