@namespace
class SpriteKind:
    change = SpriteKind.create()
scene.set_background_image(assets.image("""
    menu
"""))
scene.background_image()
scene.screen_width()
scene.screen_height()
my_sprite4 = sprites.create(img("""
        .........................
            .........................
            .........................
            .........................
            .........................
            ..1...1.1..111.1..1.11111
            ..11..1....1...1..1...1..
            ..1.1.1.1..1.1.1111...1..
            ..1..11.1..1.1.1..1...1..
            ..1...1.1..111.1..1...1..
            .........................
            .........................
            ..111..111...1.1...1.1111
            ..1..1.1..1....1...1.1...
            ..1..1.111...1..1.1..111.
            ..1..1.1.1...1..1.1..1...
            ..111..1..1..1...1...1111
            .........................
            .........................
            .........................
            .........................
            .........................
            .........................
            .........................
            .........................
    """),
    SpriteKind.player)
my_sprite4.set_position(20, 17)
my_sprite2 = sprites.create(img("""
        ................................
            ................................
            ................................
            ...11.11111...11...111..11111...
            ..1.....1....1..1..1..1...1.....
            ...11...1....1..1..111....1.....
            .....1..1...1.11.1.1.1....1.....
            ...11...1...1....1.1..1...1.....
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
    """),
    SpriteKind.player)
my_sprite2.set_position(20, 39)
my_sprite = sprites.create(img("""
        ........................................
            ........................................
            ........................................
            ..1111.111..11111..1..1111.1...1...11...
            ..1..1.1..1...1.......1..1.11..1..1.....
            ..1..1.111....1....1..1..1.1.1.1...11...
            ..1..1.1......1....1..1..1.1..11.....1..
            ..1111.1......1....1..1111.1...1...11...
            ........................................
            ........................................
            ........................................
            ........................................
            ........................................
            ........................................
            ........................................
            ........................................
    """),
    SpriteKind.player)
my_sprite.set_position(20, 57)
my_sprite3 = sprites.create(img("""
        .........................
            .........................
            .........................
            ....111.1...1..1.11111...
            ....1....1.1.......1.....
            ....111...1....1...1.....
            ....1....1.1...1...1.....
            ....111.1...1..1...1.....
            .........................
            .........................
            .........................
            .........................
            .........................
            .........................
            .........................
            .........................
    """),
    SpriteKind.player)
my_sprite3.set_position(20, 99)

def on_forever():
    while controller.down.is_pressed():
        my_sprite2.set_image(img("""
            ................................
            ................................
            ................................
            .11111111111111111111111111111..
            .11ff11fffff111f111fff11fffff1..
            .1f111111f1111f1f11f11f111f111..
            .11ff1111f1111f1f11f11f111f111..
            .1111f111f111f1f1f1fff1111f111..
            .11ff1111f111f111f1f11f111f111..
            .11111111111111111111111111111..
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
        """))
        my_sprite2.set_image(img("""
            ................................
            ................................
            ................................
            ................................
            ...11..11111...1...111..11111...
            ..1......1....1.1..1..1...1.....
            ...11....1....1.1..1..1...1.....
            .....1...1...1.1.1.111....1.....
            ...11....1...1...1.1..1...1.....
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
        """))
        my_sprite.set_image(img("""
            ........................................
            ........................................
            ........................................
            .11111111111111111111111111111111111111.
            .1fff11fff11fffff11f11fff11f111f111ff11.
            .1f1f11f11f111f1111111f1f11ff11f11f1111.
            .1f1f11f11f111f1111f11f1f11f1f1f111ff11.
            .1f1f11fff1111f1111f11f1f11f11ff11111f1.
            .1fff11f111111f1111f11fff11f111f111ff11.
            .11111111111111111111111111111111111111.
            ........................................
            ........................................
            ........................................
            ........................................
            ........................................
            ........................................
        """))
        my_sprite.set_image(img("""
            ........................................
            ........................................
            ........................................
            ........................................
            ........................................
            ..111..111..11111..1..111..1...1...11...
            ..1.1..1..1...1.......1.1..11..1..1.....
            ..1.1..1..1...1....1..1.1..1.1.1...11...
            ..1.1..111....1....1..1.1..1..11.....1..
            ..111..1......1....1..111..1...1...11...
            ........................................
            ........................................
            ........................................
            ........................................
            ........................................
            ........................................
        """))
        my_sprite3.set_image(img("""
            .........................
            .........................
            ...11111111111111111111..
            ...1fff1f111f11f1fffff1..
            ...1f1111f1f1111111f111..
            ...1fff111f1111f111f111..
            ...1f1111f1f111f111f111..
            ...1fff1f111f11f111f111..
            ...11111111111111111111..
            .........................
            .........................
            .........................
            .........................
            .........................
            .........................
            .........................
        """))
        my_sprite3.set_image(img("""
            .........................
            .........................
            .........................
            .........................
            ....111.1...1..1.11111...
            ....1....1.1.......1.....
            ....111...1....1...1.....
            ....1....1.1...1...1.....
            ....111.1...1..1...1.....
            .........................
            .........................
            .........................
            .........................
            .........................
            .........................
            .........................
        """))
        my_sprite2.set_image(img("""
            ................................
            ................................
            ................................
            .11111111111111111111111111111..
            .11ff11fffff111f111fff11fffff1..
            .1f111111f1111f1f11f11f111f111..
            .11ff1111f1111f1f11f11f111f111..
            .1111f111f111f1f1f1fff1111f111..
            .11ff1111f111f111f1f11f111f111..
            .11111111111111111111111111111..
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
        """))
forever(on_forever)
