import pgzrun

WIDTH=700
HEIGHT=490

#map_information(box in 1)
map_data=[[1,0,1,0,0,0,0,1,0,0],
          [1,0,1,1,1,0,1,1,1,0],
          [1,0,0,0,0,0,0,0,0,0],
          [1,1,0,1,1,1,1,1,1,0],
          [0,0,0,1,0,0,0,1,1,0],
          [0,1,1,1,0,1,0,0,0,1],
          [0,0,0,0,0,1,0,1,0,0]]

#player_now_location
location=[0,1]

#player
player=Actor('player',topleft=(70,0))

#floor_tiles
floor=Actor('floor',topleft=(0,0))

#boxes
box=Actor('box',topleft=(0,0))

#exit_signboard
exit=Actor('exit',topleft=(630,420))

def draw():
    screen.clear()
    for y in range(7):
        for x in range(10):
            #floorの描画
            floor.topleft=(70*x, 70*y)
            floor.draw()
            #box
            if map_data[y][x]!=0:
                box.topleft=(70*x,70*y)
                box.draw()
    exit.draw()
    player.draw()

def on_key_down(key):
    if key==keys.UP:
        #player_isn't_top
        if location[0]>=1:
            #player_direction_isn't_boxes_then_go
            if map_data[location[0]-1][location[1]]!=1:
                location[0]-=1
                player.y-=70

    if key==keys.DOWN:
        #player_isn't_bottom
        if location[0]<=5:
            #player_direction_isn't_boxes_then_go
            if map_data[location[0]+1][location[1]]!=1:
                location[0]+=1
                player.y+=70

    if key==keys.LEFT:
        #player_isn't_left.edge
        if location[1]>=1:
            #player_direction_isn't_boxes_then_go
            if map_data[location[0]][location[1]-1]!=1:
                location[1]-=1
                player.x-=70

    if key==keys.RIGHT:
        #player_isn't_right.edge
        if location[1]<=8:
            #player_direction_isn't_boxes_then_go
            if map_data[location[0]][location[1]+1]!=1:
                location[1]+=1
                player.x+=70

pgzrun.go()
