import random
import sys

print("""よくばりテスト範囲。最大60問。
""")

J = ["今の会社はたった2駅のところにある。",
"柔道部員はたいてい、安くて量の多い食堂に行きます。",
"スーザンはいつも自分の話ばかり。だから、私は彼女のことはあまり好きじゃないの。",
"コンクリートに囲まれた都会では、季節の微妙な移り変わりを実感するようなことはめったにない。",
"ラジオもテレビもなかった時代、娯楽は自分で創るしかなかった。",
"5歳からピアノを習い始めた我が家の娘たちも、すっかり大人になり、今や誰も弾かなくなった。",
"オリンピックは、開催には莫大な財政的負担がかかり、本来のスポーツマン精神が失われつつある。",
"知床半島は最近世界遺産に登録された。これで、この地域のさらなる開発にストップがかかるだろう。",
"教育において大切なのは、教える内容だけでなく、出会う人の人間性でもあるのだ。",
"初対面の時には、多くの場合、相手が一体どんな人かわからないので、不安を感じるものだ。",
"店員さんのおすすめを断るのは苦手です。",
"進路の件でジェームス先生に相談しに行くんだ。",
"こんなところで君に会うなんてびっくりだね。  うん。世間て狭いわね。",
"ジェニーを週末に晩御飯に誘うんだ。  断られたらどうするのよ。",
"若くして多くの詩や小説に慣れ親しんでしまうと、人生がわかったような気になるものだ。",
"このアンケートに答えるの面倒だね。  適当に答えておけば。",
"この町は10年前とすっかり変わってしまった。",
"バンクーバーからトロントまでの運賃はいくらですか？  片道ですか？往復ですか？",
"この果物は英語でどういうの？  Persimmon(柿)だよ。",
"営業時間は何時から何時までですか？  9時から5時までです。",
"妹に女の子の赤ちゃんが産まれたんだ。  それはよかったね。嬉しいでしょう。",
"学生時代に幅広い知識と柔軟な思考力を身につけた方がいいよ。",
"近々日本にはゴミを捨てる場所がなくなる。資源の再利用について、さらに真剣に取り組まねばならない。",
"気分転換に散歩しない？名案が浮かぶかも。",
"私の小学生の頃は、学校から帰ると近所の子供と外で遊ぶのが普通だった。",
"昔は夜によくラーメンを食べましたが、今では食べません。カロリーの摂取量を減らさなければならないからです。",
"不況のため、叔父は先月、シドニーのレストランを閉めざるを得なくなった。",
"ジョナサンが卵をひげにつけて、慌てて教室に入ってきた時、私たちは思わず笑ってしまった。",
"雨が降るなんて思ってもみなかった。家を出る前に天気予報をチェックしておけばよかった。",
"火事が起きた時、そのホテルには500人を超える客がいたに違いない。",
"弁当箱が見当たらない。ロッカーに忘れてきたかもしれない。  じゃあ、今見てきたら。",
"ジョンのような真面目な学生が、その試験でカンニングをしたはずがない。",
"寝過ごしたけど、母が駅まで車で送ってくれたので、バイトに遅刻しないで済んだ。",
"私はイタリア語がほとんど話せないが、この春、イタリアに旅行した時には、身振り手振りでなんとか通じた。",
"お金が足りなかったので、買おうと思っていたお土産を買えなかった。",
"この小包を速達で送るには、いくらかかるか調べてもらえませんか？",
"もし200歳まで生きられたら、人生は退屈だろう。",
"もし私が日本の総理大臣になったら、まず最初に日本の経済の立て直しに挑戦します。",
"ピザをフライドポテトをとろうっと。  やめておいたら。ダイエット中だろ。",
"フレッドは数学の天才だ。僕なら何時間もかかる問題を一瞬で解いてしまう。",
"もし10億円あれば、海辺に豪邸を買って、引退したい。",
"マスの味を説明しろと言われたら、どんな言葉を選びますか。",
"画面上に指を置き、水平方向に指をすべらせれば、次の画面に移動するよ。",
"もしタイムマシーンで中学時代に戻れるなら、ジェシーをデートに誘いたいわ。",
"マイケルが仕事を辞めたがっているんだ。そうしないように彼を説得してくれるとありがたいんだけど。",
"銃がなければ、米国の殺人件数は減るだろう。",
"24時間営業の保育所がもっとあれば、母子家庭の母親でももっと自由に仕事につけるだろう。",
"この水族館は楽しい。何時間でもいられる。  じゃ1日中いようよ。",
"このジーンズを返品したいのですが。ウエストがちょっときついので。",
"書類はファックスかメールのどちらでお送りいたしましょうか？  どちらでも構いません。そちらで決めてください。",
"医者の言うことを聞いておとなしく寝ていたら、数日でよくなったのにね。",
"もしビートルズに出会って歌手になっていなかったら、普通のサラリーマンになっていたと思う。",
"メルセデス・ベンツを買える余裕があればいいのに。  本当？私は自転車で十分よ。",
"最近、もう20年遅く生まれていたらなと思うことがある。",
"そろそろ後進に道を譲る時期ですよ。",
"3D映画は、あらゆるものがあたかも目の前で繰り広げられているかのように感じられる。",
"父は日頃の運動不足の解消のため、会社までいつも歩いて通勤しています。",
"マドンナのコンサートのチケットを買うために、多くの人が徹夜で列を作っていた。",
"朝ごはんをしっかり食べることは健康にいいんだよ。  わかっているけど時間がないの。",
"タバコが身体に悪いというのは常識だが、止められない人が多い。"]

E = ["The office where I work now is just two stops away on the train.",
"Members of the judo club usually go to restaurants where they can eat a lot of food cheaply.",
"Susan's always talking about herself. That's why I don't like her much.",
"In cities, where you are surrounded by concrete, you seldom experience the subtle changes in the seasons.",
"In the past, when there were no radios or televisions, people had no choice but to create their own entertainment.",
"Our daughters, who began piano lessons when they were five years old, have grown up and no longer play music.",
"The Olympic Games, which cost a fortune to host, are losing their original spirit of sportsmanship.",
"The Shiretoko Peninsula has recently been designated a World Heritage site, which will protect the area from further development.",
"What is important in education is not only what is taught, but what kind of people you meet.",
"When you meet someone for the first time, you often have no idea what they are like, and feel uneasy.",
"It is difficult for me to turn down what a salesclerk recommends.",
"I'm going to have a talk with Mr.James about what to do after graduation.",
"What a surprise to see you here! Yeah. It's a small world.",
"I'll invite Jenny to dinner on the weekend. What if she refuses?",
"People who become familiar with a lot of poems and novels at an early age feel that they know what life is all about.",
"Answering the questions on this questionnaire is troublesome. Just write whatever you like.",
"This town is completely different from what it was ten years ago.",
"What is the fare from Vancouver to Toronto? One way or round trip?",
"What do you call this fruit in English? Persimmon.",
"What are your hours? From 9 a.m. to 5 p.m.",
"My sister had a baby girl. That's great news. You must be happy.",
"While you are a student, you should acquire a lot of knowledge and become flexible in your thinking.",
"Japan in running out of places to dump trash. We must think more seriously about recycling.",
"Shall we go out for a walk to clear our heads? We may come up with a good idea.",
"When I was in elementary school, I would usually play outside with neighborhood kids after school.",
"I used to eat ramen at night, but now I do not because I must cut down on my calorie intake.",
"Because of the recession, my uncle had to close down his restaurant in Sydney last month.",
"When Jonathan rushed into the classroom with some egg on his mustache, we could not help laughing at him.",
"I did not think it would rain. I should have checked the weather report before I left home.",
"When the fire broke out, there must have been over five hundred guests in the hotel.",
"My lunch box is missing. I may have left it in my locker. Well, go and check now.",
"A serious student like John cannot have cheated on the exam.",
"I got up late. But my mother drove me to the station, so I was on time for work.",
"I speak almost no Italian, but while traveling in Italy this spring, I managed to communicate with gestures.",
"I did not have enough money on me, so I could not buy the souvenir that I wanted.",
"Could you check how much it'll cost to send this parcel by special delivery?",
"If you lived to be two hundred years old, your life would probably be boring.",
"If I were the Prime Minister of Japan, I would first of all try to improve the national economic situation.",
"I'm going to order out for pizza and French fries. I wouldn't. You're on a diet.",
"Fred is a math genius. He can solve a problem in a minute that would take me hours.",
"If I had one billion yen, I would buy a luxurious house by the ocean and retire.",
"If you were asked to describe how trout tastes, what words would you choose?",
"If you put your finger on the screen and swipe horizontally, it moves to the next screen.",
"If I could go back by time machine to the days when I was in junior high school, I would ask Jesse out.",
"Michael wants to quit his job. I'd appreciate it if you could talk him out of the idea.",
"Fewer murders would be committed in the U.S. if it were not for guns.",
"If there were more 24-hour childcare centers, single mothers would be freer to work.",
"This aquarium is fun. I could spend hours here. Why don't we stay all day?",
"I'd like a refund on these jeans. The waist is a little too tight.",
"How would you like me to send the documents by fax or by e-mail? I don't mind. You can decide.",
"If you had followed the doctor's advice and stayed in bed, you would probably have gotten well in a couple of days.",
"If I had not discovered the Beatles and become a singer, I would be just an ordinary office worker.",
"I wish I could afford to buy a Mercedes-Benz. Really? A bicycle is enough for me.",
"These days, I sometimes wish I had been born twenty years later.",
"It is about time you resigned your post to make way for younger employees.",
"In 3-D movies, you feel as if everything were happening right before your eyes.",
"My father always walks to work to make up for the lack of exercise in his daily life.",
"Many people stayed up all night waiting in line to buy tickets for Madonna's concert.",
"Eating a hearty breakfast is good for your health. I know, but I have no time.",
"Everyone knows that smoking is bad for their health, but many people cannot quit it."]

num = [i for i in range(60)]
random.shuffle(num)

score = 0
wrong_list = []

Qnum = input("問題数?: ")
print()

for i in range(int(Qnum)):
 print(J[num[i]])
 ans = input()
 if ans == E[num[i]]:
  print("Correct.")
  score += 1
 else:
  print("Wrong.")
  print("Ans:")
  print(E[num[i]])
  wrong_list.append(str(num[i] + 153))
 print()
 print()

wrong_list.sort()

print("RESULT:")
print(score, "/", Qnum)
print(wrong_list)
