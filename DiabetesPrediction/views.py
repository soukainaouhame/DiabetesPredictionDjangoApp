from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    data = pd.read_csv("D:/DiabetePrediction/diabetes.csv")
    X = data.drop("Outcome", axis=1)
    Y = data['Outcome']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    
    
    
    model = LogisticRegression(max_iter=1000)

    model.fit(X_train, Y_train)

    try:
        # Attempt to convert form values to floats
        val1 = float(request.GET['n1'])
        val2 = float(request.GET['n2'])
        val3 = float(request.GET['n3'])
        val4 = float(request.GET['n4'])
        val5 = float(request.GET['n5'])
        val6 = float(request.GET['n6'])
        val7 = float(request.GET['n7'])
        val8 = float(request.GET['n8'])
        print("VAL 1",val1)
        print("VAL 2",val2)
        print("VAL 3",val3)
        print("VAL 4",val4)
        print("VAL 5",val5)
        print("VAL 6",val6)
        print("VAL 7",val7)
        print("VAL 8",val8)
        
        # Make predictions
        pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
        print("SOSOPrediction:", pred)
        if pred == 1:
            result1 = "Positive"
        else:
            result1 = "Negative"

        return render(request, 'predict.html', {"result2": result1})

    except ValueError:
        # Handle the case where conversion to float fails (e.g., empty string)
        error_message = "Invalid input. Please enter numeric values."
        return render(request, 'predict.html', {"error_message": error_message})
