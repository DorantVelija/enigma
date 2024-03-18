import pygame


from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from draw import draw

#setup pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma Machine Simulator")

#create fonts
BOLD = pygame.font.SysFont("FreeMono", 25)
MONO = pygame.font.SysFont("FreeMono", 25, bold=True)

#global variables
WIDTH = 1600
HEIGHT = 900
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
MARGINS = {"top":200, "bottom":200, "left":100, "right":100}
GAP = 100

INPUT =""
OUTPUT =""
PATH = []


# historical enigma rotors and reflectors
I = Rotor( "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q" )
II = Rotor( "AJDKSIRUXBLHWTMCQGZNPYFVOE", "E" )
III = Rotor( "BDFHJLCPRTXVZNYEIWGAKMUSQO", "V" )
IV = Rotor( "ESOVPZJAYQUIRHXLNFTGKDCMWB", "J" )
V = Rotor( "VZBRGITYUPSDNHLXAWMJQOFECK", "Z" )
A = Reflector( "EJMZALYXVBWFCRQUONTSPIKHGD" )
B = Reflector( "YRUHQSLDPXNGOKMIEBFZCWVJAT" )
C = Reflector( "FVPJIAOYEDRZXWGCTKUQSBNMHL" )

# keyboard and plugboard
KB = Keyboard()
PB = Plugboard( ["AB", "CD", "EF"] )

# define enigma machine
ENIGMA = Enigma( B, I, II, III, PB, KB )

# set the rings
ENIGMA.set_rings((1,1,1))

# set message key
ENIGMA.set_key("CAT")

"""
# encipher message
message = "THISCOOLENIGMAMACHINE"
cipher_text = ""
for letter in message:
    cipher_text = cipher_text + ENIGMA.encipher(letter)

print(cipher_text)
"""
animating = True
while animating:
    #background
    SCREEN.fill("#333333")

    #text input
    text = BOLD.render(INPUT, True, "white")
    text_box = text.get_rect(center = (WIDTH/2,MARGINS["top"]/2))
    SCREEN.blit(text, text_box)


    # text output
    text = MONO.render( OUTPUT, True, "white" )
    text_box = text.get_rect( center=(WIDTH / 2, MARGINS["top"] / 2+25) )
    SCREEN.blit( text, text_box )

    # draw enigma machine
    draw( ENIGMA, PATH ,SCREEN, WIDTH, HEIGHT, MARGINS, GAP, BOLD )


    #update screen
    pygame.display.flip()

    # track user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                II.rotate()
            elif event.key == pygame.K_SPACE:
                INPUT = INPUT + " "
                OUTPUT = OUTPUT + " "

            else:
                key = event.unicode
                if key in "abcdefghijklmnopqrstuvwxyz":
                    letter = key.upper()
                    INPUT = INPUT + letter
                    PATH, cipher = ENIGMA.encipher(letter)
                    OUTPUT = OUTPUT + cipher






"""
letter = "A"
signal = KB.forward(letter)
signal = PB.forward(signal)
signal = III.forward(signal)
signal = II.forward(signal)
signal = I.forward(signal)
signal = A.reflect(signal)
signal = I.backward(signal)
signal = II.backward(signal)
signal = III.backward(signal)
signal = PB.backward(signal)
letter = KB.backward(signal)
"""

"""VI = Rotor("JPGVOUMFYQBENHZRDKASXLICTW")
VII = Rotor("NZJHGRCXMYSWBOUFAIVLPEKQDT")
VIII = Rotor("FKQHTLXOCBJSPDZRAMEWNIUYGV")"""
