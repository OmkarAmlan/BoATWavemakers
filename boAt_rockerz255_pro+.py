
print("Product ASIN Code : B08TV2P1N8")


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sentiment = SentimentIntensityAnalyzer()

L=["Nice product",
"The rebel with a defect",
"Good sound quality",
"Charging Related",
"Disconnecting frequently",
"Product little bit good",
"Good product",
"boAt Rockerz 255 Pro +",
"Amazon",
"Sudden remove charge",
"Very good products 😊",
"Bluetooth connect and again disconnect",
"Durable + good battery + average sound quality",
"Better hai",
"Good sound",
"Overall very good.",
"sound quality is awesome",
"Boat Rockerz",
"Good features but sound quality is not good",
"All parts working but buying 3 months not working Bluetooth headset",
"Good",
"Super &  Best thing",
"Awesome product",
"good",
"It's good....",
"Good product, worth the money!",
"good",
"Good",
"Nice Product",
"Good one",
"Volume is less",
"Excellent battery backup and worth for money",
"Value of money",
"Mangnet are not working properly",
"Nice",
"Product is good.",
"Very nice product. I use daily 5-6 hrs but till 5 days it will work without charge in this duration.",
"Worth Buying",
"For bluetooth calling and power backup.",
"4 month before bluetooth connection automatic connect and disconnect",
"Heavy ear tips for small ears because of metal",
"Very good product 🙂",
"Great product, worth it",
"Good",
"Nice product",
"Good product",
"Headset.",
"Good but disappointing due to one reason",
"It's ok",
"NICE PRODUCT",
"It's good",
"Good earphone but base didn't met expectations",
"Awesome charging backup 👍",
"The Best.",
"Bluetooth service centre not available",
"Decent for this price",
"Value for price",
"Really good product",
"Boat",
"Noice",
"Sound quality best",
"Nice product",
"Rajesh",
"Nice 👍",
"Good product and sound quality",
"Superb quality",
"Best design",
"Build quality in improvement",
"Nice product",
"Very nice product but charging cable not good",
"Nice",
"The magnetic quality of buds are not powerful. Buds keep falling apart.",
"Good",
"Nice",
"Nice product",
"Nice product",
"Good buy",
"Owesome",
"Osm",
"nice product",
"Very nice and good quality Bluetooth earphone.",
"Superb_base",
"Sound base is best",
"Good neckband but the sound quality is not so good",
"amazing battery backup and connectivity",
"Good",
"Rockerz 255 Pro+",
"Better for music",
"Nice Product",
"Good Sound BUT Very Poor (In-Ear Grip) Fit & Poor Build Quality",
"Everything is good except",
"Good base and sound colety",
"Battery capacity is super",
"Okee to use.",
"Good",
"Excellent",
"Outer shell very hard",
"Product",
"Good",
"good",]

ans=[]
for row in L:
    ans.append(sentiment.polarity_scores(row))
sumpos=0
sumneg=0
sumneu=0
sumcomp=0
pos=0
neg=0
neu=0
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