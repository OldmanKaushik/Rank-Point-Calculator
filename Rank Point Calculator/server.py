from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("RankPointCalculator.html")

@app.route("/display", methods = ["POST"])
def rank_points():
    name = request.form["name_name"]
    subs_1 = request.form["subs_1_name"]
    subs_2 = request.form["subs_2_name"]
    subs_3 = request.form["subs_3_name"]
    subs_4 = request.form["subs_4_name"]
    gp = request.form["subs_5_name"]
    pw = request.form["subs_6_name"]
    arr = [subs_1,subs_2,subs_3,subs_4,gp,pw]
    new_arr = []
    
    for i in range(6):
        if(arr[i]=="A"): new_arr.append(20)
        elif(arr[i]=="B"):new_arr.append(17.5)
        elif(arr[i]=="C"):new_arr.append(15)
        elif(arr[i]=="D"):new_arr.append(12.5)
        elif(arr[i]=="E"):new_arr.append(10)
        elif(arr[i]=="S"):new_arr.append(5)
        else: new_arr.append(0)
        if(i>2):new_arr[i] = new_arr[i]/2
    total = sum(new_arr)
    return f"Your Rank Points is {total}. Well Done!"
            
if __name__== "__main__":
    app.run()
