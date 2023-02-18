
print("Product ASIN Code : B0949SBKMP")


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sentiment = SentimentIntensityAnalyzer()

L=["Good 👍",
"Step count Failed",
"Nice quality",
"Nice watch",
"Budjet King",
"Bad connectivity",
"I like this watch but only missing sum features like u can't able to receive the call.",
"It's pretty decent",
"Value for the money spent",
"Wake up screen not up to the mark",
"The Blue color is worst. BUY RED ONE",
"Design very good",
"Excellent👍💯",
"Its worth it",
"Average quality",
"Very nice",
"Sensor is not good",
"Good but accuracy is low.",
"Boat FLASH: value for money",
"Always disconnected",
"NOT CONNECTING WITH BLUETOOTH",
"Nice",
"Budget. Friendly with a round dial ......",
"Watch almost good",
"Wearable not detecting incoming call alerts",
"Watch again not getting on",
"Nice",
"Not worth the money",
"Good product",
"Good",
"Battery 🔋 power awesome,basic smart watch",
"Build Quality ☝🏻🙏🏻🙂",
"Need to improve more on quality",
"No words for this watch, But, Just Wow ❤️❤️❤️",
"Almost Cost Efficient",
"Best gift to teen kids",
"Battery stop working after few months of usage",
"Their some only features but that the have nice and smooth display",
"Awesome product",
"This is very good",
"Awsm watch and lovely strap colours",
"Good",
"Best smartwatch ever🎉🎉",
"Ts watcha hi",
"For fifty rupees only",
"Ok",
"It's so osm ....go for it guys .....bas ismei speaker ka be be option hota tho both aacha hota 😉",
"Kinda piyana UPu boAt flash thoppu",
"Wake up gesture do not work properly rest is fine.",
"Best Watch For beginner and Worth for Money!",
"Good",
"Nice",
"Overall good watch!",
"Doesn't connecting properly",
"performance is perfect",
"Not so good",
"Watch review",
"She loved it! ❤️",
"Not top of the line",
"Value for Money",
"Contacts display",
"Good product at this price",
"Nice product",
"Connecting problem may be raised after using 3-4 months",
"Best watch at this range.. i think",
"Good battery lyf. Good water proof.",
"I metallic body of watch",
"Good watch for the first time user",
"Only one minus temper glass no",
"Not at all great product",
"Design and looks are good. Great battery life! Rest all disappoints!",
"It's pretty good",
"Notification issue",
"All fit",
"Nic",
"Worth it",
"Lookwise awesome",
"Could have been better.",
"To know calories",
"Very average",
"Amazing watch but didn't like the strap have to replace",
"Very Nice product from Boat",
"Not so impressive",
"Using for 1 year.",
"Screen touch is good.",
"Good",
"awesome looks and hardware, not satisfactory software",
"Smart watch",
"Good",
"Purchase only for looks, not for festures",
"Nice but strap is too delicate",
"This product was not worth",
"Worth spending money on this",
"It lags a bit",
"No calling feature",
"It’s nt have bt calling but Good n Comfortable Smart Watch",
"Friendly product",
"👌",
"I love its design btw it's a descent watch .",
"Good investment",]

ans=[]

for row in L:
    ans.append(sentiment.polarity_scores(row))
sumpos=0
sumneg=0
pos=0
neg=0
neu=0
sumneu=0
sumcomp=0
for i in range(len(ans)):
    if(ans[i]['compound']==0):
        neu+=1
    elif(ans[i]['compound']>0):
        pos+=1
    else:
        neg+=1
    sumpos+=ans[i]['pos']
    sumneg+=ans[i]['neg']
    sumneu+=ans[i]['neu']
    sumcomp+=ans[i]['compound']
    
avgpos=sumpos/len(ans)
avgneg=sumneg/len(ans)
avgnue=sumneu/len(ans)
avgcomp=sumcomp/len(ans)

print("Average positive review = " + str(avgpos))
print("Average negative review = " + str(avgneg))
print("Average neutral review = " + str(avgnue))
print("Compound average = " + str(avgcomp))
print("Positive Reviews = " + str(pos*100/len(ans)) + " %")
print("Negative Reviews = " + str(neg*100/len(ans)) + " %")
print("Neutral Reviews = " + str(neu*100/len(ans)) + " %")