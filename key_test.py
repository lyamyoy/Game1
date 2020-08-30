import pgzrun

def on_key_down(key):
    print('何かキーが押されました')
    if key==keys.UP:
        print('上矢印押された')

    if key==keys.DOWN:
        print('下矢印押された')

    if key==keys.LEFT:
        print('左矢印押された')

    if key==keys.RIGHT:
        print('右矢印押された')

    print()

pgzrun.go()


    

