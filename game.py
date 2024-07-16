import pygame

pygame.init()
screen = pygame.display.set_mode((500, 300))  

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			break

	pygame.display.update()
