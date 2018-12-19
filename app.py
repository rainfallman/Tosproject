from bottle import route, run, request, abort, static_file
import os
from fsm import TocMachine


VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
machine = TocMachine(
    states=[
        'user',
        'test',
        'setinfo',
            'setsex',
            'setcareer',
            'setitem',
            'setrace',
        'start',
            'turnleft',
                'search',
                'nosearch',
            'turnright',
                'save',
                'nosave',
        'town',
            'hotel',
            'store',
                'update',
                'magicpotion',
                'bless',
                'storehidden',
        'cave',
            'chest',
                'chestopen',
                    'take',
                    'notake',
                'chestno',
            'otherpath',
        'smallboss',
            'potionatk',
            'friendatk',
            'justatk',
        'boss',
        'win',
        'lose'

    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'test',
            'conditions': 'is_going_to_test'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'setinfo',
            'conditions': 'is_going_to_setinfo'
        },
        {
            'trigger': 'advance',
            'source': 'setinfo',
            'dest': 'setsex',
            'conditions': 'is_going_to_setsex'
        },
        {
            'trigger': 'advance',
            'source': 'setinfo',
            'dest': 'setrace',
            'conditions': 'is_going_to_setrace'
        },
        {
            'trigger': 'advance',
            'source': 'setinfo',
            'dest': 'setcareer',
            'conditions': 'is_going_to_setcareer'
        },
        {
            'trigger': 'advance',
            'source': 'setinfo',
            'dest': 'setitem',
            'conditions': 'is_going_to_setitem'
        },
        {
            'trigger': 'advance',
            'source': 'setsex',
            'dest': 'setinfo',
            'conditions': 'is_going_back_setsex'
        },
        {
            'trigger': 'advance',
            'source': 'setrace',
            'dest': 'setinfo',
            'conditions': 'is_going_back_setrace'
        },
        {
            'trigger': 'advance',
            'source': 'setcareer',
            'dest': 'setinfo',
            'conditions': 'is_going_back_setcareer'
        },
        {
            'trigger': 'advance',
            'source': 'setitem',
            'dest': 'setinfo',
            'conditions': 'is_going_back_setitem'
        },
        {
            'trigger': 'advance',
            'source': 'setinfo',
            'dest': 'start',
            'conditions': 'is_going_to_start'
        },
        #初始部份結束 下面是冒險過程
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'turnleft',
            'conditions': 'is_going_to_turnleft'
        },
        {
            'trigger': 'advance',
            'source': 'turnleft',
            'dest': 'search',
            'conditions': 'is_going_to_search'
        },
        {
            'trigger': 'advance',
            'source': 'turnleft',
            'dest': 'nosearch',
            'conditions': 'is_going_to_nosearch'
        },
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'turnright',
            'conditions': 'is_going_to_turnright'
        },
        {
            'trigger': 'advance',
            'source': 'turnright',
            'dest': 'save',
            'conditions': 'is_going_to_save'
        },
        {
            'trigger': 'advance',
            'source': 'turnright',
            'dest': 'nosave',
            'conditions': 'is_going_to_nosave'
        },
        {
            'trigger': 'advance',
            'source': [
                'search',
                'nosearch',
                'save',
                'nosave',
            ],
            'dest': 'town'
        },
        #小鎮的選擇
        {
            'trigger': 'advance',
            'source': 'town',
            'dest': 'hotel',
            'conditions': 'is_going_to_hotel'
        },
        {
            'trigger': 'advance',
            'source': 'town',
            'dest': 'store',
            'conditions': 'is_going_to_store'
        },
        {
            'trigger': 'advance',
            'source': 'store',
            'dest': 'update',
            'conditions': 'is_going_to_update'
        },
        {
            'trigger': 'advance',
            'source': 'store',
            'dest': 'magicpotion',
            'conditions': 'is_going_to_magicpotion'
        },
        {
            'trigger': 'advance',
            'source': 'store',
            'dest': 'storehidden',
            'conditions': 'is_going_to_storehidden'
        },
        {
            'trigger': 'advance',
            'source': 'store',
            'dest': 'bless',
            'conditions': 'is_going_to_bless'
        },
        {
            'trigger': 'advance',
            'source': [
                'hotel',
                'update',
                'magicpotion',
                'storehidden',
                'bless'
            ],
            'dest': 'cave'
        },
        #山洞與捷徑的選擇
        {
            'trigger': 'advance',
            'source': 'cave',
            'dest': 'chest',
            'conditions': 'is_going_to_chest'
        },
        {
            'trigger': 'advance',
            'source': 'cave',
            'dest': 'otherpath',
            'conditions': 'is_going_to_otherpath'
        },
        {
            'trigger': 'advance',
            'source': 'chest',
            'dest': 'chestopen',
            'conditions': 'is_going_to_chestopen'
        },
        {
            'trigger': 'advance',
            'source': 'chestopen',
            'dest': 'take',
            'conditions': 'is_going_to_take'
        },
        {
            'trigger': 'advance',
            'source': 'chestopen',
            'dest': 'notake',
            'conditions': 'is_going_to_notake'
        },
        {
            'trigger': 'advance',
            'source': 'chest',
            'dest': 'chestno',
            'conditions': 'is_going_to_chestno'
        },
        {
            'trigger': 'advance',
            'source': [
                'chestno',
                'notake',
                'otherpath'
            ],
            'dest': 'smallboss'
        },
        #小boss戰鬥
        {
            'trigger': 'advance',
            'source': 'smallboss',
            'dest': 'potionatk',
            'conditions': 'is_going_to_potionatk'
        },
        {
            'trigger': 'advance',
            'source': 'smallboss',
            'dest': 'friendatk',
            'conditions': 'is_going_to_friendatk'
        },
        {
            'trigger': 'advance',
            'source': 'smallboss',
            'dest': 'justatk',
            'conditions': 'is_going_to_justatk'
        },
        {
            'trigger': 'advance',
            'source': [
                'potionatk',
                'friendatk',
                'justatk'
            ],
            'dest': 'boss'
        },
        {
            'trigger': 'advance',
            'source': 'boss',
            'dest': 'win',
            'conditions': 'is_going_to_win'
        },
        {
            'trigger': 'advance',
            'source': 'boss',
            'dest': 'lose',
            'conditions': 'is_going_to_lose'
        },
        {
            'trigger': 'go_back',
            'source': [
                'test'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


#@route('/show-fsm', methods=['GET'])
#def show_fsm():
#    machine.get_graph().draw('fsm.png', prog='dot', format='png')
#    return static_file('fsm.png', root='./', mimetype='image/png')

PORT =os.environ['PORT']
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
