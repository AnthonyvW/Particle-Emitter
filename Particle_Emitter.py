import pygame
import random

pygame.init()

# Clock Speed
FPS = 60
clock = pygame.time.Clock()
# Game Window
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
transparent_Overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA) # For Transparent Effects
pygame.display.set_caption('Particle Emitter')
# Setting Font
particle_Font = pygame.font.SysFont("Consolas", 15) # Font
# Particle Emitter Settings
particle_Emitters = []
Speed = 0
Glows = True
Glow_Intensity = 40
X_Force = 0
Y_Force = 0
Decay = 0.05
Lifetime = 4
Rand_X_Dir = True
Rand_X_Range = 3
Rand_Y_Dir = True
Rand_Y_Range = 3
Rand_Lifetime = True
Rand_Decay = True
Rand_Decay_Max = 8
Rand_Decay_Min = 4
R = 0
G = 0
B = 0
Start_R = 255
Start_G = 255
Start_B = 255

button_list = [
    (pygame.Rect(0, 10 + 15, 25, 15), 1, 0), (pygame.Rect(25, 10 + 15, 30, 15), -1, 0),
    (pygame.Rect(0, 10 + 15 * 2, 55, 15), 0, 1),
    (pygame.Rect(0, 10 + 15 * 3, 25, 15), 1, 2), (pygame.Rect(25, 10 + 15 * 3, 30, 15), -1, 2),
    (pygame.Rect(0, 10 + 15 * 4, 25, 15), 1, 3), (pygame.Rect(25, 10 + 15 * 4, 30, 15), -1, 3),
    (pygame.Rect(0, 10 + 15 * 5, 25, 15), 1, 4), (pygame.Rect(25, 10 + 15 * 5, 30, 15), -1, 4),
    (pygame.Rect(0, 10 + 15 * 6, 55, 15), 0, 5),
    (pygame.Rect(0, 10 + 15 * 7, 25, 15), 1, 6), (pygame.Rect(25, 10 + 15 * 7, 30, 15), -1, 6),
    (pygame.Rect(0, 10 + 15 * 8, 55, 15), 0, 7),
    (pygame.Rect(0, 10 + 15 * 9, 25, 15), 1, 8), (pygame.Rect(25, 10 + 15 * 9, 30, 15), -1, 8),
    (pygame.Rect(0, 10 + 15 * 10, 55, 15), 0, 9),
    (pygame.Rect(0, 10 + 15 * 11, 55, 15), 0, 10),
    (pygame.Rect(0, 10 + 15 * 12, 25, 15), 1, 11), (pygame.Rect(25, 10 + 15 * 12, 30, 15), -1, 11),
    (pygame.Rect(0, 10 + 15 * 13, 25, 15), 1, 12), (pygame.Rect(25, 10 + 15 * 13, 30, 15), -1, 12),
    (pygame.Rect(0, 10 + 15 * 14, 25, 15), 1, 13), (pygame.Rect(25, 10 + 15 * 14, 30, 15), -1, 13),
    (pygame.Rect(0, 10 + 15 * 15, 25, 15), 1, 14), (pygame.Rect(25, 10 + 15 * 15, 30, 15), -1, 14),
    (pygame.Rect(0, 10 + 15 * 16, 25, 15), 1, 15), (pygame.Rect(25, 10 + 15 * 16, 30, 15), -1, 15),
    (pygame.Rect(0, 10 + 15 * 17, 25, 15), 1, 16), (pygame.Rect(25, 10 + 15 * 17, 30, 15), -1, 16),
    (pygame.Rect(0, 10 + 15 * 18, 25, 15), 1, 17), (pygame.Rect(25, 10 + 15 * 18, 30, 15), -1, 17),
    (pygame.Rect(0, 10 + 15 * 19, 25, 15), 1, 18), (pygame.Rect(25, 10 + 15 * 19, 30, 15), -1, 18),
    (pygame.Rect(0, 10 + 15 * 20, 25, 15), 1, 19), (pygame.Rect(25, 10 + 15 * 20, 30, 15), -1, 19),
    (pygame.Rect(79, 15 + 15 * 21, 20, 15), 0, 20), (pygame.Rect(103, 15 + 15 * 21, 20, 15), 1, 20), (pygame.Rect(127, 15 + 15 * 21, 20, 15), 2, 20), (pygame.Rect(151, 15 + 15 * 21, 20, 15), 3, 20), (pygame.Rect(175, 15 + 15 * 21, 20, 15), 4, 20), (pygame.Rect(199, 15 + 15 * 21, 20, 15), 5, 20),
    (pygame.Rect(0, 5 + 15 * 23, 85, 15), 0, 21), (pygame.Rect(95, 5 + 15 * 23, 125, 15), 1, 21),
    (pygame.Rect(0, 10 + 15 * 24, 195, 15), 0, 22),
    ]

def button_press(number, id):
    global Speed, Glows, X_Force, Y_Force, Decay, Lifetime, Rand_X_Dir, Rand_X_Range, Rand_Y_Dir, Rand_Y_Range, Rand_Lifetime, Rand_Decay, Rand_Decay_Max, Rand_Decay_Min, R, G, B, Start_R, Start_G, Start_B, particle_Emitters, Glow_Intensity

    if id == 0:
        if number > 0:
            Speed += 1
        elif Speed > 0:
            Speed -= 1
    elif id == 1:
        Glows = not Glows
    elif id == 2:
        if number > 0:
            X_Force += 0.1
        else:
            X_Force -= 0.1
    elif id == 3:
        if number > 0:
            Y_Force += 0.1
        else:
            Y_Force -= 0.1
    elif id == 4:
        if number > 0:
            Decay += 0.01
        else:
            Decay -= 0.01
    elif id == 5:
        Rand_X_Dir = not Rand_X_Dir
    elif id == 6:
        if number > 0:
            Rand_X_Range += 1
        elif Rand_X_Range > 0:
            Rand_X_Range -= 1
    elif id == 7:
        Rand_Y_Dir = not Rand_Y_Dir
    elif id == 8:
        if number > 0:
            Rand_Y_Range += 1
        elif Rand_Y_Range > 0:
            Rand_Y_Range -= 1
    elif id == 9:
        Rand_Decay = not Rand_Decay
    elif id == 10:
        Rand_Lifetime = not Rand_Lifetime
    elif id == 11:
        if number > 0 and Rand_Decay_Min < Rand_Decay_Max:
            Rand_Decay_Min += 1
        elif number < 0 and Rand_Decay_Min > 0:
            Rand_Decay_Min -= 1
    elif id == 12:
        if number > 0:
            Rand_Decay_Max += 1
        elif Rand_Decay_Max > 0 and Rand_Decay_Min < Rand_Decay_Max:
            Rand_Decay_Max -= 1
    elif id == 13:
        if R >= -255 and R < 255 and number > 0:
            R += 1
        elif R > -255 and R <= 255:
            R -= 1
    elif id == 14:
        if G >= -255 and G < 255 and number > 0:
            G += 1
        elif G > -255 and G <= 255:
            G -= 1
    elif id == 15:
        if B >= -255 and B < 255 and number > 0:
            B += 1
        elif B > -255 and B <= 255:
            B -= 1
    elif id == 16:
        if Start_R >= 0 and Start_R < 255 and number > 0:
            Start_R += 1
        elif Start_R > 0 and Start_R <= 255 and number < 0:
            Start_R -= 1
    elif id == 17:
        if Start_G >= 0 and Start_G < 255 and number > 0:
            Start_G += 1
        elif Start_G > 0 and Start_G <= 255 and number < 0:
            Start_G -= 1
    elif id == 18:
        if Start_B >= 0 and Start_B < 255 and number > 0:
            Start_B += 1
        elif Start_B > 0 and Start_B <= 255 and number < 0:
            Start_B -= 1
    elif id == 19:
        if Glow_Intensity >= 0 and Glow_Intensity < 255 and number > 0:
            Glow_Intensity += 1
        elif Glow_Intensity > 0 and Glow_Intensity <= 255 and number < 0:
            Glow_Intensity -= 1
    elif id == 20:
        if number == 0:  # Mana Particle
            Speed = 0
            Glows = True
            X_Force = 0
            Y_Force = -1
            Decay = 0.05
            Lifetime = 4
            Rand_X_Dir = True
            Rand_X_Range = 2
            Rand_Y_Dir = False
            Rand_Y_Range = 3
            Rand_Lifetime = True
            Rand_Decay = False
            Rand_Decay_Max = 8
            Rand_Decay_Min = 4
            R = 2
            G = 1
            B = 0
            Start_R = 255
            Start_G = 255
            Start_B = 255
            Glow_Intensity = 40
        elif number == 1:  # From Darkness Comes Forth Light.
            Speed = 0
            Glows = True
            X_Force = 0
            Y_Force = 0
            Decay = 0.05
            Lifetime = 4
            Rand_X_Dir = True
            Rand_X_Range = 3
            Rand_Y_Dir = True
            Rand_Y_Range = 3
            Rand_Lifetime = True
            Rand_Decay = False
            Rand_Decay_Max = 8
            Rand_Decay_Min = 4
            R = -3
            G = -3
            B = -3
            Start_R = 0
            Start_G = 0
            Start_B = 0
            Glow_Intensity = 40
        elif number == 2:  # Dino Killer
            Speed = 0
            Glows = True
            X_Force = 1.5
            Y_Force = -1
            Decay = 0.05
            Lifetime = 4
            Rand_X_Dir = True
            Rand_X_Range = 2
            Rand_Y_Dir = False
            Rand_Y_Range = 3
            Rand_Lifetime = True
            Rand_Decay = False
            Rand_Decay_Max = 8
            Rand_Decay_Min = 4
            R = 1
            G = 2
            B = 3
            Start_R = 255
            Start_G = 255
            Start_B = 255
        elif number == 3: # Fire
            Speed = 0
            Glows = True
            X_Force = 0
            Y_Force = -1
            Decay = 0.04
            Lifetime = 4
            Rand_X_Dir = True
            Rand_X_Range = 2
            Rand_Y_Dir = False
            Rand_Y_Range = 3
            Rand_Decay = False
            Rand_Lifetime = True
            Rand_Decay_Min = 3
            Rand_Decay_Max = 8
            R = 0
            G = 3
            B = 0
            Start_R = 255
            Start_G = 255
            Start_B = 0
            Glow_Intensity = 40
        elif number == 4:
            Speed = 0
            Glows = True
            X_Force = 0
            Y_Force = -1
            Decay = 0.04
            Lifetime = 4
            Rand_X_Dir = True
            Rand_X_Range = 2
            Rand_Y_Dir = True
            Rand_Y_Range = 3
            Rand_Decay = False
            Rand_Lifetime = True
            Rand_Decay_Min = 3
            Rand_Decay_Max = 7
            R = 1
            G = -2
            B = 4
            Start_R = 255
            Start_G = 0
            Start_B = 255
            Glow_Intensity = 70
        elif number == 5:
            Speed = 0
            Glows = False
            X_Force = 2
            Y_Force = -1
            Decay = 0.15
            Lifetime = 4
            Rand_X_Dir = True
            Rand_X_Range = 3
            Rand_Y_Dir = True
            Rand_Y_Range = 3
            Rand_Decay = False
            Rand_Lifetime = True
            Rand_Decay_Min = 10
            Rand_Decay_Max = 20
            R = 3
            G = 3
            B = 3
            Start_R = 240
            Start_G = 240
            Start_B = 240
            Glow_Intensity = 70
    elif id == 21:
        if number == 0:
            particle_Emitters = []
        else:
            Speed = 0
            Glows = True
            X_Force = 0
            Y_Force = 0
            Decay = 0.05
            Lifetime = 4
            Rand_X_Dir = True
            Rand_X_Range = 3
            Rand_Y_Dir = True
            Rand_Y_Range = 3
            Rand_Lifetime = True
            Rand_Decay = True
            Rand_Decay_Max = 8
            Rand_Decay_Min = 4
            R = 1
            G = 1
            B = 1
            Start_R = 255
            Start_G = 255
            Start_B = 255
    elif id == 22:
        Speed = random.randint(0,20)
        if Speed < 10:
            Speed = random.randint(0,3)
        elif Speed < 15:
            Speed = random.randint(4,6)
        else:
            Speed = random.randint(7,10)
        Glows = bool(random.getrandbits(1))
        X_Force = random.randint(-50, 50) / 10
        Y_Force = random.randint(-10, 10) / 10
        Decay = random.randint(0, 20) / 100
        Rand_X_Dir = bool(random.getrandbits(1))
        Rand_X_Range = random.randint(0,5)
        Rand_Y_Dir = bool(random.getrandbits(1))
        Rand_Y_Range = random.randint(0,5)
        Rand_Decay = bool(random.getrandbits(1))
        Rand_Lifetime = bool(random.getrandbits(1))
        Rand_Decay_Min = random.randint(0,5)
        Rand_Decay_Max = random.randint(Rand_Decay_Min,20)
        R = random.randint(-4,4)
        G = random.randint(-4,4)
        B = random.randint(-4,4)
        Start_R = random.randint(0,255)
        Start_G = random.randint(0,255)
        Start_B = random.randint(0,255)
        Glow_Intensity = random.randint(0,255)

def draw_text(text, _x, _y, color=(255, 255, 255), font=particle_Font):
    '''Draws Text to Screen at _x, _y'''
    img = font.render(text, True, color)
    screen.blit(img, (_x, _y))

class particle_emitter:
    def __init__(self, Red, Green, Blue, XForce, YForce, Fade, Xpos, Ypos, Speed = 0, life = 4, DecayMin = 4, DecayMax = 4, Glows = False, randomX_Direction = True, randomY_Direction = True, random_lifetime = True, RandDecay = True, Rand_X = 4, Rand_Y = 4, StartR = 255, StartG = 255, StartB = 255, GlowIntensity = 40):
        '''Creates a particle emitter that emits particles at every Speed intervals.'''
        self.YForce = YForce
        self.XForce = XForce
        self.fade = Fade
        self.particles = []
        self.Xpos = Xpos
        self.Ypos = Ypos
        self.speed = Speed
        self.current_speed = 0
        self.Glows = Glows
        self.life = life
        self.randomX_Direction = randomX_Direction
        self.Rand_X = Rand_X
        self.randomY_Direction = randomY_Direction
        self.Rand_Y = Rand_Y
        self.Rand_Life = random_lifetime
        self.Rand_Life_Max = DecayMax
        self.Rand_Life_Min = DecayMin
        self.R = Red
        self.G = Green
        self.B = Blue
        self.Start_R = StartR
        self.Start_G = StartG
        self.Start_B = StartB
        self.Glow_Intensity = GlowIntensity
        # Sets the Particle Emitter's decay
        if RandDecay:
            self.fade = (random.randint(1, 10) / 100)
        else:
            self.fade = Fade

    def update_emitter(self, solid_Screen, transparent_Screen):
        # Adds another particle according every self.speed Frames
        if self.current_speed == self.speed:
            if self.Rand_Life:
                self.particles.append([[self.Xpos, self.Ypos], [self.fade], random.randint(self.Rand_Life_Min, self.Rand_Life_Max), [self.Start_R, self.Start_G, self.Start_B]])
            else:
                self.particles.append([[self.Xpos, self.Ypos], [self.fade], self.life, [255, 255, 255]])
            self.current_speed = 0
        else:
            self.current_speed += 1

        # Updates all the particles belonging to the emitter.
        for particle in self.particles:
            # Modifies Particle Direction
            # Modifies Direction on the X Axis
            if self.randomX_Direction:
                particle[0][0] += random.randint(-self.Rand_X, self.Rand_X) + self.XForce
            else:
                particle[0][0] += self.XForce
            # Modifies Direction on the Y Axis
            if self.randomY_Direction:
                particle[0][1] += random.randint(-self.Rand_Y, self.Rand_Y) + self.YForce
            else:
                particle[0][1] += self.YForce
            particle[2] -= self.fade
            # Color Shifting
            # Red Particle Fade
            if particle[3][0] - self.R >= 0 and particle[3][0] - self.R <= 255:
                particle[3][0] -= self.R
            elif particle[3][0] - self.R < 0:
                particle[3][0] = 0
            elif particle[3][0] - self.R > 255:
                particle[3][0] = 255
            # Green Particle Fade
            if particle[3][1] - self.G >= 0 and (particle[3][1] - self.G) <= 255:
                particle[3][1] -= self.G
            elif particle[3][1] - self.G < 0:
                particle[3][1] = 0
            elif particle[3][1] - self.G > 255:
                particle[3][1] = 255
            # Blue Particle Fade
            if particle[3][2] - self.B >= 0 and particle[3][2] - self.B <= 255:
                particle[3][2] -= self.B
            elif particle[3][2] - self.B < 0:
                particle[3][2] = 0
            elif particle[3][2] - self.B > 255:
                particle[3][2] = 255
            # Draws particle to screen
            if self.Glows:  # Toggles Glow
                pygame.draw.circle(transparent_Screen, [particle[3][0], particle[3][1], particle[3][2], self.Glow_Intensity], particle[0], particle[2] * 2)
            pygame.draw.circle(solid_Screen, particle[3], particle[0], particle[2])
            # Cleans up nonexistent particles
            self.particles = [particle for particle in self.particles if particle[2] > 0]

run = True
while run:
    # Clock Speed
    clock.tick(FPS)
    # Background
    screen.fill((0, 0, 0))
    transparent_Overlay.fill((0, 0, 0, 0))
    # Gets Mouse Position
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    # Keypresses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Makes it so the window closes when the red X is pressed.
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Exits when Escape is pressed
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Creates particle emitter on screen when clicked.
            if x > 290 or y > 10 + 15 * 26:  # Makes it so particle emitters can't be put in the setting box.
                particle_Emitters.append(particle_emitter(R, G, B, X_Force, Y_Force, Decay, x, y, Speed, Lifetime, Rand_Decay_Min, Rand_Decay_Max, Glows, Rand_X_Dir, Rand_Y_Dir, Rand_Lifetime, Rand_Decay, Rand_X_Range, Rand_Y_Range, Start_R, Start_G, Start_B, Glow_Intensity))
            else:  # Checks if a button was clicked in the box.
                for button in button_list:
                    if button[0].collidepoint(x, y):
                        button_press(button[1], button[2])
    # Updates Emitters
    for particle_Emitter in particle_Emitters:
        particle_Emitter.update_emitter(screen, transparent_Overlay)

    # BUTTON DEBUG
    #for button in button_list:
    #   pygame.draw.rect(screen, (255, 255, 255), button[0], 1)

    # Puts Buttons on the Screen
    screen.blit(transparent_Overlay, (0, 0))
    draw_text(f"New Emitter Settings", 5, 5)
    draw_text(f"+ | -  Current Speed = {Speed:.0f}",5,10 + 15)
    draw_text(f"Toggle Glowing Particles = {Glows}", 5, 10 + 15 * 2)
    draw_text(f"+ | -  X Force = {X_Force:.1f}", 5, 10 + 15 * 3)
    draw_text(f"+ | -  Y Force = {Y_Force:.1f}", 5, 10 + 15 * 4)
    draw_text(f"+ | -  Particle Decay = {Decay:.2f}", 5, 10 + 15 * 5)
    draw_text(f"Toggle Random X Direction = {Rand_X_Dir}", 5, 10 + 15 * 6)
    draw_text(f"+ | -  Random X Force = {Rand_X_Range}", 5, 10 + 15 * 7)
    draw_text(f"Toggle Random Y Direction = {Rand_Y_Dir}", 5, 10 + 15 * 8)
    draw_text(f"+ | -  Random Y Force = {Rand_Y_Range}", 5, 10 + 15 * 9)
    draw_text(f"Toggle Random Decay = {Rand_Decay}", 5, 10 + 15 * 10)
    draw_text(f"Toggle Random Lifetime = {Rand_Lifetime}", 5, 10 + 15 * 11)
    draw_text(f"+ | -  Random Life Minimum = {Rand_Decay_Min}", 5, 10 + 15 * 12)
    draw_text(f"+ | -  Random Life Maximum = {Rand_Decay_Max}", 5, 10 + 15 * 13)
    draw_text(f"+ | -  Red Decrease = {R}", 5, 10 + 15 * 14)
    draw_text(f"+ | -  Green Decrease = {G}", 5, 10 + 15 * 15)
    draw_text(f"+ | -  Blue Decrease = {B}", 5, 10 + 15 * 16)
    draw_text(f"+ | -  Starting Red = {Start_R}", 5, 10 + 15 * 17)
    draw_text(f"+ | -  Starting Green = {Start_G}", 5, 10 + 15 * 18)
    draw_text(f"+ | -  Starting Blue = {Start_B}", 5, 10 + 15 * 19)
    draw_text(f"+ | -  Glow Intensity = {Glow_Intensity}", 5, 10 + 15 * 20)
    draw_text(f"Presets : 1  2  3  4  5  6", 5, 15 + 15 * 21)
    draw_text(f"CLEAR ALL   RESET SETTINGS", 5, 5 + 15 * 23)
    draw_text(f"RANDOM PARTICLE EMITTER", 5, 10 + 15 * 24)
    draw_text("Created By Anthony van Weel", 5, 785)
    # Updates Screen
    pygame.display.update()

pygame.quit()