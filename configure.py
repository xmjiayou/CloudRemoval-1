import os


class Config(object):
    train_epoch = 2 ** 9
    train_size = int(2 ** 10)
    eval_size = 2 ** 3
    batch_size = int(2 ** 4 * 1.25)
    batch_epoch = train_size // batch_size

    size = int(2 ** 8)  # int(2 ** 7)
    replace_num = int(0.368 * batch_size)
    learning_rate = 8e-5  # 1e-4

    show_gap = 2 ** 2  # time
    eval_gap = 2 ** 2  # time
    gpu_limit = 0.9  # 0.0 ~ 1.0
    gpu_id = 1

    data_dir = '/mnt/sdb1/data_sets'
    aerial_dir = os.path.join(data_dir, 'AerialImageDataset/train')
    cloud_dir = os.path.join(data_dir, 'ftp.nnvl.noaa.gov_color_IR_2018')
    grey_dir = os.path.join(data_dir, 'CloudGreyDataset_%dx%d' % (size, size))

    def __init__(self, model_dir='mod'):
        self.model_dir = model_dir
        self.model_name = 'mod'
        self.model_path = os.path.join(self.model_dir, self.model_name)
        self.model_npz = os.path.join(self.model_dir, self.model_name + '.npz')
        self.model_log = os.path.join(self.model_dir, 'training_npy.txt')


def run():
    import cv2
    import numpy as np
    from utils import img_util

    # np.median(ary) == np.percentile(ary, 50)
    # np.quantile(ary) == np.percentile(ary, 75)
    # thr = cv2.threshold(img, np.percentile(img, 85), 255, cv2.THRESH_BINARY)[1]
    imgs = img_util.get_data__cloud1(32)
    thrs = np.percentile(imgs, 85, axis=(1, 2, 3), keepdims=True)
    imgs[imgs < thrs] = 0
    imgs[imgs >= thrs] = 255

    for img in imgs:
        cv2.imshow('', img)
        cv2.waitKey(423)
    pass


if __name__ == '__main__':
    # from beta import run
    # from mod_eval import run
    from mod_replace import run

    # from mod_haze_unet import run
    # from mod_mend_buff import run
    # from mod_mend_buff_rd import run
    # from mod_mend_disc import run
    # from mod_mend_in_norm import run
    # from mod_mend_circle import run
    # from mod_mend_unet import run

    run()
