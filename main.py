"""
Title: Knight vs Rats
Creators: Piper and Kaitlyn
Description: In this game, the player is a knight and your goal 
is to kill and earn points
"""
# On Start 
info.set_life(3) 
info.set_score(0) 
# Player
knight= sprites.create(img("""
    ....................
    ....................
    ....................
    ....................
    ....................
    ....................
    ...ff.ffffff........
    ..f33fbbccccf.......
    ..f3fbbcbbbbcf......
    ...ffbcbfbbfbf......
    ...fbcbbfbbfbf......
    ...fbcbbfbbfbf......
    ....ffbbfbbfbf......
    ...fffbbbbbbbf......
    ..fcbbfbbbbbf.......
    .fbcbcbffffff.......
    .fffffbbbcccf.......
    ..fccfbbbbbcf.......
    ..fcbfbbbbbff.......
    ..fbbbfbbbcfbf......
    ..fbbcfbcccfcf......
    ..fbccfbffffcf......
    ...fffbbbfbff.......
    .....fbbbfbf........
    ....fbbbbfbf........
    ....fbbccfcf........
    ....fcccccfcf.......
    ....fffffffff.......
    ....................
    ....................
""")) 
knight.set_kind(SpriteKind.player)
knight.set_position(45, 132)
controller.move_sprite(knight, 100, 0)
knight.ay = 100
scene.camera_follow_sprite(knight) 
# Enemy
bat= sprites.create(img("""
    . . f f f . . . . . . . . . . .
    f f f c c . . . . . . . . f f f
    f f c c c . c c . . . f c b b c
    f f c 3 c c 3 c c f f b b b c .
    f f c 3 b c 3 b c f b b c c c .
    f c b b b b b b c f b c b c c .
    c c 1 b b b 1 b c b b c b b c .
    c b b b b b b b b b c c c b c .
    c b 1 f f 1 c b b c c c c c . .
    c f 1 f f 1 f b b b b f c . . .
    f f f f f f f b b b b f c . . .
    f f 2 2 2 2 f b b b b f c c . .
    . f 2 2 2 2 2 b b b c f . . . .
    . . f 2 2 2 b b b c f . . . . .
    . . . f f f f f f f . . . . . .
    . . . . . . . . . . . . . . . .
""")) 
bat.set_kind(SpriteKind.enemy) 
bat.set_position(90, 132) 

bat2=sprites.create(img("""
    . f f f . . . . . . . . f f f .
    f f c . . . . . . . f c b b c .
    f c c . . . . . . f c b b c . .
    c f . . . . . . . f b c c c . .
    c f f . . . . . f f b b c c . .
    f f f c c . c c f b c b b c . .
    f f f c c c c c f b c c b c . .
    . f c 3 c c 3 b c b c c c . . .
    . c b 3 b c 3 b b c c c c . . .
    c c b b b b b b b b c c . . . .
    c 1 1 b b b 1 1 b b b f c . . .
    f b b b b b b b b b b f c c . .
    f b c b b b c b b b b f . . . .
    . f 1 f f f 1 b b b c f . . . .
    . . f b b b b b b c f . . . . .
    . . . f f f f f f f . . . . . .
"""))
bat2.set_kind(SpriteKind.enemy)
bat2.set_position(375,132)

# Coins 
coin = sprites.create(img("""
    . . b b b b . .
    . b 5 5 5 5 b .
    b 5 d 3 3 d 5 b
    b 5 3 5 5 1 5 b
    c 5 3 5 5 1 d c
    c d d 1 1 d d c
    . f d d d d f .
    . . f f f f . .
""")) 
coin.set_kind(SpriteKind.food)
def on_overlap3(sprite, otherSprite):
    coin.destroy()
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_overlap3)

# Lose Life
def on_overlap(sprite, otherSprite):
    sprite.set_position(knight.x - 30, knight.y-20)
    scene.camera_shake()
    info.change_life_by(-1)

def on_button_event_b_pressed():
    projectile = sprites.create_projectile_from_sprite(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . d d . . . . . .
        . . . . . . . d b d . . . . . .
        . . . . f . d b d . . . . . . .
        . . . . . f d d . . . . . . . .
        . . . . f f f . . . . . . . . .
        . . . f f f . f . . . . . . . .
        . . . 3 f . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """), knight, 50, 0)
controller.player1.on_button_event(ControllerButton.B, ControllerButtonEvent.PRESSED, on_button_event_b_pressed)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap)

def on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_overlap2)

# Tilemap
scene.set_tile_map(img("""
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    .................................5................
    ...................................333.....2......
    .................................3......3..3......
    ......5.................5.......33............55.1
    ................2..............333...............1
    ccccccccccc...cccccccccccccccccccc..........cccccc
    ccccccccccc444cccccccccccccccccccc4444444444cccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccc
"""))
scene.set_tile(5, img("""
    . . . . . . . .
    . . . . . . . .
    . . . . . . . .
    . . . . . . . .
    . . . . . . . .
    . . . . . . . .
    . . . . . . . .
    . . . . . . . .
"""))
scene.set_tile(12, img("""
    a a a c c a a a a a a c c a a a
    3 3 3 3 c 3 3 3 3 3 3 3 c 3 3 3
    3 3 3 a c 3 3 3 3 3 3 3 c 3 3 3
    a a a a c a a a a a a a c c a a
    c c c c c c c c c c c c c c c c
    c a 3 3 3 3 3 a c a 3 3 3 3 3 a
    c c a a a a a a c c a a a a a a
    c c c c c c c c c c c c c c c c
    a a a c a a a a a a a a c a a a
    a a a c c a a a a a a a c a a a
    c c c c c c c c c c c c c c c c
    c a a a a a a c c a a a a a a c
    c c c c c c c c c c c c c c c c
    a a c c a a a a a a c c a a a a
    c c c c c c c c c c c c c c c c
    c c c c c c c c c c c c c c c c
"""), True)
scene.set_tile(4, img("""
    5 4 4 5 5 4 4 4 4 2 2 2 4 4 4 4
    4 4 4 4 4 5 5 4 2 2 2 2 4 4 4 5
    4 2 2 2 4 4 5 4 2 2 4 4 5 5 5 5
    2 2 4 2 4 4 5 4 2 2 4 5 5 5 5 4
    2 2 2 2 4 4 5 4 2 2 4 4 5 5 4 4
    4 2 2 2 4 5 5 4 4 4 4 4 4 4 4 2
    2 2 2 4 4 5 5 5 4 4 2 2 2 2 2 2
    4 2 2 4 5 5 5 5 4 2 2 4 2 2 2 4
    5 4 4 4 4 4 4 5 5 4 2 2 2 4 4 4
    4 4 4 2 2 2 4 4 5 5 4 4 4 4 5 5
    4 2 2 2 2 2 2 2 4 5 5 5 5 5 5 5
    5 4 4 2 4 2 2 4 4 5 5 5 4 4 4 5
    5 5 4 2 2 2 4 4 4 5 5 4 2 2 2 4
    4 5 4 4 4 4 5 5 5 5 4 2 4 2 2 4
    4 5 5 5 5 5 5 4 4 4 2 4 2 4 2 4
    4 5 5 5 4 4 4 4 2 2 2 2 4 2 4 4
"""))
scene.set_tile(2, img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
""")) 
scene.set_tile(3, img("""
    b d d d d d d c b d d d d d d c
    d b b b b b b c d b b b b b c c
    d b b b b b b c d b b b b c b c
    d b b b b b b c d b b b d d b c
    d b b b b b b c d b b c b b b c
    d b b b b b b c d b c c b b b c
    d b b b b b b b d b c c b b b b
    c c c c c c b a c c c c c c b a
    b d d d d d d c b d d d d d d c
    d b b b b b b c d b b b b b b c
    d b b b b b b c d b b b b b b c
    d b b b b b b c d b b b b b b c
    d b b b b b c c d b b b b b b c
    d b b b b c c c d b b b b b b c
    d b b b b c c b d b b b b b b b
    c c c c c c c a c c c c c c c a
"""), True) 
scene.place_on_random_tile(coin, 5)

# Jump/DoubleJump
canDoubleJump = True
def jump():
    global canDoubleJump
    if canDoubleJump:
        knight.vy = -50
        canDoubleJump = knight.is_hitting_tile(CollisionDirection.BOTTOM)
controller.A.on_event(ControllerButtonEvent.PRESSED, jump)

def on_update():
    global canDoubleJump
    if knight.is_hitting_tile(CollisionDirection.BOTTOM):
        canDoubleJump = True
game.on_update(on_update)
