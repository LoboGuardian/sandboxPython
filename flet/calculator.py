import flet as ft

def main(page: ft.Page):
    page.title = "Simple Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # This will display the current operation or the result
    txt_display = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=200, read_only=True)

    operations = []  # To store the numbers and operators
    current_input = ""  # To store the current input

    def button_click(e):
        nonlocal current_input
        button_value = e.control.data
        
        if button_value in ['+', '-', '*', '/']:
            if current_input:
                operations.append(current_input)  # Add the current input before operator
                operations.append(button_value)  # Add the operator
                current_input = ""
                txt_display.value = " ".join(operations)  # Update the display to show current operation
        elif button_value == '=':
            if current_input:
                operations.append(current_input)  # Add the last number
                expression = ' '.join(operations)  # Join the operations into a string

            try:
                result = eval(expression)  # Calculate the result
                # Update the display to show just the result
                txt_display.value = str(result)
            except Exception:
                txt_display.value = "Error"

            # Reset the input and operations after calculation
            current_input = ""
            operations.clear()  # Clear the operations for future calculations
        # else:
            # txt_display.value = "0"  # If nothing was entered

        elif button_value == 'C':
            current_input = ""
            operations.clear()
            txt_display.value = "0"  # Reset display to 0
        else:
            current_input += button_value
            
            if current_input:  # Update display to show the current input
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
    page.add(ft.Row([
        txt_display,
    ], alignment=ft.MainAxisAlignment.CENTER))

    for row in buttons:
        ft_row = ft.Row(
            [
                ft.TextButton(num, data=num, on_click=button_click) for num in row
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        page.add(ft_row)

ft.app(main)
