import pandas as pd

data = {
    "student": ["amit","sumit","PRIYA","lucky","subhi","amit","pushkar","rahul","mona","gannu"],
    "marks": ["90","89","78","99","97","98","69","65","55","79"],
    "age":["19","20","21""19","20","21","19","20","21","22"]
    
}

df = pd.DataFrame (data)
print(df)
