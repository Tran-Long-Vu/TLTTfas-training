
MODEL_BACKBONE= "rn18"
MODEL_NAME = 'rn18fas'
ATTACK_TYPE = 'printing'
INFERENCE_DEVICE = 'CUDA'

INFERENCE_TYPE = 'printing'

VAL_DATASET = 'CVPR23'
TEST_DATASET = 'HAND_CRAWL'

TEST_FROM_CHECKPOINT = False # onnx

PATH_TO_CHECKPOINT_MODEL = 'checkpoints/fas-best.pth'

PATH_TO_IMAGES = ''
PATH_TO_VIDEOS = ''
PATH_TO_SINGLE_VIDEO = './data/video_benchmark/0/real.mp4'


PATH_TO_PRINTING_TEST_DATASET = 'data/datasets/Hand_crawl/images/'
PATH_TO_REPLAY_TEST_DATA = 'data/datasets/Hand_crawl/videos/'

PATH_TO_STATE_DICT = 'model/rn18-fas-ckp.pth'

PATH_TO_CHECKPOINT_ONNX = 'checkpoints/fas-best.onnx'

PATH_TO_SAVE_CHECKPOINT = 'checkpoints/'
PATH_TO_FAS_MODEL = './model/rn18-fas.onnx'
PATH_TO_FD_MODEL ='./model/scrfd.onnx'



