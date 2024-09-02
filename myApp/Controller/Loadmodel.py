import pickle

def Loadmodel(file:str):
    with open(file, "rb") as f:
        model = pickle.load(f)

    return model

