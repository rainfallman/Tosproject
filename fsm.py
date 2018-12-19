from transitions.extensions import GraphMachine

from utils import send_text_message

gender="性別不明"
race="種族不明"
career="初新者"
startitem="空空的行囊"
hp=200
atk=10
defence=10
coin=100
friend=0
bless=0
potion=0

bosshp=800
bossatk=100
bossdef=30

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_test(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'test'
        return False

    
    def is_going_to_setinfo(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            if '開始冒險' in  text.lower():
                sender_id = event['sender']['id']
                responese = send_text_message(sender_id, "有一天,一位自稱是魔王的神祕人突然出現在這安祥和平的世界\n他也放出了許多原本不存在在這世界上的怪異生物,讓大家陷入恐慌之中,於是你決定背起行囊,向這未知的\"魔王\"發起挑戰")
            return '開始冒險' in  text.lower()
        return False

    def is_going_to_setsex(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '性別' in  text.lower()
        return False
    
    def is_going_back_setsex(self, event):
        if event.get("message"):
            text = event['message']['text']
            global gender
            if '男' in  text.lower():
                gender="男性"
            if '女' in  text.lower():
                gender="女性"
            return '男' in  text.lower() or '女' in  text.lower()
        return False

    def is_going_to_setrace(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '種族' in  text.lower()
        return False

    def is_going_back_setrace(self, event):
        if event.get("message"):
            text = event['message']['text']
            global race
            if '人類' in  text.lower():
                race="人類"
            if '精靈' in  text.lower():
                race="精靈"
            if '矮人' in  text.lower():
                race="矮人"
            return '人類' in  text.lower() or '精靈' in  text.lower() or '矮人' in  text.lower()
        return False

    def is_going_to_setitem(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '初始裝備' in  text.lower()
        return False

    def is_going_back_setitem(self, event):
        if event.get("message"):
            text = event['message']['text']
            global startitem
            global coin
            if '紅藥水' in  text.lower():
                startitem="紅藥水"
            if '金幣' in  text.lower():
                startitem="金幣"
                coin+=100
            if '異常解除藥' in  text.lower():
                startitem="異常解除藥"
            return '紅藥水' in  text.lower() or '金幣' in  text.lower() or '異常解除藥' in  text.lower()
        return False

    def is_going_to_setcareer(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '職業' in  text.lower()
        return False

    def is_going_back_setcareer(self, event):
        if event.get("message"):
            text = event['message']['text']
            global career
            global hp
            global atk
            global defence
            if '騎士' in  text.lower():
                career="騎士"
                hp=500
                atk=50
                defence=50
            if '魔法師' in  text.lower():
                career="魔法師"
                hp=350
                atk=80
                defence=40
            if '戰士' in  text.lower():
                career="戰士"
                hp=700
                atk=100
                defence=0
            return '騎士' in  text.lower() or '魔法師' in  text.lower() or '戰士' in  text.lower()
        return False

    def is_going_to_start(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '出發' in  text.lower()
        return False


    def on_enter_test(self, event):
        print("I'm entering state1")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering test")
        self.go_back()

    def on_exit_test(self):
        print('Leaving state1')

    def on_enter_setinfo(self, event):

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "請輸入 \"性別\" \"種族\" \"職業\" \"初始裝備\" 來設定初始狀態 如果全部都設定好了請輸入\"出發\" ")
        
    
    def on_enter_setsex(self, event):

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "請輸入 \"男性\" \"女性\"  ")

        
    def on_exit_setsex(self,event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你選擇的是" +gender)


    def on_enter_setrace(self, event):

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "請輸入 \"人類\" \"精靈\" \"矮人\" ")

    def on_exit_setrace(self,event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你選擇的是" +race)

    def on_enter_setitem(self, event):

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "請輸入 \"紅藥水\" \"金幣\" \"異常解除藥\" ")
    
    def on_exit_setitem(self,event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你選擇的是" +startitem)

    def on_enter_setcareer(self, event):

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "請選擇職業：\n \"騎士\"：血量中等 傷害中等 防禦中等\n\"魔法師\"：血量偏低 傷害高等 防禦中等 \n\"戰士\"：血量高等 傷害高等 防禦極低 ")
    
    def on_exit_setcareer(self,event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你選擇的是" +career)

    def on_enter_start(self, event):

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "於是一位"+gender+"、"+race+"的"+career +",帶著"+startitem+"前去討伐魔王了")
        responese = send_text_message(sender_id, "出發過一陣子之後 你遇到了一個左右的岔路 請問你要\"往左走\"還是\"往右走\"呢？ ")
    


    #初始狀態設定完成 接下來出發打boss
    def is_going_to_turnleft(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '往左走' in  text.lower()
        return False

    def is_going_to_turnright(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '往右走' in  text.lower()
        return False

    def on_enter_turnleft(self, event):

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你在這裡這裡發現了一具冒險者的屍體,看上去死相很慘,但是你發現他緊抱著一個背包,裏面或許會有有用的東西,請問你要\"打開\"背包 ,還是選擇當作沒看到,\"無視\"這個背包呢")


    def is_going_to_search(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '打開' in  text.lower()
        return False

    def is_going_to_nosearch(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '無視' in  text.lower()
        return False

    def on_enter_search(self, event):
        global hp
        print("open")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你下定決心鼓起勇氣打開了背包,卻因為背包打開後傳出了如地獄般的惡臭,讓你感到身體非常的不舒服,吐的滿地都是\n因為聞到了惡臭導致嘔吐 血量下降50點 於是你在原地稍做休息之後\"繼續上路\"")
        hp-=50
        self.advance(event)
   
    def on_enter_nosearch(self, event):

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你覺得大體為重,不應該打擾,所以你無視了背包\"繼續上路\"")
        self.advance(event)

    def on_enter_turnright(self, event):

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你發現了一位冒險者正被魔物襲擊,看上去情況很危急,請問你要選擇\"幫助\"這位冒險者 ,還是選擇當作沒看到,\"無視\"這位冒險者")

    def is_going_to_save(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '幫助' in  text.lower()
        return False

    def is_going_to_nosave(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '無視' in  text.lower()
        return False

    def on_enter_save(self, event):
        global friend
        friend+=1
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你決定幫助這位無助的冒險者,成功的把魔物擊退了,冒險者為了報答你的救命之恩,所以決定跟你一起去討伐魔王,於是你與這位冒險者組成了一支隊伍準備\"繼續上路\"")
        self.advance(event)
        
   
    def on_enter_nosave(self, event):

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你覺得別人的事情不關你的事,所以你就無視那位冒險者的求救徑自離開了現場,不久之後你就聽到了悽慘的哀嚎聲,但是你無情的頭也不回的\"繼續上路\"")
        self.advance(event)

    """
    def is_going_to_town(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '繼續上路' in  text.lower()
        return False
    """
    def on_enter_town(self, event):

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你繼續旅行,來到了一座小鎮\n這座小鎮看上去很和平,似乎沒有被魔王侵略過\n你繞了小鎮一圈,發現有一間旅館跟一間道具店,因為你在趕路,所以你只能選擇進入\"旅館\"稍微休息一下 或是在\"道具店\"買些東西來幫助冒險")
    
    #進入小鎮 小鎮事件

    def is_going_to_hotel(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '旅館' in  text.lower()
        return False

    def on_enter_hotel(self, event):
        global friend
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你走進旅館,用一點小錢租了一間房間一晚,打算稍微休息一夜之後再繼續上路")
        if friend>0:
            responese = send_text_message(sender_id, "由於先前你救了你的伙伴一命,所以晚上的時候你與你的伙伴發生了不可描述之事")
        responese = send_text_message(sender_id, "於是你度過了一個平和的夜晚,到早上時你整理好你的行囊,準備\"繼續上路\"")
        self.advance(event)

    def is_going_to_store(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '道具店' in  text.lower()
        return False

    def on_enter_store(self, event):
        global coin
        global race
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你走進了道具店,店裡琳琅滿目的神奇商品讓你似乎忘記了時間,直到店主人呼喚你你才終於回過神來")
        responese = send_text_message(sender_id, "我這裡有一瓶魔法藥水,你需要這瓶神奇的\"魔法藥水\"嗎？（效果不明）")
        responese = send_text_message(sender_id, "或是如果你想要祝福的話.我知道一種古老的咒語能讓你身體機能更厲害,能讓你的冒險更加順利,你想要我幫你施加古老的\"祝福\"嗎？")
        if race=="精靈" :
            responese = send_text_message(sender_id, "我看客人你跟我一樣都是精靈族,所以我可以給你一個\"神祕禮物\" 你想要這神祕的禮物嗎？")
        if coin>150 :
            responese = send_text_message(sender_id, "嗯.....我聽到你的口袋裡有不少錢 如果你願意給我你口袋的錢的話,我可以幫你把你的武器\"升級\"到更高的等級喔")
        
    def is_going_to_update(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '升級' in  text.lower()
        return False

    def is_going_to_bless(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '祝福' in  text.lower()
        return False

    def is_going_to_magicpotion(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '魔法藥水' in  text.lower()
        return False

    def is_going_to_storehidden(self, event):
        if event.get("message"):
            text = event['message']['text']
            return '神祕禮物' in  text.lower()
        return False

    def on_enter_update(self, event):
        global coin
        global atk
        global defence
        coin=0
        atk+=50
        defence+=30
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "於是你把身上所有的錢跟你的武器交給了店主,只看見店主開始施法,讓空氣中的魔力凝聚在武器上面,過了3小時後,店主把武器還給了你,並說： 我已經幫你把你的武器升級好了,這下你的冒險應該會更加輕鬆 \n你接過武器,向店主道謝之後走出了商店街,準備好\"繼續上路\"")
        self.advance(event)

    def on_enter_bless(self,event):
        global bless
        global atk
        global defence
        bless=1
        atk+=30
        defence+=15
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "於是你讓店主在你身上施加祝福,只看見店主開始施法,讓空氣中的魔力凝聚在你的身體上面,過了1、2小時後,店主說： 我已經在你身上施加了古老的祝福,這下你已經不會被任何的惡魔所魅惑或洗腦控制了,於是你向店主道謝之後走出了商店街,準備好\"繼續上路\"")
        self.advance(event)

    def on_enter_magicpotion(self,event):
        global coin
        global potion
        coin-=50
        potion=1
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "於是你向店主購買了那瓶神奇的魔法藥水,只看見這瓶藥水在店裡的光照之下顯的清澈透明,於是你向店主道謝之後把藥水放進了背包裏面,走出了商店街,準備好\"繼續上路\"")
        self.advance(event)

    def on_enter_storehidden(self,event):
        global hp
        global atk
        global defence
        hp+=200
        atk+=50
        defence+=30
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你向店主要了所謂的神祕禮物,只看見店主拿出了一瓶藥水要你喝下,店主說：這是我們精靈族的密傳密藥,喝了不僅可以更加延長飲用者的壽命,更可以使人的所有身體機能大幅提升\n於是你接過瓶子大口喝下,你喝下之後發現你的身體能力明顯的上升了許多,於是你向店主道謝之後,走出了商店街,準備好\"繼續上路\"")
        self.advance(event)

    """
    def is_going_to_cave(self,event):
        if event.get("message"):
            text = event['message']['text']
            return '繼續上路' in  text.lower()
        return False
    """
    def on_enter_cave(self,event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "於是你繼續你的討伐魔王之旅 之後遇到了一個山洞,地圖上說這座山洞是通往魔王所在地的捷徑,但是由於山洞非常的漆黑,你也不知道裏面有甚麼東西,所以你猶豫著是否要\"進入\"這座山洞走捷徑去打魔王,還是選擇\"繞道\",找其他的路")

#命運石之洞的選擇
    def is_going_to_chest(self,event):
        if event.get("message"):
            text = event['message']['text']
            return '進入' in  text.lower()
        return False

    def is_going_to_otherpath(self,event):
        if event.get("message"):
            text = event['message']['text']
            return '繞道' in  text.lower()
        return False

    def is_going_to_chestopen(self,event):
        if event.get("message"):
            text = event['message']['text']
            return '打開寶箱' in  text.lower()
        return False

    def is_going_to_take(self,event):
        if event.get("message"):
            text = event['message']['text']
            return '拿走' in  text.lower()
        return False

    def is_going_to_notake(self,event):
        if event.get("message"):
            text = event['message']['text']
            return '放棄' in  text.lower()
        return False

    def is_going_to_chestno(self,event):
        if event.get("message"):
            text = event['message']['text']
            return '不打開' in  text.lower()
        return False

    def on_enter_chest(self,event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "於是你鼓起勇氣進入了山洞,由於山洞內部很黑,所以你只能慢慢的一步步摸索,後來你在洞穴出口附近發現了一個寶箱,你猶豫著是否要\"打開寶箱\"還是\"不打開\"寶箱")

    def on_enter_chestopen(self,event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你好奇的打開寶箱,發現裏面放著一大堆的珠寶跟金幣,價值大概夠你與你的後代活好幾輩子,突然你萌生了拿走這些錢財之後過著隱世的生活,甚麼魔王的管他去死,你是否要\"拿走\"這些錢財過隱世的生活,還是你要為了大義,\"放棄\"這些錢財去討伐魔王")

    def on_enter_take(self,event):
        global friend
        sender_id = event['sender']['id']
        if friend>0:
            responese = send_text_message(sender_id,"於是你決定把這些錢財拿走,與你身旁的冒險者伙伴過著隱世的日子,沒有人知道後來你們在哪裡,去了哪裡\n END")
        if friend==0:
            responese = send_text_message(sender_id,"於是你決定把這些錢財拿走,獨自過著隱世的生活,最後孤獨的活著,終老一生\n END")

    def on_enter_notake(self,event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id,"你揮去了心中的雜念,你心想,我是為了討伐魔王才踏上此旅途,不是為了錢財,我不能被這種東西誘惑\n於是你把寶箱閤上,走出了洞穴")
        self.advance(event)

    def on_enter_chestno(self,event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id,"你覺得寶箱可能有詐,所以你無視了寶箱,直接往洞穴出口走去")
        self.advance(event)

    def on_enter_otherpath(self,event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id,"你覺得已經接近魔王所在地了,洞穴裏面有可能會有魔王的手下在埋伏,所以你決定不走洞穴,你選擇了繞道而行")
        self.advance(event)

    def on_enter_smallboss(self,event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id,"你費盡千辛萬苦終於來到魔王城的大門\n你推開了沈重的魔王城大門,發現迎接你的不是魔王,而是魔王忠心耿耿的手下,魅魔-西思那\n她阻擾著你前進去打倒魔王,你思考著該如何突破她")
        if friend>0 :
            responese = send_text_message(sender_id,"\"伙伴\" ：請伙伴迎戰這傢伙,自己趁對面不注意時突破她的防線")
        if potion>0 :
            responese = send_text_message(sender_id,"\"藥水\" ：對她丟出那瓶神奇的魔法藥水")
        responese = send_text_message(sender_id,"\"硬上\" ：不管後果如何,直接衝上前去跟她拼了！！！")

#小boss戰鬥

    def is_going_to_potionatk(self,event):
        if event.get("message"):
            text = event['message']['text']
            return '藥水' in  text.lower()
        return False

    def is_going_to_friendatk(self,event):
        if event.get("message"):
            text = event['message']['text']
            return '伙伴' in  text.lower()
        return False

    def is_going_to_justatk(self,event):
        if event.get("message"):
            text = event['message']['text']
            return '硬上' in  text.lower()
        return False

    def on_enter_potionatk(self,event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id,"於是你朝對手丟出了精靈商人賣給你的魔法藥水,沒想到魔法藥水砸到魅魔之後藥水居然凝固了,活生生的把魅魔給固定住了,於是你毫髮無傷的通過了這關")
        self.advance(event)

    def on_enter_friendatk(self,event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id,"你的伙伴跳了出來,想盡辦法的吸引住魅魔的注意,而你在魅魔的一個閃神時,一口氣突破了魅魔的防線")
        self.advance(event)

    def on_enter_justatk(self,event):
        global bless
        global startitem
        global hp
        global atk
        global defence
        sender_id = event['sender']['id']
        if bless>0 :
            responese = send_text_message(sender_id,"由於你受過古老祝福的保護,魅魔的各種魅惑或洗腦攻擊都沒有效果,所以你無視她的攻擊直接走向魔王的房間")
        if bless==0 and startitem=='異常解除藥' :
            responese = send_text_message(sender_id,"你艱難的戰勝了魅魔,雖然你中了魅魔的魅惑,但是還好你有著異常解除藥,所以沒有太大的損傷")
            hp-=200
        if bless==0 and startitem!='異常解除藥' :
            responese = send_text_message(sender_id,"你艱難的戰勝了魅魔,但是你中了魅魔的魅惑,導致你的力量下降,防禦力也下降了")
            hp-=200
            atk-=30
            defence-=20
        self.advance(event)

#bossfight

    def is_going_to_win(self,event):
        global atk
        global bosshp
        global hp
        global bossatk
        global defence
        global bossdef
        if event.get("message"):
            text = event['message']['text']
            sender_id = event['sender']['id']
            if '一般攻擊' in text.lower() and bosshp>0 and hp>0:
                bosshp=bosshp-(atk-bossdef)
                hp=hp-(bossatk-defence)
            if '防守攻擊' in text.lower() and bosshp>0 and hp>0:
                bosshp=bosshp-(atk*0.8-bossdef)
                hp=hp-(bossatk-defence*1.4)
            if '捨命攻擊' in text.lower() and bosshp>0 and hp>0:
                bosshp=bosshp-(atk*2-bossdef)
                hp=hp-(bossatk-defence*0.1)
            if bosshp>0 and hp>0:
                responese = send_text_message(sender_id,"魔王還剩下"+str(bosshp)+"血量")
                responese = send_text_message(sender_id,"你還剩下"+str(hp)+"血量")
            responese = send_text_message(sender_id,"\"一般攻擊\"：一般性的攻擊\n\"防守攻擊\"：邊防禦邊攻擊 增加防禦減少一些傷害\n\"捨命攻擊\"：放棄防禦,全力攻擊\n")

            
            return bosshp<=0
        return False

    def is_going_to_lose(self,event):
        global hp
        if hp<=0:
            return True
        return False

    def on_enter_boss(self,event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id,"終於你到了魔王的面前,你緊握手中的武器,向魔王發起了挑戰")
        responese = send_text_message(sender_id,"\"一般攻擊\"：一般性的攻擊\n\"防守攻擊\"：邊防禦邊攻擊 增加防禦減少一些傷害\n\"捨命攻擊\"：放棄防禦,全力攻擊\n")

    def on_enter_win(self,event):
        global friend
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id ,"你戰勝魔王,成功的阻止魔王毀滅世界")
        if friend >0 :
            responese = send_text_message(sender_id ,"回到城鎮之後,你與你一同挑戰魔王的冒險者一起生下了孩子,從此過著幸福快樂的日子")

    def on_enter_lose(self,event):
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id,"魔王打敗你了,再也沒有人能夠阻止魔王的野心了")

    def is_going_to_reset(self,event):
        global gender
        global race
        global career
        global startitem
        global hp
        global atk
        global defence
        global coin
        global friend
        global bless
        global potion
        global bosshp
        global bossatk
        global bossdef
        if 'reset' in  text.lower() :
            gender="性別不明"
            race="種族不明"
            career="初新者"
            startitem="空空的行囊"
            hp=200
            atk=10
            defence=10
            coin=100
            friend=0
            bless=0
            potion=0
            bosshp=800
            bossatk=100
            bossdef=30
            if event.get("message"):
                text = event['message']['text']
                sender_id = event['sender']['id']
                responese = send_text_message(sender_id,"reset")
                return 'reset' in  text.lower()
        else :
            return False


