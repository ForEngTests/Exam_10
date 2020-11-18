import random
import sys

print("""システム(Standard)テスト範囲。
最大11×4=44問。

全範囲・・・Enter 0
範囲指定・・Enter the Chapter Number(7, 8, 9, 10).
""")

score = 0
wrong_list = []
select = input()
list = ["7", "8", "9", "10"]

J = ["その少年は犬を怖がっていたらしい。",
"正直にいえば、僕は彼の話し方が気に入らない。",
"不思議なことに、その花瓶は割れなかった。",
"私は彼がカラオケで歌うのを聞いたことがありません。",
"その先生は自分の話をトム(Tom)に信じさせることはできなかった。",
"彼の冗談には笑わざるを得なかった。",
"妹はフランス文学を研究するためにパリへ渡った。",
"私たちは氷の上を滑らないように注意した。",
"その見知らぬ人は親切にも道案内をしてくれた。",
"このコーヒーは熱すぎて飲めない。",
"友達が今晩テレビに出ることになっている。",
"脂肪をとりすぎると高血圧になることもある。",
"彼はそんなに長い間怠惰であったことを悔やんでいます。",
"彼らは僕が払えといって聞かないのです。",
"キャシー(Cathy)は大学を出るとすぐに結婚した。",
"私たちはその喜劇を見て思わず笑ってしまったのだった。",
"あいつとうまくやっていくことはとてもできない。",
"言い訳をしようとしても無駄ですよ。",
"勤勉が成功への鍵であることは言うまでもありません。",
"今は食べたくありません。",
"やってみるだけの価値はあると思う。",
"昨日あの小説を読み終えました。",
"彼女が店先でコートを眺めているのを私は見た。",
"赤ちゃんを泣かせたままにしておいてはいけません。",
"私は混雑した電車のなかでずっと立ちっぱなしでした。",
"そこへ着いたら友人は待っていた。",
"彼はニュージーランドに留学していたことがあったので英語は達者です。",
"左に折れると警察署がありますよ。",
"タクシーがなかったので私たちは歩いて帰宅しなければなりませんでした。",
"彼は顔つきから判断すると50を超えている。",
"彼は自分の体が持ち上げられるのを感じた。",
"パソコンの修理にいくらかかりましたか。",
"トム(Tom)は目を閉じて考えにふけっていた。",
"当時、北米は新世界と呼ばれていた。",
"たくさんの家が台風で吹き飛ばされてしまっている。",
"その家は現在建築中です。",
"引力の法則は誰によって発見されましたか。",
"あのおじいさんは村の皆に尊敬されている。",
"彼の絵はその美術館に展示されるでしょう。",
"そのホールは学生たちでいっぱいでした。",
"姉は自分の収入に満足していない。",
"人はその仲間によって知られるといいます。",
"僕はバイクを取られてしまった。",
"彼はその晩、残業をさせられた。"]

E = ["The boy seems to have been afraid of dogs.",
"To be honest, I don't like his way of speaking.",
"Strange to say, the vase did not break.",
"I have never heard him sing karaoke.",
"The teacher couldn't make Tom believe her story.",
"I couldn't but laugh at his joke.",
"My sister went to Paris in order to study French literature.",
"We were careful so as not to slip on the ice.",
"The stranger was kind enough to show me the way.",
"This coffee is too hot for me to drink.",
"My friend is to appear on TV tonight.",
"Eating too much fat may lead to high blood pressure.",
"He regrets having been lazy for such a long time.",
"They insist on my paying the money.",
"On finishing university, Cathy got married.",
"We could not help laughing at the comedy.",
"There is no getting along with him.",
"It is no use trying to excuse yourself.",
"It goes without saying that diligence is the key to success.",
"I don't feel like eating now.",
"I think it is worth trying.",
"I finished reading the novel yesterday.",
"I saw her window-shopping for a coat.",
"Don't leave your baby crying.",
"I remained standing in the crowded train.",
"Arriving there, I found my friend waiting for me.",
"Having studied in New Zealand, he is good at speaking English.",
"Turning left, you'll see the police station.",
"There being no taxis, we had to walk home.",
"Judging from his looks, he is not under fifty.",
"He felt his body lifted.",
"How much did it cost to get your PC fixed?",
"Tom was meditating with his eyes closed.",
"In those days, North America was called the New World.",
"Many houses have been blown down by the typhoon.",
"The house is now being built.",
"Who was the law of gravitation discovered by?",
"The old man is looked up to by everybody in the village.",
"His painting will be displayed in the museum.",
"The hall was filled with students.",
"My sister is not satisfied with her salary.",
"It is said that a man is known by the company he keeps.",
"I had my motorbike stolen.",
"He was made to work overtime that evening."]

if select == "0":
 num = [i for i in range(44)]
 random.shuffle(num)
 Qnum = int(input("問題数?: "))

elif select in list:
 num = [(int(select) - 7) * 11 + i for i in range(11)]
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
print([str((i // 11) + 7) + "-" + str(i % 11 + 1) for i in wrong_list])
