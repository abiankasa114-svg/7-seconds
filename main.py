def on_button_pressed_a():
    pass
    input.on_button_pressed(Button.A, on_button_pressed_a)
    start = 0
    def on_button_pressed_a():
        global start
        start = input.running_time()
        input.on_button_pressed(Button.A, on_button_pressed_a)
        start = 0
        def on_button_pressed_a():
            global start
            start = input.running_time()
            basic.show_icon(IconNames.CHESSBOARD)
            input.on_button_pressed(Button.A, on_button_pressed_a)
            def on_button_pressed_b():
                pass
                input.on_button_pressed(Button.B, on_button_pressed_b)
                start = 0
                def on_button_pressed_b():
                    elapsed = input.running_time() - start
                    input.on_button_pressed(Button.B, on_button_pressed_b)
                    start = 0
                    def on_button_pressed_b():
                        elapsed = input.running_time() - start
                        score = abs(elapsed - 7000)
                        input.on_button_pressed(Button.B, on_button_pressed_b)
                        start = 0
                        def on_button_pressed_b():
                            elapsed = input.running_time() - start
                            score = abs(elapsed - 7000)
                            basic.show_number(score)
                            input.on_button_pressed(Button.B, on_button_pressed_b)

