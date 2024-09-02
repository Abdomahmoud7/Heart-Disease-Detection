def GetPredictions(model, inputs):
    predect = model.predict([inputs])[0]

    results = {
        1: "Disease",
        0: "Not Disease"
    }

    return results[predect]



