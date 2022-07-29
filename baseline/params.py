class Parameters():
    def __init__(self):

        self.batch_size = 128
        self.epochs = 11
        self.learning_rate = 0.001
        self.weight_decay = 1e-7
        self.shuffle = True

        self.resume = False
        self.USE_GPU = True
        self.ON_COLAB = True

        self.print_every = 10

        self.run_id = '3jkxyacc'

        if self.ON_COLAB:
            self.txt_path = 'drive/Othercomputers/Il mio laptop/Deep-Pose-Estimation/baseline/poses_txt'
            self.csv_path = 'drive/Othercomputers/Il mio laptop/Deep-Pose-Estimation/baseline/poses.csv'
            self.root_path = 'drive/Othercomputers/Il mio laptop/Deep-Pose-Estimation/baseline/RGB_images'
            self.checkpoint_path = 'drive/Othercomputers/Il mio laptop/Deep-Pose-Estimation/baseline/checkpoint'
            self.tm_path = 'drive/Othercomputers/Il mio laptop/Deep-Pose-Estimation/baseline/AnyConv.com__LDA.stl'
        else:
            self.txt_path = './poses_txt'
            self.csv_path = './poses.csv'
            self.root_path = './RGB_images'
            self.checkpoint_path = './checkpoint'
            self.tm_path = './AnyConv.com__LDA.stl'