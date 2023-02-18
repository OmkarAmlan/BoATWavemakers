
print("Product ASIN Code : B08PDGRR32")


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sentiment = SentimentIntensityAnalyzer()

L=["Great speakers for Indoors (Only transmits sound from front not from back. It's serves the purpose though)Decent Battery life, RGB lights & It's controls are easy to understand, Mostly will use mobile or PC controls anyway :).I would say charging time was a huge con , It'll take about 4 hours 30 mins to charge it from 0 to 100%,of course they mentioned it will take 4 hours, but it can be improved as cost is bit high.✌️",
"Battery life indication is not properly working when 70 to 100% life. This is only cons i have seen since 15 days usage. Backup time around 6 hrs at 65% volume with RGB ON. I'm fully satisfied about battery life.Bluetooth connectivity is superb. Mobile is in terrace where speaker is in ground floor awesome working without distraction.Sound and voice is crystal clear while using low volume and then high volume bass is superb. I'm in rural area the FM is connected, its tuning and tuning but not further connected i think the frequency of the product is above 100Hz thats the reason, so main concern for myself.I recommend to buy this product surely.",
"Before we buy this we always look for an honest feedbacks in the feedback sections because we don't wanna take risk with spending money.So here's the take: If you live in an apartment or a room then buy this, it has more than average bass and sound is good as well. Dont go with the video comparisons on YouTube it will only confuse you. The only cons is the battery , if you blast on a high volume it will last 3 hours but that's enough for anyone.If you play it in 50 to 70 percent volume which also sounds high then it will last 8 hours.Good luck with the purchase.",
"Just one thing the fm is minus point for me as i have tried so many times but i canot connect to fm , and besides it nothing to worry about you can go for it .",
"Sound quality is good at this price point but it is not delivering battery backup that Boat is claiming......!!",
"Good quality but needed more volume",
"I'm 3.5 star rating for Regan the body material low  but sound is good light is good",
"Everything is good axcept battery is not going to be long time. Thankyou.",
"Amazon products package was very. Good and on time delivered I am completely satisfied",
"Amazing sound quality. Worth for price. Best product 🔥",
"Please don't Buy this product. ❌No doubt the product quality is good but the customer support is as worst as possible.Please go for any other brand but not this, really felt so uncomfortable while claiming the guarantee. If I rank the product its 8/10... But if I rank the service team and the customer support it will be 1/10.I've suffered alot, writing this comment to guide others who are just going to purchase it now.",
"Awesome speaker at this price range!!! 🤩🤩",
"Worth for the money and late charging. Battery 🔋 long last",
"Best quality",
"Sound quality is good.bluetuth connectivity good.battery life is somethind disappoint but overall product is awesome.i recommend to buy.",
"Battery durations",
"Just received it two days ago, and so far… it's doing well for itself. However, I was expecting more bass, more depth towards softer tones or background sounds in videos, for it’s size is quite big!As per connectivity issues, it does get disconnected here n there, n gets connected again. The voice stared to distort once in between these two days too…Hopefully the minor problems won’t become major as time passes by.",
"Sudden this device off when sound is high.....",
"Speaker is very good as per price. Best thing about this speak is its bass. I love it, don't think twice just go for it.",
"Say 9 hours but is runs upto 6-7 hours",
"Nice",
"Best sound quality",
"Sound quality is better",
"Sound is not good bass it's  ok",
"ಚೆನ್ನಾಗಿದೆ , ಉತ್ತಮ ಗುಣಮಟ್ಟದ ಉತ್ಪನ್ನ",
"Worst Battery backup",
"Product is nice",
"Very good",
"Battery life is low.Led lights are not that good.Bass is bestSound quality is also bestBut is Price high.",
"I like boat 1200",
"great product in this budget",
"Sound quality very nice and Bluetooth jabardast bettery long life",
"More sound required , great base .",
"Battery capacity very low.",
"Battery life depends on Sound level.",
"LOVE IT WE ITS NEXT UPDATE OR MODEL 🤠",
"काफी loud ह,बेस भी गजब हैफुल चार्ज होकर,फुल आवाज में 3 घण्टे चल जाता है",
"Actually It So Time To Charge It one of the Dis advantage But So Sound Soo Good If You Listen 60 To 70 It Super Clear Voice and Lyrics Overall So Good...",
"All is good except battery life. If from starting this is situation then I guess within a year it will need constant power.",
"Good speaker GOOD sound quality and bass also good FM Not working That's the only problem",
"Sounds very well with Boat signature audio quality. Audio is very balanced and bass is good.",
"Sound quality was good but but excellent",
"I like the product but battery backup don't like",
"It's giving only 1-2 hrs battery backup. Only problem with battery Otherwise its excellent.",
"Value for money! Use it wisely if you listen for long hours battery might drain so turn off RGB when you listen to music or anything else.",
"Nice product but low bass",
"First of 1200 bass isn't that much as we expect and it doesn't connect sometimes automatically apart from that all are goodSound quality , loudness superb",
"Sound quality is ok but battery backup worst",
"the bass of the product is avg and not according to the size of the product....",
"speaker is very nice sound quality is also goog and loud too but battery backu is decent not very good",
"Nice Qualitycrisp soundGood bassBattery is not upto mark but yes will last upto 5-6 hrs",
"Ossm deal",
"Compactness/Sound quality/Power Backup.....well designed technology.",
"Beautiful looking, clear audio, only complaint to battery life",
"Life is just 3 ,4 months after that automatically switch off",
"FM and voice assistance is not working even after restart.Return period is also over.What should i do know.",
"A friend purchased, we had an indoor party (suitable for 5-10 people), we were ALL super impressed. I too purchased, completely happy.Was about to order stone 1450, but eventually preferred 1200 (got some negative feedback about 1450).Bass is super amazing.Coming to prices, they are at higher end. I think they have soared the prices basis the demand of this particular model. I had a voucher, otherwise good if around 3k or 3.5k maximum.Boat website and Amazon have same prices.Trustworthy product delivered by Amazon. Have a barcode on product box for its authenticity.",
"Good one, sounds quality depending on connected device, fm not working.",
"Their is this weird issue that I'm facing 1 year after it's usage. It turns off at higher volumes and that is really disturbing. Thus, I'd recommend not to buy this product",
"Though I saw the mixed review honestly I was confused .. since I wanted to gift my mother .. she is very happy",
"Overall good sound for music and voice chat. Battery drains faster if RGB are connected. Should show RGB lights only when sound is playing through speakers to preserve power, but it shows as soon as RGB mode is on. Also button should be more visible. In dark it should illuminate or should be given appropriate color. Buttons are not distinguished in color from body color",
"This one is beast when I am speaking about the quality of the sound output. But within few months the exact problem started with breaking connectivity with the Bluetooth. And specially the worst part of the product that the battery life has degraded like anything . At first it was giving 4 hours of battery life which now has degraded and came something around 1.5 hours. The base of this 14 watt Bluetooth speaker is the only thing which makes this product stand alone thing in the crowd.",
"Microphone quality is poor cannot be used for calls, otherwise the sound and bass is good.",
"Bass is just too good. only problem is low battery life.",
"This thing will not give a good music listening. Just okay for listening the music. Don't expect perfect bass or soud quality it will loud with its maximum volume bOat brand can give us a best quality product but why they don't make those things are good",
"Sound is Good,Bluetooth connectivity is okBut Battery life is poor",
"Very good quality in terms of pricing and features.Worth buying if you compromise a bit with sound clarity.",
"Best sound quality on this product.",
"I tested it well and really it survived themAnd sound quality was also good too andValuable for your money too",
"Absolutely in love with this product,  best in class sound ,loud and clear,  bass output is ok, Bluetooth connectivity is good too",
"The product is fabulous but it's battery back up is low and there is a negative point that we cannot switch off the RGB lights in the speaker while we from Bluetooth",
"1st about the good qualitySound was loud & amazing.Build also very rough and toughNow about the bed qualitiesThe Bluetooth connectivity was the worst.battery life also not up to the mark",
"It's battery drain soon in 2 hours with RGB and without RGB only for 3 hours  but sound quality is good",
"Sound quality is good. Highs mids and lows are balanced. The base is sufficient but not good for deep base lovers.I faced some connectivity issues. Within 5 meter sound cracked sometimes. 10 meter range is worst.Control buttons are pathetic. Sometimes times works perfectly but sometimes it's not responding and very lagging.Battery life is average, it's depending on the volume.FM is just a joke.",
"It's  a Great product recommended to go for it",
"Product quality and sound is good super bass",
"Right for the price",
"I bought this speaker at reasonably good price at Rs2499. Played it for four days and found that sound quality is excellent for this price. But I found it's battery backup is way below than what is claimed in its description. It hardly runs for 3 (three) hours at full volume with RGB lights on.  So keep this in mind before buying it.",
"The sound and bass are in sync and sounds good. Even on full volume no distortion sound could be heard. The passive bass radiators works well enhancing the sound beats. Overall good bluetooth speaker at this price. But the battery back up is not as put up in banners. On volume above 60℅ the battery back up is around 6 hrs with led. And the charging time from 10-100 is above 4 hours.",
"Nothing",
"Beatry life is low",
"the sound produced from this speaker is loud and clear.The bass is the best quality in this speaker.The highs are sharp,the mids are clear and the highs are the best.I like the RGB lighting around the bass radiator.It is pretty big speaker for this price range.The size makes the speaker not portable and coming to the weight it is pretty heavy.I conclude it is a great speaker respective of its sound,the size and the weight are the only cons of this speaker.",
"I have only one problem with thisThe battery life of this product is not that goodIt's battery fastly gets drained so I have to charge it many timesExcept this all things are very good👍👍Overall 4 /5",
"Nice sound quality.",
"Quality of sound is very good build quality also goodbut redio connectivity is very poorbattery life needs to improve 4 to 4.30 hr battery life.",
"Received on time.. great experience.  . Buy it and enjoy thr roller coaster ride with the bass , sound quality and with THE RGBs ... 😍",
"Battery bad",
"I love the overall design and the sound is loud too. But bass is a little bit below my expectations. I have to use an equaliser app to produce good enough bass. Battery is also good..",
"Sound quality is simply superb",
"Bty prblm",
"Not crystal clear sound but loud and bass is ossom",
"I am using this speaker and the bluetooth often get disconnected by its own from my phone rest all are godd speakers are quite good and loud for the 14w speakers but the price was high.",
"Carry strep nhi diya gya iske sath",
"Sound is not clear in full volumes I think money is enough but the quality is not enough and the bluetooth indicator or level of charge suddenly increase and decrease The cover or cloth materials is not good it is not stiky.",
"Go for it",
"Bought this for my mother who is used to play devotional songs in the morning... Good sound. For film songs reasonable bass. Battery lasts for about 7 Hrs as in specs..But since control buttons are total black difficult to identify which button for what.",
"BoAt Stone 1200 Speaker खतरनाक है खतरनाक मै इस स्पीकर को और स्पीकर जहाँ - जहाँ गया है वहाँ पर इस स्पीकर ने अपना एक अलग से पहचान बनाया है। जब स्पीकर बजता है और उसमे से जो तभाई वाला बैस निकलता है सुन और महसूस करके बस यही कहता बडा बवाल चीज है रे, फिर भी किसी मे तगड़ा खुभी हो और उस मे एक भी कमी न हो ऐसा नही हो सकता ऐसा ही इसमें है मै जब कभी स्पीकर को लगभग 20 - 30  अवाज या वाल्यूम मे कभी सुनता हू तो इस स्पीकर से एक प्रकार का ( हीस ) जैसा अवाज आता है जो बहुत ही बेकार सा मुझको लगता है।",
"The product is amazing in this rate but the battery life could be more extended.",]

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