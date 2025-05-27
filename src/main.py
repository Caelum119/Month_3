import flet
from flet import Page, TextField, ElevatedButton, Column, Text, ListView

def main(page: Page):
    page.title = "Учёт расходов"

    expenses = []  # список расходов, каждый элемент будет словарём {"name": ..., "amount": ...}
    total_sum = 0

    # Текстовые поля для ввода
    name_input = TextField(label="Название расхода", width=200)
    amount_input = TextField(label="Сумма расхода", width=200, keyboard_type="number")

    # Отображение списка расходов
    expenses_list = Column()

    # Текст для общей суммы
    total_text = Text("Общая сумма расходов: 0", size=16, weight="bold")

    def add_expense(e):
        nonlocal total_sum
        name = name_input.value.strip()
        amount_str = amount_input.value.strip()

        # Проверка, что заполнено и сумма число > 0
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

        # Добавляем в список расходов
        expenses.append({"name": name, "amount": amount})
        total_sum += amount

        # Добавляем новый элемент в UI список
        expenses_list.controls.append(Text(f"{name}: {amount}"))
        total_text.value = f"Общая сумма расходов: {total_sum}"
        # Очищаем поля ввода
        name_input.value = ""
        amount_input.value = ""
        page.update()

    add_button = ElevatedButton(text="Добавить расход", on_click=add_expense)

    # Добавляем все элементы на страницу
    page.add(
        name_input,
        amount_input,
        add_button,
        expenses_list,
        total_text,
    )

flet.app(target=main)
