from fastapi import FastAPI
from Controller.GitPredictions import GetPredictions
from Controller.Loadmodel import Loadmodel
import uvicorn

model = Loadmodel("D:\Machine Learning Projects\myApp\model\heart_disease_model.pkl")
app = FastAPI()

@app.get("/")
def getPredections(age: int, sex: int, cp: int, trestbps: int, chol: int, 
                   fbs: int, restecg: int, thalach: int, exang: int, 
                   oldpeak: int, slope: int, ca: int, thal: int):
    
    inputs = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    
    predections = GetPredictions(model, inputs)

    return predections

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)


