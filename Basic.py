import random
import sys

print("""Basicの日本語を表示する。
判定は行わない。(2つあったりするから)
全範囲・・・Enter 0
範囲指定・・Enter the Chapter Number(7, 8, 9, 10).
""")

J = ["彼は病気だったらしい。(2)",
"彼女は若い頃美人だったと言われていた。(2)",
"実を言うと、私はお金の持ち合わせがありません。",
"彼はいわばかごの鳥だ。",
"私はジョンが家に入るのを見た。(2)",
"彼女は弟を外で待たせておいた。(2)",
"彼の勇気には感嘆せざるを得ない。",
"私は始発電車に乗るために早く起きた。",
"彼らは音をたてないように靴を脱いだ。",
"君は一人で旅するには幼すぎる。",
"この箱は重すぎて私には運べません。",
"クリスは今夜出発する予定です。",
"手伝ってくれるなんて親切ね。",
"百聞は一見にしかず。(諺)",
"彼女はお金を無駄遣いしてしまったことを後悔している。(2)",
"僕は父が貧しくたって恥ずかしくない。(2)",
"彼は私を見た途端顔を背けた。(2)",
"私は彼がまだ生きていると思わざるを得ない。(2)",
"今から10年後には何が起こるかわかったものではない。(2)",
"彼女にデートを申し込んでも無駄だよ。",
"健康が富にまさることは言うまでもない。(2)",
"今夜は勉強する気になれない。",
"エディンバラ城は訪れてみる価値はある。",
"恐れ入りますが窓を開けていただけませんか。----良いですよ。",
"先日どこかで彼にお会いしたのを覚えています。",
"私は心臓が激しく鼓動しているのを感じた。",
"お待たせしてすみません。",
"子供たちは私たちの方へ走ってきた。",
"何を言っていいかわからなかったので彼は黙っていた。(2)",
"宿題を終えた後でテレビを見た。(2)",
"右に曲がれば郵便局が見えますよ。(2)",
"夜になったので私たちは家路についた。",
"厳密にいえば宵の明星は星(恒星)ではない。",
"海に囲まれているので、英国は気候が温暖である。",
"彼は待合室で自分の名前が呼ばれるのを聞いた。",
"あなたは英語で用が足せますか。",
"彼女はドレスをクリーニングしてもらった。",
"その老人は足を組んで椅子に腰掛けていた。",
"その犬は子供たちにジョンと呼ばれている。",
"この部屋は、ハウスキーパーによってすでに清掃されていた。",
"その道路は作業員に修理されているところだ。",
"電話は誰によって発明されましたか。",
"彼は皆に笑われた。",
"ホワイト氏は隣人たちの評判が良い。",
"その小説は多くの人々から愛されるでしょう。",
"この市の誰でも市長を知っている。",
"その山の頂上は雪で覆われていた。",
"私たちはそのニュースにびっくりした。",
"彼女が病気だそうだよ。(2)",
"私は一昨日腕時計を盗まれた。",
"あの人たちのテント、洪水で押し流されちゃったんだよ。",
"かわいそうにもその学生は、自分の意思に反して契約書にサインさせられた。(2)"]

select = input()

if select == "0":
 for i in range(52):
  print(J[i])
  print()

elif select == "7":
 for i in range(13):
  print(J[i])
  print()

elif select == "8":
 for i in range(13, 25):
  print(J[i])
  print()

elif select == "9":
 for i in range(25, 38):
  print(J[i])
  print()

elif select == "10":
 for i in range(38, 52):
  print(J[i])
  print()

else:
 sys.exit()
