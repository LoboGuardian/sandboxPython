import flet as ft

def main(page: ft.Page):
    page.title = "Simple Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Display for the current operation or the result
    txt_display = ft.TextField(
        value="0",
        text_align=ft.TextAlign.RIGHT,
        width=200,
        read_only=True,
        border=ft.border.all(2, ft.colors.BLUE)  # Add border to the display
    )

    operations = []  # To store the numbers and operators
    current_input = ""  # To store the current input

    def button_click(e):
        nonlocal current_input
        button_value = e.control.data

        if button_value in ['+', '-', '*', '/']:
            if current_input:
                operations.append(current_input)
                operations.append(button_value)
                current_input = ""
                txt_display.value = " ".join(operations)

        elif button_value == '=':
            if current_input:
                operations.append(current_input)
                expression = ' '.join(operations)
                try:
                    result = eval(expression)
                    txt_display.value = str(result)
                except Exception:
                    txt_display.value = "Error"

            current_input = ""
            operations.clear()

        elif button_value == 'C':
            current_input = ""
            operations.clear()
            txt_display.value = "0"  # Reset display to 0

        else:
            current_input += button_value

            if current_input:
                txt_display.value = " ".join(operations) + " " + current_input
            else:
                txt_display.value = "0"

        page.update()

    # Create a grid of buttons for the calculator
    buttons = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['C', '0', '=', '+']
    ]

    # Add the display field at the top
    page.add(ft.Row([txt_display], alignment=ft.MainAxisAlignment.CENTER))

    for row in buttons:
        ft_row = ft.Row(
            [
                ft.Container(
                    ft.TextButton(num, data=num, on_click=button_click),
                    border=ft.border.all(2, ft.colors.BLUE),  # Add border to each button
                    padding=ft.padding.all(2)  # Optional: add some padding
                ) for num in row
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        page.add(ft_row)

ft.app(main)
