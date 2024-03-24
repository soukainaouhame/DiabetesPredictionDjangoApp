Title of the Project: "Diabetes Prediction System" 📈

Excited to share my second project in data analysis, kindly given to me by MeriSKILL

Objective: Predicting diabetes likelihood in patients based on specific diagnostic measurements from the dataset. The dataset originates from the National Institute of Diabetes and Digestive and Kidney Diseases.

COLUMN DESCRIPTION FOR DIABETES DATA:

Pregnancies
Glucose
Blood Pressure
Skin Thickness
Insulin
BMI
Diabetes
Age
Outcome

In analyzing the dataset, I categorized the data into independent and dependent variables. Notably, all seven variables—Pregnancies, Glucose, Blood pressure, Skin thickness, Insulin, BMI, Diabetes, Age—are independent, with 'Outcome' serving as the dependent variable.

Within the dataset, 0 indicates a non-diabetic individual, while 1 signifies a diabetic individual. This rationale leads us to leverage Logistic Regression, a method for predicting binary outcomes using the logistic function.

Correlation Matrix Analysis:

Positive correlations between "Glucose," "BMI," "Age," and "Insulin" with the "Outcome" variable align with expectations based on diabetes risk factors. Notably, the lack of strong negative correlations suggests that none of the variables significantly reduce diabetes risk.

Training and Test Data:

80% of the data is dedicated to training, with the remaining 20% allocated for testing. The model's accuracy stands at 0.77, indicating its correct prediction of outcomes for around 77% of instances in the dataset.
