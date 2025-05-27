import flet
from flet import Page, TextField, ElevatedButton, Column, Text, ListView

def main(page: Page):
    page.title = "Учёт расходов"

    expenses = []  
    total_sum = 0

    name_input = TextField(label="Название расхода", width=200)
    amount_input = TextField(label="Сумма расхода", width=200, keyboard_type="number")

    expenses_list = Column()

    total_text = Text("Общая сумма расходов: 0", size=16, weight="bold")

    def add_expense(e):
        nonlocal total_sum
        name = name_input.value.strip()
        amount_str = amount_input.value.strip()

        if not name or not amount_str:
            page.snack_bar = Text("Пожалуйста, заполните оба поля")
            page.snack_bar.open = True
            page.update()
            return

        try:
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError()
        except ValueError:
            page.snack_bar = Text("Сумма должна быть положительным числом")
            page.snack_bar.open = True
            page.update()
            return

        expenses.append({"name": name, "amount": amount})
        total_sum += amount

        expenses_list.controls.append(Text(f"{name}: {amount}"))
        total_text.value = f"Общая сумма расходов: {total_sum}"
        name_input.value = ""
        amount_input.value = ""
        page.update()

    add_button = ElevatedButton(text="Добавить расход", on_click=add_expense)

    page.add(
        name_input,
        amount_input,
        add_button,
        expenses_list,
        total_text,
    )

flet.app(target=main)
