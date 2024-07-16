from script import Script

class Level:
	def __init__(self, number, name, map_size: tuple, environment, time, properties={}):
		self.number = number
		self.name = name
		self.map_size = size
		self.environment = environment
		self.time = time
		self.properties = properties

		self.conditions = {}
		self.messages = {}
		self.tasks = {}
		self.main_task = None
		self.items_on_field = []
		self.actions = []

		self.script = Script()


	def add_conditions(self, name, conditions: list[Condition]):
		self.conditions[name] = []
		for cond in conditions:
			self.conditions[name].append(cond)

	def add_message(self, name, condition):
		self.messages[name] = condition

	def add_task(self,
		name, 
		condition: Condition, 
		show_condition: Condition, 
		is_main=False
	):
		if is_main:
			self.main_task = condition
			return
		self.tasks[name] = (condition, show_condition)

	def add_to_field(self, item, coords: tuple):
		add = self.adding_to_field
		if add.get(item):
			add[item].append(coords)
			return
		add[item] = [coords]

	def add_action(self, act_type, data, condition, delay=None):
		self.actions.append((act_type, data, condition, delay))
