from bingo_constants import *
import pygame, random, time

def main():

    pygame.init()

    pygame.display.set_caption("balls")

    screen = pygame.display.set_mode((800,600))

    running = True

    OUTSIDE_COLOR = (100,100,100)
    OUTSIDE_RECT = (OUTSIDE_X, OUTSIDE_Y, OUTSIDE_WIDTH, OUTSIDE_HEIGHT)
    INSIDE_COLOR = (0,0,0)
    INSIDE_RECT = (INSIDE_X, INSIDE_Y, INSIDE_WIDTH, INSIDE_HEIGHT)
    LETTERS_COLOR = (255,255,255)
    LETTERS_RECT = (LETTERS_X, LETTERS_Y, LETTERS_WIDTH, LETTERS_HEIGHT)

    HOPPER_OUTSIDE_RECT = (HOPPER_OUTSIDE_X, HOPPER_OUTSIDE_Y, HOPPER_OUTSIDE_WIDTH, HOPPER_OUTSIDE_HEIGHT)
    HOPPER_INSIDE_RECT = (HOPPER_INSIDE_X, HOPPER_INSIDE_Y, HOPPER_INSIDE_WIDTH, HOPPER_INSIDE_HEIGHT)
    

    number_font = pygame.font.SysFont("Impact", 35)
    letter_font = pygame.font.SysFont("Arial", 35, bold=True)
    

    BOARD_NUMBERS_X = []
    BOARD_NUMBERS_Y = []
    BOARD_NUMBERS_COLOR = []

    BOARD_LETTERS = ["B","I","N","G","O"]
    BOARD_LETTERS_X = BOARD_NUMBERS_POS_X - BOARD_NUMBERS_WIDTH
    BOARD_LETTERS_Y = []
    
    HOPPER_IND_LETTERS_X = []
    HOPPER_IND_LETTERS_Y = HOPPER_LETTERS_Y


    

    hopper_letters_graphic = pygame.image.load('pictures\\Bingo_Hopper_Letters.png')
    hopper_numbers_graphic = pygame.image.load('pictures\\seven_segment_numbers.png')

    
    for n in range (0,75,1):
        BOARD_NUMBERS_X.append(BOARD_NUMBERS_POS_X + ((n % 15) * BOARD_NUMBERS_WIDTH))
        BOARD_NUMBERS_Y.append(BOARD_NUMBERS_POS_Y + (int(n / 15) * BOARD_NUMBERS_HEIGHT))
        BOARD_NUMBERS_COLOR.append((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        if (n < 5):
            HOPPER_IND_LETTERS_X.append(HOPPER_LETTERS_X + (n * HOPPER_IND_LETTERS_WIDTH))
            BOARD_LETTERS_Y.append(BOARD_NUMBERS_POS_Y + (n * BOARD_NUMBERS_HEIGHT))
    

    
    pygame.draw.rect(screen, OUTSIDE_COLOR, OUTSIDE_RECT)
    pygame.draw.rect(screen, INSIDE_COLOR,INSIDE_RECT)
    pygame.draw.rect(screen, LETTERS_COLOR, LETTERS_RECT)

    for n in range(0,75,1):
        pygame.draw.rect(screen, BOARD_NUMBERS_COLOR[n], (BOARD_NUMBERS_X[n], BOARD_NUMBERS_Y[n], BOARD_NUMBERS_WIDTH, BOARD_NUMBERS_HEIGHT))
    #pygame.draw.rect(screen, OUTSIDE_COLOR, OUTSIDE_RECT)

    pygame.display.flip()

    color_cycle = 0

    number_status = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10]
    numbers_left = 75
    random_ball = 0
    random_flag = 0



    while running:

        #Clear screen
        pygame.draw.rect(screen, (0,255,0),(0,0,800,600))

        if (random_flag == 0):
            random_ball = random.randint(1,75)
        else:
            random_flag += 1
            if (random_flag >= 40):
                random_flag = 0

        
        for n in range(0,75,1):
            if (number_status[n] == 0):
                BOARD_NUMBERS_COLOR[n] = (0,0,0)
            elif (number_status[n] < 10):
                BOARD_NUMBERS_COLOR[n] = (255 * (number_status[n] % 2),255 * (number_status[n] % 2),255 * (number_status[n] % 2))
            else:
                BOARD_NUMBERS_COLOR[n] = (255,255,0)
            #BOARD_NUMBERS_COLOR[n] = ((int((n/75)*255)+color_cycle) % 256, (int((n/75)*255)+color_cycle) % 256,0)

    
        pygame.draw.rect(screen, OUTSIDE_COLOR, OUTSIDE_RECT)
        pygame.draw.rect(screen, INSIDE_COLOR,INSIDE_RECT)
        pygame.draw.rect(screen, LETTERS_COLOR, LETTERS_RECT)


        for n in range(0,75,1):
            pygame.draw.rect(screen, BOARD_NUMBERS_COLOR[n], (BOARD_NUMBERS_X[n], BOARD_NUMBERS_Y[n], BOARD_NUMBERS_WIDTH, BOARD_NUMBERS_HEIGHT))

            number_text_shadow = number_font.render(str(n+1), True, (0,0,0))
            number_text = number_font.render(str(n+1), True, (100,100,100))

            NUMBER_POS_X = BOARD_NUMBERS_X[n] + (BOARD_NUMBERS_WIDTH - number_text.get_width()) / 2
            NUMBER_POS_Y = BOARD_NUMBERS_Y[n] + (BOARD_NUMBERS_HEIGHT - number_text.get_height()) / 2

            screen.blit(number_text_shadow, (NUMBER_POS_X+2, NUMBER_POS_Y+2))
            screen.blit(number_text, (NUMBER_POS_X, NUMBER_POS_Y))

            if (n < 5):
                letter_text = letter_font.render(BOARD_LETTERS[n], True, (255,0,0))

                LETTER_POS_X = BOARD_LETTERS_X  + (BOARD_NUMBERS_WIDTH - letter_text.get_width()) / 2
                LETTER_POS_Y = BOARD_LETTERS_Y[n] + (BOARD_NUMBERS_HEIGHT - letter_text.get_height()) / 2
                
                screen.blit(letter_text, (LETTER_POS_X, LETTER_POS_Y))

                    

        pygame.draw.rect(screen, OUTSIDE_COLOR, HOPPER_OUTSIDE_RECT)
        pygame.draw.rect(screen, INSIDE_COLOR, HOPPER_INSIDE_RECT)
        screen.blit(hopper_letters_graphic, (HOPPER_LETTERS_X, HOPPER_LETTERS_Y))

        for n in range(0,5,1):
            inactive_letter_text = letter_font.render(BOARD_LETTERS[n], True, (50,50,50))
            active_letter_text = letter_font.render(BOARD_LETTERS[n], True, (255,255,0))

            if (int(random_ball/15) == n):
                HOPPER_LETTER_POS_X = HOPPER_IND_LETTERS_X[n] + (HOPPER_IND_LETTERS_WIDTH - active_letter_text.get_width()) / 2
                HOPPER_LETTER_POS_Y = HOPPER_IND_LETTERS_Y + (HOPPER_IND_LETTERS_HEIGHT - active_letter_text.get_height()) / 2

                screen.blit(active_letter_text, (HOPPER_LETTER_POS_X, HOPPER_LETTER_POS_Y))
            else:
                HOPPER_LETTER_POS_X = HOPPER_IND_LETTERS_X[n] + (HOPPER_IND_LETTERS_WIDTH - inactive_letter_text.get_width()) / 2
                HOPPER_LETTER_POS_Y = HOPPER_IND_LETTERS_Y + (HOPPER_IND_LETTERS_HEIGHT - inactive_letter_text.get_height()) / 2

                screen.blit(inactive_letter_text, (HOPPER_LETTER_POS_X, HOPPER_LETTER_POS_Y))

        tens = int((random_ball+1) / 10)
        ones = (random_ball+1) % 10

        HOPPER_TENS_RECT =(HOPPER_IND_NUMBERS_X[tens], HOPPER_IND_NUMBERS_Y, HOPPER_IND_NUMBERS_WIDTH, HOPPER_IND_NUMBERS_HEIGHT)
        HOPPER_ONES_RECT =(HOPPER_IND_NUMBERS_X[ones], HOPPER_IND_NUMBERS_Y, HOPPER_IND_NUMBERS_WIDTH, HOPPER_IND_NUMBERS_HEIGHT)
        
        screen.blit(hopper_numbers_graphic, (HOPPER_NUMBERS_X[0], HOPPER_NUMBERS_Y), HOPPER_TENS_RECT)
        screen.blit(hopper_numbers_graphic, (HOPPER_NUMBERS_X[1], HOPPER_NUMBERS_Y), HOPPER_ONES_RECT)


        pygame.display.flip()

        time.sleep(.1)

        color_cycle += 1
        if (color_cycle > 255):
            color_cycle = 0

        for n in range(0,75,1):
            if (number_status[n] > 0 and number_status[n] < 10):
                number_status[n] += 1
            elif (number_status[n] >= 10):
                number_status[n] = 10

                

        
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_b):
                    ball_chosen = 75
                    while number_status[ball_chosen] > 0 and numbers_left > 0:
                        ball_chosen = random.randint(0,74)
                        print ("Ball Chosen: "+str(ball_chosen)+", Status is "+ str(number_status[ball_chosen]) + ", "+ str(numbers_left) + " numbers left")

                    if (number_status[ball_chosen] == 0):
                        number_status[ball_chosen] += 1
                        numbers_left -= 1
                        
                        random_flag += 1
                        random_ball = ball_chosen

                    
                if (event.key == pygame.K_ESCAPE):
                    running = False
                    pygame.quit()
                    #sys.exit()
                    

main()
