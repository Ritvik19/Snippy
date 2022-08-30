# TF and PT models don't explicitly use a random seed parameter
# So the following function can be used to set random seed
# For scikit learn we can provide random state directly


def seed(seed, tensforflow_init=True, pytorch_init=True):
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)
    if tensforflow_init:
        tf.random.set_seed(seed)
    if pytorch_init:
        torch.manual_seed(seed)
        torch.cuda.manual_seed(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
