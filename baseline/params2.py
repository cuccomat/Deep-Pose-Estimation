from operator import truediv


class Parameters():
    def __init__(self):

        self.batch_size = 1
        self.batch_size_1 = 60
        self.epochs = 100
        self.learning_rate = 0.001
        self.weight_decay = 1e-7
        self.decay = 0.001
        self.decay_t = 0.000001
        self.shuffle = True

        self.resume = False
        self.USE_GPU = True
        self.ON_COLAB = True

        self.print_every = 10

        self.run_id = '2t7uzdmb' #cuccomat/Deep Pose Estimation PnP Downsampled/3ksiu9sw

        if self.ON_COLAB:
            self.txt_path = 'drive/Othercomputers/Il mio laptop/Deep-Pose-Estimation/baseline/poses_equatoriale_txt'
            self.txt_path_2 = 'drive/Othercomputers/Il mio laptop/Deep-Pose-Estimation/baseline/poses_45_DLC_txt'
            self.csv_path = 'drive/Othercomputers/Il mio laptop/Deep-Pose-Estimation/baseline/poses_equatoriale.csv'
            self.csv_path_2 = 'drive/Othercomputers/Il mio laptop/Deep-Pose-Estimation/baseline/poses_45_DLC.csv'
            self.root_path = 'drive/Othercomputers/Il mio laptop/Deep-Pose-Estimation/baseline/RGB_images_equatoriale'
            self.root_path_2 = 'drive/Othercomputers/Il mio laptop/Deep-Pose-Estimation/baseline/dataset_45_DLC'
            self.checkpoint_path = 'drive/Othercomputers/Il mio laptop/Deep-Pose-Estimation/baseline/checkpoint'
            self.tm_path = 'drive/Othercomputers/Il mio laptop/Deep-Pose-Estimation/baseline/AnyConv.com__LDA.stl'
            self.object_points_path = 'drive/Othercomputers/Il mio laptop/Deep-Pose-Estimation/baseline/3D points'
        else:
            self.txt_path = './poses_equatoriale_txt'
            self.csv_path = './poses_equatoriale.csv'
            self.root_path = './RGB_images_equatoriale'
            self.checkpoint_path = './checkpoint'
            self.tm_path = './AnyConv.com__LDA.stl'
            self.object_points_path = './3D points'