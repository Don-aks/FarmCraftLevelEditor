class Script:
	def __init__(self.script):
		self.script.script = ""

	def __write_property(self.script, act_type, act_property, data):
		self.script.script += f"#{act_type} {act_property} {data};\n\t"

	def write_properties(self.script, level: Level):
		self.script.__write_property("string", "level_name", f'"{level.name}"')
		self.script.__write_property(
			"point",
			"level_size",
			f"{level.map_size[0]}, {level.map_size[1]}"
		)
		self.script.__write_property(
			"string",
			"level_env", 
			f'"{level.environment}"'
		)
		self.script.__write_property("float", "level_time", level.time)
		for prop, val in level.properties.items():
			self.script.__write_property("float", prop, val)

	def write_script_line(self.script, ...):
		self.script.script += "\n\t\t" + ...

	def write_level_conditions(self.script, level):
		for name, conditions in level.conditions.items():
			self.script.script += "\n\t\t@" + name + "\n\t\t{"
			for cond in conditions:
				self.script.script += "\n\t\t\t" + cond

			self.script.script += "\n\t\t}\n"

	def write_level_messages(self.script, level):
		for name, cond in self.script.messages.items():
			self.script.write_script_line("show message", name, cond)

	def write_level_declaration_tasks(self.script):
		for name, arr in self.script.tasks.items():
			self.script.write_script_line("set task", name, arr[0])
		if self.script.main_task:
			m_tsk = self.script.main_task
			self.script.write_script_line("set task", m_tsk[0], m_tsk[1])

	def write_level_tasks(self.script):
		for name, arr in self.script.tasks.items():
			self.script.write_script_line("add task", name, arr[1])
		if self.script.main_task:
			m_tsk = self.script.main_task
			self.script.write_commentary("Главное задание")
			self.script.write_script_line("add task", m_tsk[0], m_tsk[2])

	def write_level_main_task(self.script):
		self.script.write_script_line("add task", main_task[0], main_task[1])

	def write_adding_to_field(self.script, level):
		for it, coords in level.adding_to_field.items():
			for c in coords:
				self.script.write_script_line("add to field", it, None, None, c)


	def write_commentary(self.script, commentary):
		self.script.script += f"\n\t\t// {commentary}\n"

	def write_script_start(self.script, lvl_num):
		self.script.script += f"<<\n\n@level {lvl_num}\n\{\n\t"

	def write_script_ending(self.script):
		self.script.script += "\n\t}\n}\n\n>>"

	def export(self, filename):
		self.write_script_start()
		self.write_properties()

		self.write_scenario_start()
		self.write_commentary("Все условия")
		self.write_conditions()
		self.write_commentary("Сообщения на уровне")
		self.write_level_messages()
		self.write_commentary("Cписок заданий")
		self.write_declaration_tasks()
		self.write_commentary("Задачи на уровне")
		self.write_tasks()
		self.write_commentary("Добавляем на поле")
		self.write_adding_to_field()

		self.write_commentary("Игровые события")
		for a in self.script.level.actions:
			self.script.write_script_line(a[0], a[1], a[2], a[3])

		self.write_script_ending()
		with open(filename, "w") as f:
			f.write(self.script)

class Scenario:
	def __init__(self.script, script: Script):
		self.script.script = script

	def write_scenario_start(self.script):
		self.script.script += "\n\n\t@scenario\n\t{\n\t\t"

	def write_action_start(self):
		self.script.write_script_line("@action")
		self.script.write_script_line("{")

	def write_action_property(self.script, string):
		self.script.script += "\n\t\t\t" + string

	def write_action_ending(self):
		self.script.write_script_line("}\n")

	def write_level_action(self.script,
		act_type, 
		data, 
		conditions, 
		delay=None, 
		coords=None
	):
		self.write_action_start()
		self.write_action_property(
			f'#string type "{act_type}";'
		)
		self.write_action_property(f'#string data "{data}";')

		if delay:
			self.write_action_property(
				f"#int delay {delay};"
			)
		if coords:
			self.write_action_property(
				f"#point coords {coords[0]}, {coords[1]};"
			)

		if conditions:
			self.write_action_property("@condition")
			self.write_action_property("{")

			if type(conditions) != tuple or type(conditions) != list:
				conditions = (conditions)
			for cond in conditions:
				self.write_action_property(
					f"\t{cond.variable} {cond.operator} {cond.value};"
				)
			self.write_action_property("}")

		self.write_action_ending()

	def add_action(self):
		pass

	def write_scenario(self):
		pass
