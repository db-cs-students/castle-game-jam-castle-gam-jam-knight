"""
Title: Knight vs bats
Creators: Piper and Kaitlyn
Description: In this game, the player is a knight and your goal 
is to kill and earn points
"""
# On Start 
scene.set_background_image(img("""
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb1bb1bbb1bb1bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb1bb1bbb1bb1bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb111b11111b111bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb111b11111b111bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb111111212111111bbbbbbbbbbbbbbbbbbbbbbbbbbbbb111111212111111bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb11111111111111111bbbbbbbbbbbbbbbbbbbbbbbbbbb11111111111111111bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb111b111111111b111bbbbbbbbbbbbbbbbbbbbbbbbbbb111b111111111b111bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb11bbb1111111bbb11bbbbbbbbbbbbbbbbbbbbbbbbbbb11bbb1111111bbb11bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb1bbbbb11111bbbbb1bbbbbbbbbbbbbbbbbbbbbbbbbbb1bbbbb11111bbbbb1bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb1b1bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb1b1bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbccbccbccbccbcccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbcbbcddcddcbbcbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbdddddddddddbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbdddddddddddddbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbddbddbddbddbdbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcb.bb.bb.bb.bb.bbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbddbddbddbddbdbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbcbcccbddddddddddddddbcccbcbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbcbcbccbddddddddddddddbccbcbcbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbdbcbbddddddccddddddbbcbdbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbddbcbbdddddcffbdddddbbcbddbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbdddbcbbddddcffeebddddbbcbdddbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbdddbcbbddddcfeeebddddbbcbdddbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbdddbbbbddddcfeeebddddbbbbdddbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbdddbbbbddddcfeeebddddbbbbdddbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbdddbbbbddddcfeeebddddbbbbdddbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbdddbbbbddddcfeeebddddbbbbdddbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbdddbbbbddddcfeeebddddbbbbdddbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbcccbbbbccccb4441dccccbbbbcccbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbcccbbbbccccb4441dccccbbbbcccbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbcccbbbbccccb4441dccccbbbbcccbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbcccbbbbccccb4441dccccbbbbcccbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbcccbbbbccccb4441dccccbbbbcccbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbcccbdbbccccb4441dccccbbdbcccbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbcccbdbbccccb4411dccccbbdbcccbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbccbdbbcccccb11dcccccbbdbccbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbcbdbbccccccddccccccbbdbcbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbdbdbdbbccccccccccccccbddbdbdbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddbdbdddbccccccccccccccbdddbdbddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbcbccbccbccbccbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbb.bb.bb.bb.bb.bdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbcbccbccbccbccbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbcccccccccccccbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbcccccccccccbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbdbbdccdccdbbdbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddbddbddbddbddbddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbfffffbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbfffffbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbfffffffbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbfffffffbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbfffffffffbfffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbfffffffffbfffbbbbbbbbbbbbbbbbbbbbbbbbbbbfffffffffffffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffffffffffffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffff2f2ffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffff2f2ffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbfffffbfffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbfffffbfffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbfbbbfbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbfbbbfbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
"""))
game.splash("press A to start")
game.splash("controles: A to jump")
game.splash("use A twice to double Jump")
game.splash("B to shoot")
game.splash("dont die!")
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
animation.run_image_animation(knight,
 [img("""
     ....................
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
     ...ffffbbbbff.......
     ......fbbfbf........
     .....fcbfcbf........
     ....fccbffbf........
     ....fccf.fccf.......
     ....fcf..fcccf......
     ....ff...fffff......
 """), 
 img("""
     ....................
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
 """), 
 img("""
 """)], 
 0,
 True)

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



# win game 
door = sprites.create(img("""
    . . . . c c c c c c c c . . . .
    . . . c f f b e e e e e 1 . . .
    . . c f f b e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
""")) 
tiles.place_on_random_tile(None, img("""
    . . . . c c c c c c c c . . . .
    . . . c f f b e e e e e 1 . . .
    . . c f f b e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
    . . c f b e e e e e e e e 1 . .
"""))

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
coin2 = sprites.create(img("""
    . . b b b b . .
    . b 5 5 5 5 b .
    b 5 d 3 3 d 5 b
    b 5 3 5 5 1 5 b
    c 5 3 5 5 1 d c
    c d d 1 1 d d c
    . f d d d d f .
    . . f f f f . .
"""))
coin3 = sprites.create(img("""
    . . b b b b . .
    . b 5 5 5 5 b .
    b 5 d 3 3 d 5 b
    b 5 3 5 5 1 5 b
    c 5 3 5 5 1 d c
    c d d 1 1 d d c
    . f d d d d f .
    . . f f f f . .
"""))
coin4 = sprites.create(img("""
    . . b b b b . .
    . b 5 5 5 5 b .
    b 5 d 3 3 d 5 b
    b 5 3 5 5 1 5 b
    c 5 3 5 5 1 d c
    c d d 1 1 d d c
    . f d d d d f .
    . . f f f f . .
"""))
coin5 = sprites.create(img("""
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
coin2.set_kind(SpriteKind.food)
coin3.set_kind(SpriteKind.food)
coin4.set_kind(SpriteKind.food)
coin5.set_kind(SpriteKind.food)
def on_overlap3(sprite, otherSprite):
    otherSprite.destroy()
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
    projectile.lifespan = 1000
controller.player1.on_button_event(ControllerButton.B, ControllerButtonEvent.PRESSED, on_button_event_b_pressed)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap)
def on_destroyed(sprite):
    sprite.start_effect(effects.spray)
sprites.on_destroyed(SpriteKind.projectile, on_destroyed)
def on_overlap2(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_overlap2)

def on_destroyed2(sprite):
    info.change_score_by(5)
sprites.on_destroyed(SpriteKind.enemy, on_destroyed2)
# Tilemap
scene.set_background_image(img("""
    ddccccccccccccddccccccccccccdd
    ddcbbbbbbbbbbcddcbbbbbbbbbbcdd
    ddbddddddddddbddbddddddddddbdd
    ddccccccccccccddccccccccccccdd
    ddcbbbbbbbbbbcddcbbbbbbbbbbcdd
    ddbddddddddddbddbddddddddddbdd
    ddccccccccc555ddccccccccc555dd
    ddcbbbbbbbb555ddcbbbbbbbb555dd
    ddbdddddddd555ddbdddddddd555dd
    ddccccccccccccddccccccccccccdd
    ddcbbbbbbbbbbcddcbbbbbbbbbbcdd
    ddbddddddddddbddbddddddddddbdd
    ddccccccccccccddccccccccccccdd
    ddcbbbbbbbbbbcddcbbbbbbbbbbcdd
    bbbddddddddddbbbbddddddddddbbb
    cccccccccccccccccccccccccccccc
"""))
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
"""), True)
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
scene.place_on_random_tile(coin2, 5)
scene.place_on_random_tile(coin3, 5)
scene.place_on_random_tile(coin4, 5)
scene.place_on_random_tile(coin5, 5)
def on_hit_tile(sprite):
    game.over()
scene.on_hit_tile(SpriteKind.player, 4, on_hit_tile)
# Jump/DoubleJump
canDoubleJump = True
def jump():
    global canDoubleJump
    if canDoubleJump:
        knight.vy = -55
        canDoubleJump = knight.is_hitting_tile(CollisionDirection.BOTTOM)
controller.A.on_event(ControllerButtonEvent.PRESSED, jump)

def on_update():
    global canDoubleJump
    if knight.is_hitting_tile(CollisionDirection.BOTTOM):
        canDoubleJump = True
game.on_update(on_update)
