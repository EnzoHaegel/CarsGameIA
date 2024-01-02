import pygame

class Segment:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

class Map:
    def __init__(self):
        self.segments = []
        self.start_point = (100, 100)
        self.start_angle = 0  # En degrés
        self.end_point = (500, 500)

    def add_segment(self, start_point, end_point):
        self.segments.append(Segment(start_point, end_point))

    def load_map(self, filename):
        with open(filename, 'r') as f:
            data = f.readlines()
        self.segments = []
        for line in data:
            start, end = line.strip().split(";")
            start_point = tuple(map(int, start.split(',')))
            end_point = tuple(map(int, end.split(',')))
            self.add_segment(start_point, end_point)

    def save_map(self, filename):
        with open(filename, 'w') as f:
            for segment in self.segments:
                line = "{},{};{},{}\n".format(segment.start_point[0], segment.start_point[1], segment.end_point[0], segment.end_point[1])
                f.write(line)

    def display(self, screen):
        for segment in self.segments:
            pygame.draw.line(screen, (0, 0, 0), segment.start_point, segment.end_point, 2)

# Pygame initialization
pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

# Create a map object
game_map = Map()
# Add segments manually or load them from a file
game_map.add_segment((100, 100), (200, 200))
game_map.add_segment((200, 200), (300, 300))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display the map
    screen.fill((200, 200, 200))  # Fill the screen with black
    game_map.display(screen)
    pygame.display.flip()

pygame.quit()
