/** 
Title: Knight vs Rats
Creators: Piper and Kaitlyn
Description: In this game, the player is a knight and your goal 
is to kill and earn points

 */
//  On Start 
info.setLife(3)
info.setScore(0)
//  Player
let knight = sprites.create(img`
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
`)
knight.setKind(SpriteKind.Player)
knight.setPosition(45, 132)
controller.moveSprite(knight, 100, 0)
knight.ay = 100
scene.cameraFollowSprite(knight)
//  Enemy
let bat = sprites.create(img`
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
bat.setKind(SpriteKind.Enemy)
bat.setPosition(90, 132)
let bat2 = sprites.create(img`
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
`)
bat2.setKind(SpriteKind.Enemy)
bat2.setPosition(375, 132)
//  Lose Life
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_overlap(SpriteKind: Sprite, OtherSpriteKind: Sprite) {
    info.changeLifeBy(-1)
})
//  Tilemap
scene.setTileMap(img`
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
`, true)
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
scene.setTile(3, img`
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
`, true)
//  Jump/DoubleJump
let canDoubleJump = true
controller.A.onEvent(ControllerButtonEvent.Pressed, function jump() {
    
    if (canDoubleJump) {
        knight.vy = -50
        canDoubleJump = knight.isHittingTile(CollisionDirection.Bottom)
    }
    
})
game.onUpdate(function on_update() {
    
    if (knight.isHittingTile(CollisionDirection.Bottom)) {
        canDoubleJump = true
    }
    
})
