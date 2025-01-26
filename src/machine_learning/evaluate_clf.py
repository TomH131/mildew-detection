from src.data_management import load_pkl_file, download_model

download_model()


def load_test_evaluation(version):
    return load_pkl_file(f'outputs/{version}/evaluation.pkl')