/** 
Title: Knight vs Rats
Creators: Piper and Kaitlyn
Description: In this game, the player is a knight and your goal 
is to kill 

 */
//  On Start 
info.setLife(3)
info.setScore(0)
let knight = sprites.create(img`
    . . . . 3 3 3 3 3 3 . . . . . .
    . . . . 3 . . . . 3 . . . . . .
    . . . 3 3 . . . . 3 . . . . . .
    . . . 3 3 3 3 . . 3 . . . . . .
    . . . . . . 3 3 3 3 . . . . . .
    . . . . . . 3 3 . . . . . . . .
    . . . . . . 3 3 . . . . . . . .
    . . . . . . 3 3 . . . . . . . .
    . . . . . 3 3 3 . . . . . . . .
    . . . . . 3 3 3 . . . . . . . .
    . . . . . 3 . 3 . . . . . . . .
    . . . . 3 3 . 3 . . . . . . . .
    . . . . 3 . . 3 . . . . . . . .
    . . . . 3 . . 3 3 . . . . . . .
    . . . 3 3 . . . 3 . . . . . . .
    . . . 3 . . . . 3 3 . . . . . .
`)
knight.setPosition(45, 136)
controller.moveSprite(knight)
scene.cameraFollowSprite(knight)
scene.setTileMap(img`
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    .................................5.333............
    ...........................................2......
    .................................3......3..3......
    ......5.................5.......33............55.1
    .....d..........2.....d........333...............1
    ccccccccccc...cccccccccccccccccccc..........cccccc
    ccccccccccc444cccccccccccccccccccc4444444444cccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccc
`)
scene.setTile(5, img`
    . . b b b b . .
    . b 5 5 5 5 b .
    b 5 d 3 3 d 5 b
    b 5 3 5 5 1 5 b
    c 5 3 5 5 1 d c
    c d d 1 1 d d c
    . f d d d d f .
    . . f f f f . .
`)
scene.setTile(12, img`
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
`)
scene.setTile(4, img`
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
`)
scene.setTile(13, img`
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
`)
scene.setTile(2, img`
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
`)
let bat = sprites.create(img`
    . . f f f . . . . . . . . f f f
    . f f c c . . . . . . f c b b c
    f f c c . . . . . . f c b b c .
    f c f c . . . . . . f b c c c .
    f f f c c . c c . f c b b c c .
    f f c 3 c c 3 c c f b c b b c .
    f f b 3 b c 3 b c f b c c b c .
    . c 1 b b b 1 b c b b c c c . .
    . c 1 b b b 1 b b c c c c . . .
    c b b b b b b b b b c c . . . .
    c b 1 f f 1 c b b b b f . . . .
    f f 1 f f 1 f b b b b f c . . .
    f f 2 2 2 2 f b b b b f c c . .
    . f 2 2 2 2 b b b b c f . . . .
    . . f b b b b b b c f . . . . .
    . . . f f f f f f f . . . . . .
`)
