from flask import Blueprint , request
from src.services.activity import detect_activity ,create_df

eval = Blueprint("Eval" ,__name__ ,url_prefix= '/eval')

@eval.route('/' , methods = ['POST' ,'GET'])
def index():
    
    if request.method == 'POST':
        payload =  request.get_json()
        # preProcess the data
        acc = [] 
        data = payload['data']
        if len(data) != 0:
            for i in data:
                i[0] , i[1] ,i[2] = float(i[0]) , float(i[1]) , float(i[2])
                acc.append(i)
        # fed the data into the system    
        df = create_df(acc)
        activity = detect_activity(df)
        print(activity)
        return {"data"  :activity}
    else:
        return {"data"  :"Recived Succefully by Get request "}