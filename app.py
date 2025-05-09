from flask import Flask,request,render_template
import pickle
from datetime import datetime



app=Flask(__name__)

#loading the model
model=pickle.load(open('Housing_Model','rb'))


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/',methods=['POST'])
def predict():
    try:
         '''
         Required input for machine learning model
         square
         livingRoom
         drawingRoom
         kitchen
         bathRoom
         constructionTime
         elevator
        '''
         query_square=request.form['square']
         query_livingroom=request.form['livingroom']
         query_drawingroom=request.form['drawingroom']
         query_kitchen=request.form['kitchen']
         query_bathroom=request.form['bathroom']
         query_constructiontime=request.form['constructiontime']
         query_elevator=request.form['elevator'] 
        
        # For elevator
         if query_elevator=="elevator_0":
            elevator_1=0
         else:
            elevator_1=1

         model_data=[[query_square,query_livingroom,query_drawingroom,query_kitchen,
                      query_bathroom,query_constructiontime,elevator_1]]
        
         result=model.predict(model_data)
         x=float(result)
         y="{:.3f}".format(x)

         return render_template('index.html',results=y)


    except ValueError:
        return render_template('index.html')
   

if __name__=="__main__":
    app.run(debug=True)






