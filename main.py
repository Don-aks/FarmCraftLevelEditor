class Item:
	def __init__(self, name, x, y):
		super(Item, self).__init__()
		self.name = name
		self.x = x
		self.y = y


class Condition:
	def __init__(self, name, variable, operator, value):
		super(Condition, self).__init__()
		self.variable = variable
		self.operator = operator
		self.value = value

	lvl.add_condition("test_cond", ["time"], [">="], ["10000000000000"])
	lvl.add_message("l1_test_msg", "test_cond")
	lvl.add_task("l1_test_task", "test_cond", "second_test_cond")
	lvl.add_task("l1_test_main_task", "test_cond", "second_test_cond", True)
	lvl.add_to_field("heroine", (0, 0))
	lvl.add_action("add particles", "pumpkin item_hint 20", "test_cond", 2)

if __name__ == "__main__":
	number = int(input("Это уровень №"))
	name = input("Название: ")
	size_x = input("Размер поля Х: ")
	size_y = input("Размер поля Y: ")
	env = input("Местность: ")
	time = input("Золотое время в секундах: ")

	lvl = Level(number, name, (size_x, size_y), env, time)
	ln = lvl.number
	while True:
		menu = input("Что сделать? (help - для помощи) ")
		if menu == "help":
			print("message - показать сообщение")
			print("add task - добавить задание")
			print("add to field - добавить на поле")

			print("\nexport - сохранить уровень")
		elif menu == "message":
			text = input("Текст: ")
			cond = input("Когда? ")
			cond_name = f"l{ln}_cond{len(lvl.conditions)}"
			msg_name = f"l{ln}_m{len(lvl.messages)}"
			lvl.add_conditions(cond_name, [cond])
			lvl.add_message(msg_name, cond_name)
		elif menu == "export":
			lvl.export("test.txt")
			break
