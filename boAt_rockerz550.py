
print("Product ASIN Code : B0856HNLDK")


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sentiment = SentimentIntensityAnalyzer()

L=["Overall a good buy!",
"Great Headphone with some inconvenience",
"Great budget Headphone",
"Likeable headphones",
"If you are looking for Good sound Quality but less feature , then this is it",
"Best in range , just go for it.",
"Good in the price range",
"It's sound is beautiful easily going and voice canceling is the best in this product",
"Ok",
"Good but check the below mentioned things",
"Must try",
"Very comfortable with good base",
"Worst build quality",
"Awesome, just go for it",
"Going to buy it again",
"Decent headphone",
"The price of the item should minimize...Rs. 1500 is value for the product",
"Good sound and worst built quality",
"Good product at this price",
"This is a budget friendly piece of amazing volume. A good buy. I purchased it in 1700",
"Rockerzz 550 boat",
"Good sound quality",
"Value for money",
"I am hearing a noise whenever I am watching a video",
"Good product value for money",
"2 years !",
"Rockers 550",
"must buy",
"Bass is less,boat rockers 900 is good for me.",
"Mast h",
"Wire as mentioned not delivered! Bluetooth call not consistent",
"Satisfies my requirements",
"Budget premium Over the Ear Headphones.",
"Good quality headphones",
"Nice one",
"After 1 year of usage",
"waste of money",
"Size",
"Good purchase",
"Works for me",
"9 months of use",
"GOOD BUY",
"Its worth spending money",
"Very soft and must have product",
"nice",
"Good 4 out of 5 headphones.",
"Best buy of 2021 of mine",
"Best product under 1500 rs",
"Great quality",
"Annoying announcement",
"Value for 💸",
"Review of the product",
"Best budget headphones",
"BASS MISSING",
"My feedback",
"Best headphones ever",
"Decent product",
"It's OK",
"Good headphones",
"Quality is peak",
"Good sound but low bass",
"Best product in this prize range. And the colour looks fabulous.",
"Received Defective  product",
"Noise cancellation",
"Extreme Sound Leakage",
"Buy a JBL if you want a good sound quality",
"Rockerz 550 rocks",
"Cheap hardware quality. Don't purchase.",]

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