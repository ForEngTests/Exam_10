import random
import sys

print("""システム(Advanced)テスト範囲。
最大13×4=52問。

全範囲・・・Enter 0
範囲指定・・Enter the Chapter Number(7, 8, 9, 10).
""")

score = 0
wrong_list = []
select = input()
list = ["7", "8", "9", "10"]

J = ["彼は主にネットなどから情報を得ていたようだ。",
"かいつまんで言うと実地訓練に集中しなければならないということだ。",
"新聞は、いわば社会の目であり耳である。",
"私は手品師が帽子からうさぎを取り出すのを見た。",
"先日お借りした本をもう一週間拝借させてください。",
"私は明日から始まる入学試験を受けるためにここに着いた。",
"悪い習慣を身につけないように注意しなさい。",
"僕は去年の夏休みにアルバイトをして、パック旅行で海外に行けるくらい稼ぐことができました。",
"手を貸そうか。その箱は重たくて一人では教室まで持っていけないよ。",
"こんなに朝早く電話してくるなんて、どういうつもりだ。",
"その家で先々週見つかった英国人男女は、餓死したのではないかと思われている。",
"実を言うと、ちょうどその日にもらったばかりの給料を全部取られちゃったんだ。",
"N教授はインドで開かれることになっている国際会議に出席のため、昨夜成田空港を発った。",
"文法を学ぶことも読む能力をつけることも、話す際には大いに役立つんだよ。",
"君はあんなことをしたのを恥ずかしいと思わないかい。",
"母親は息子が金メダルをとったのが自慢だった。",
"ホームページを見たらすぐにそれをプリントしておくようにするとよい。",
"少年の頃僕は誰にでも敵意を感じないわけにはいかなかった。",
"西欧文明がある問題に直面している事実を隠すことはできない。",
"そんな本を読んだってなんの役にも立たないよ。",
"健康がほかの何よりも大切であることは言うまでもない。",
"暖かい日に野原を散歩すると自然に対して感謝したくなります。",
"皆様にお会いするのを楽しみにしています。",
"自分の目で作品を見てみたい、直接彼に会いたい、と思わないではいられませんでした。",
"オリンピックにおいてもっとも重要なことは勝つことではなくて参加することであるというのは、言うまでもない。",
"大きな駅のホームに日本各地に向かうさまざまな列車が並んでいる光景は鮮明に覚えている。",
"海の上に何か黒いものが浮かんでいるのに気がついた。",
"お待たせしてすみません。どのくらいお待ちになりましたか。",
"川沿いに少し行くと景色の良いので有名な場所に着いた。",
"客を送り出すと、私はその本を鉛筆をはさんでおいたところから読み出した。",
"月が出たので電灯を消しました。",
"一般的に言ってどの家庭もさほど裕福ではありませんでした。",
"昔に比べると日本人の生活は自然との接触を失っている。",
"私は自分で手紙を書き、それを英語に訳してもらった。",
"先月その歯医者さんに親知らずを抜いてもらいました。",
"私は彼が靴を手に持ったまま走っているのを見た。",
"警察庁はこうした事情に配慮して、専用駐車スペースの整備など、高齢ドライバーの支援に力点を置いた施策に取り組み始めた。",
"医師に認知症と診断されて、免許を取り消されたのは、受験した75歳以上の高齢者全体から見ればごく少数だ。",
"私たちは国際語である英語を使って、日本をもっと外国に理解してもらう必要がある。",
"1990年代、日本人観光客は贅沢品を買いあさることで有名であった。",
"そろばんは2000年以上もの間使われてきた。",
"負傷者たちは救急車に運び込まれているところでした。",
"誰がその大学への道を案内したのですか。",
"私は突然外国人に話しかけられたので面食らった。",
"そんな事態は我慢できない。",
"学校からの帰り道、にわか雨にあってずぶぬれになりました。",
"私は切手の収集に興味を持っています。",
"現代人は骨が弱くなったと言われる。",
"吊り橋を渡るときに、帽子を風に吹き飛ばされてしまった。",
"本や雑誌がこれほど数多く出版されているにもかかわらず、私たちが読書に費やす時間は年々減少している。",
"詰め込みの受験学習はすべて忘れてしまい身につきませんが、想像力は学習だけでなく人生のあらゆることに応用されるでしょう。",
"今の子供は親の期待を受け、親の決めた進路を歩かされている。"]

E = ["He seems to have acquired information mainly from the Internet.",
"To sum up, we have to focus on our on-the-job training.",
"Newspapers are, as it were, the eyes and ears of society.",
"I saw the magician take a rabbit from the hat.",
"Please let me have the book I borrowed the other day for another week.",
"I came here so as to take the entrance exams that will start tomorrow.",
"Be careful not to form bad habits.",
"By working hard at my part-time job last summer, I earned sufficient money to travel overseas on a package tour.",
"Shall I give you a hand? The box seems too heavy to carry to the classroom by yourself.",
"It is rude of you to call me so early in the morning.",
"The British man and woman who were found in the house two weeks ago seem to have starved to death.",
"To be honest, I had my whole salary I had earned that day stolen.",
"Professor N left Narita Airport last night in order to attend the international conference, which was to be held in India.",
"Learning grammar and developing reading ability are very helpful in learning to speak the language.",
"Aren't you ashamed of having done such a thing?",
"His mother was proud of her son having got the gold medal.",
"On seeing the website, you should print it.",
"When I was a boy, I couldn't but show hostility to everybody.",
"There is no hiding the fact that Western civilization faces a certain problem.",
"It is no use at all reading such a book.",
"It goes without saying that nothing is more important than health.",
"When we take a walk in a field on a warm day, we feel like thanking nature.",
"I am looking forward to seeing you all.",
"I couldn't but want to look at his work with my own eyes and to see him in person.",
"Needless to say, the most important thing in the Olympics is not to win but to take part.",
"I clearly remember seeing, from the platforms of a big railway station, various trains bound for several places in Japan.",
"I saw something dark floating on the sea.",
"I am sorry to have kept you waiting. How long have you been waiting?",
"Going a little way along the river, I reached the place famous for its fine view.",
"Having seen my guests off, I started to read the book from the page where I had put a pencil.",
"The moon coming out, I switched off the light.",
"Generally speaking, most of the families were not so well off.",
"Compared with the past, the Japanese people have reduced their contact with nature.",
"I wrote a letter by myself and had it translated into English.",
"I had a wisdom tooth pulled out by the dentist last month.",
"I saw him running with his shoes in his hands.",
"Taking this situation into consideration, the National Police Agency has started to work on measures which put emphasis on assisting elderly drivers, such as providing special parking spaces for them.",
"Considering the total number of examinees aged 75 and over, the number of people who were diagnosed with dementia and had their drivers' licenses canceled was very small.",
"We must try to have Japan understood more by other countries, by using English as an international language.",
"In the 1990s, Japanese tourists were well known for buying up many luxury goods.",
"An abacus has been used for more than 2,000 years.",
"The injured were being carried into the ambulance.",
"By whom were you shown the way to the university?",
"I was embarrassed when I was suddenly spoken to by a foreigner.",
"Such matters cannot be put up with.",
"I was caught in a shower on my way home from school and got wet to the skin.",
"I am interested in collecting stamps.",
"It is said that modern people have weak bones.",
"I had my hat blown off by the wind when I went across the suspension bridge.",
"Though many books and magazines are being published, the amount of time we spend in reading has been decreasing every year.",
"What you study for tests through cramming will soon be forgotten and lost from your memory; but your imagination can be applied not only for your school work but also for everything in your life.",
"Children today are made to walk the course determined by their parents' expectations."]

if select == "0":
 num = [i for i in range(52)]
 random.shuffle(num)
 Qnum = int(input("問題数?: "))

elif select in list:
 num = [(int(select) - 7) * 13 + i for i in range(13)]
 random.shuffle(num)
 Qnum = int(input("問題数?: "))

else:
 sys.exit()

for i in range(Qnum):
 print(J[num[i]])
 ans = input()
 if ans == E[num[i]]:
  print("Correct.")
  score += 1
 else:
  print("Wrong.")
  print("Ans:")
  print(E[num[i]])
  wrong_list.append(num[i])
 print()
 print()

wrong_list.sort()

print("RESULT:")
print(score, "/", Qnum)
print([str((i // 13) + 7) + "-" + str(i % 13 + 1) for i in wrong_list])
