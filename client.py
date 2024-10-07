import threading
import socket
from connection import *
import sys
import game_player
import time
from game_object import*
import pickle 
from game_player import *  
from battletest2 import *
lock=threading.Lock()   



class client:
    def __init__(self,ip,port):
        self.s=socket.socket()
        self.server_port=port
        self.server_ip=ip
        self.s.connect((self.server_ip,self.server_port))
        print("connected")  
        global username , password , email , end
        end=False

    def send_msg(self,msg):
        data_sent=send_by_size(self.s,msg)
        #print(data_sent)      

    def recieve_msg(self):
        server_reply=recv_by_size(self.s)   
        #print(server_reply)
        return server_reply
    
   

class user(client):
    def __init__(self,ip,port):
        super().__init__(ip,port)

    def sign_up(self):
        global username , password , email,server_reply
        if signup_password_text_input !=""and signup_username_text_input !="" and signup_email_text_input !="":
            print("passed if statement")    
            username=signup_username_text_input
            password=signup_password_text_input
            email=signup_email_text_input

            if username=="" or  password=="" or email==""and quit==False:
                username=input("enter username")
                password=input("enter password")
                email=input("enter email")
            self.send_msg("signup~"+username+"~"+password+"~"+email)

            server_reply=self.recieve_msg().decode()
            print(server_reply)
        else:
            server_reply="signup failed"
        
    def login(self):
        global username , password,server_reply
        if username_text_input !="" and password_text_input !="":
            
            username=username_text_input
            password=password_text_input 
            if username=="" or  password=="":
                username=input("enter username")
                password=input("enter password")
                
            print(username,password)
            with lock:
                self.send_msg("login~"+username+"~"+password)
                server_reply=self.recieve_msg()
                #print(server_reply)
                return server_reply
            
        else:
            server_reply="login failed"
            return"login failed"
            
        #print(server_reply)

#will work on this tommorow 
    def forgort_password(self): 
        username=input("enter username")
        self.send_msg("forgort_password~"+username)


    def msg_friend(self):# this needs to be fixed so messaging can work
        global end
        while not end:
            friend=input ("enter name of friend")
            while True:
                time.sleep(0.25)
                content=input("enter what you want to say to your friend")
                if content=="quit":
                    print("ended message send to that person")
                    bool=True  
                    break
                self.send_msg(("message~"+ username +"~"+friend+"~"+content))
            varify=input("do you want to fully close the app")
            if varify=="yes":
                end=True
                break

    def reciceve_messages(self):
        global end
        msg=""
        timeout_seconds = 5
        self.s.settimeout(timeout_seconds)
        while not end:
            if(end==True):
                    break
            try: 
                msg=recv_by_size(self.s)
            except Exception as e:
                print(e)
            
            if(len(msg)!=0):
                msg=game_player.messging_msg(msg)
                print(f"messesege recived from {msg.src_name.decode()}: {msg.message.decode()} ")
            
            


class game_client(user):
    def __init__(self,ip,port):
        global window
        super().__init__(ip,port)
        self.friends={}
        self.pokemons={}
        self.items={}
        self.server_messages={}
    def starter_screen(self,window,socket):
        try:
            pygame.init()
            global username_text_input, password_text_input
            # Set up the window
            window_width = 1280
            window_height = 720
            #window = pygame.display.set_mode((window_width, window_height))
            pygame.display.set_caption("Pokemon Battlegrounds")
            global active_input_rect,signup_confirm_password_input_rect,signup_email_input_rect,signup_password_input_rect,signup_username_input_rect,username_input_rect,password_input_rect
            global signup_confirm_password_input_text
            global signup_username_text_input
            global signup_password_text_input
            global signup_email_text_input
            # Define colors
            RED = (255, 0, 0)
            WHITE = (255, 255, 255)
            BLACK = (0, 0, 0)
            cyan = (0, 255, 255)    

            # Load and scale background images
            background_image = pygame.image.load('bk1.jpg')
            background_image = pygame.transform.scale(background_image, (window_width, window_height))
            login_background_image = pygame.image.load('lukario1.jpg')
            login_background_image = pygame.transform.scale(login_background_image, (window_width, window_height))

            # Define buttons
            button_width = 200
            button_height = 50
            button_x = window_width // 2 - button_width // 2
            button_y_start = window_height // 2 - 100

            signup_button_rect = pygame.Rect(button_x, button_y_start, button_width, button_height)
            play_button_rect = pygame.Rect(button_x, button_y_start + 60, button_width, button_height)
            quit_button_rect = pygame.Rect(button_x, button_y_start + 120, button_width, button_height)
            other_button_rect = pygame.Rect(button_x, button_y_start + 180, button_width, button_height)

            # Define button text
            font = pygame.font.Font(None, 36)
            signup_text = font.render("Sign Up", True, WHITE)
            play_text = font.render("Play Game", True, WHITE)
            quit_text = font.render("Quit", True, WHITE)
            other_text = font.render("Other", True, WHITE)

            # Define game title
            title_font = pygame.font.Font(None, 72)
            title_text = title_font.render("Pokemon Battlegrounds", True, RED)
            title_rect = title_text.get_rect(center=(window_width // 2, 100))

            # Define login screen elements
            username_font = pygame.font.Font(None, 36)
            password_font = pygame.font.Font(None, 36)
            username_text = username_font.render("Username:", True, WHITE)
            password_text = password_font.render("Password:", True, WHITE)
            username_input_rect = pygame.Rect(window_width // 2 - 150, window_height // 2 - 50, 300, 50)
            password_input_rect = pygame.Rect(window_width // 2 - 150, window_height // 2 + 50, 300, 50)
            back_button_rect = pygame.Rect(50, 50, 150, 50)
            login_button_rect = pygame.Rect(window_width // 2  -150, window_height // 2 + 150, 200, 50)

            login_text = font.render("Login", True, cyan)
            back_text = font.render("Back", True, WHITE)



            #signup stuff
            # Define sign-up screen elements
            signup_username_text = username_font.render("Username:", True, WHITE)
            signup_password_text = password_font.render("Password:", True, WHITE)
            signup_confirm_password_text = password_font.render("Confirm Password:", True, WHITE)
            signup_email_text = password_font.render("Email:", True, WHITE)
            var=(window_width // 2 - 150, window_height // 2-100)
            signup_username_input_rect = pygame.Rect(window_width // 2 - 150, window_height // 2 - 250, 300, 50)
            signup_password_input_rect = pygame.Rect(window_width // 2 - 150, window_height // 2-100, 300, 50)
            signup_confirm_password_input_rect = pygame.Rect(window_width // 2 - 150, window_height // 2 , 300, 50)
            signup_email_input_rect = pygame.Rect(window_width // 2 - 150, window_height // 2 + 100, 300, 50)
            global player_cords
            # Game loopri
            running = True
            show_signup_screen = False
            signup_username_text_input = ""
            signup_password_text_input = ""
            signup_confirm_password_text_input = ""
            signup_email_text_input = ""
            signup_text=font.render("signup", True, cyan)
            active_input_rect =None
            # Game loop
            signup_toserver_button_rect = pygame.Rect(window_width // 2  -150, window_height // 2 + 150, 200, 50)
            running = True
            show_login_screen = False
            username_text_input = ""
            password_text_input = ""
            while running:
                # Handle events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if show_login_screen:
                            if back_button_rect.collidepoint(mouse_pos):
                                show_login_screen = False
                                username_text_input = ""
                                password_text_input = ""
                            elif login_button_rect.collidepoint(mouse_pos):
                                # Handle login button click
                                print("Login button clicked")
                                print("sending username and password to server")
                                player_cords=self.login()
                                #print(player_cords)
                                if server_reply !="login failed" and server_reply !=b"login failed":
                                    login_text = font.render("Login successful", True, cyan)
                                    running = False
                                    username_input_text=""
                                    password_input_text=""
                                else:
                                    login_text = font.render("Login failed", True, cyan)
                                    username_input_text=""
                                    password_input_text=""

                            else:
                                # Handle login screen input
                                if username_input_rect.collidepoint(mouse_pos):
                                    username_text_input = ""
                                    active_input_rect = username_input_rect

                                elif password_input_rect.collidepoint(mouse_pos):
                                    password_text_input = ""
                                    active_input_rect = password_input_rect

                        elif show_signup_screen:
                            if signup_toserver_button_rect.collidepoint(mouse_pos):
                                print("signup button clicked")
                                self.sign_up()
                                if server_reply=="signup successful":
                                    signup_text = font.render("signup successful", True, cyan)
                                else:
                                    signup_text = font.render("signup failed", True, cyan)

                            elif back_button_rect.collidepoint(mouse_pos):
                                show_signup_screen = False
                                signup_username_text_input = ""
                                signup_password_text_input = ""
                                signup_confirm_password_text_input = ""
                                signup_email_text_input = ""
                            else:
                                # Handle sign-up screen input
                                if signup_username_input_rect.collidepoint(mouse_pos):
                                    signup_username_text_input = ""
                                    active_input_rect = signup_username_input_rect
                                elif signup_password_input_rect.collidepoint(mouse_pos):
                                    signup_password_text_input = ""
                                    active_input_rect = signup_password_input_rect
                                elif signup_confirm_password_input_rect.collidepoint(mouse_pos):
                                    signup_confirm_password_text_input = ""
                                    active_input_rect = signup_confirm_password_input_rect
                                elif signup_email_input_rect.collidepoint(mouse_pos):
                                    signup_email_text_input = ""
                                    active_input_rect = signup_email_input_rect




                        else:
                            if signup_button_rect.collidepoint(mouse_pos):
                                # Handle sign up button click
                                show_signup_screen = True
                            elif play_button_rect.collidepoint(mouse_pos):
                                # Show login screen
                                show_login_screen = True
                            elif quit_button_rect.collidepoint(mouse_pos):
                                # Handle quit button click
                                running = False
                                self.s.close()
                                sys.exit()
                            elif other_button_rect.collidepoint(mouse_pos):
                                # Handle other button click
                                print("Other button clicked")




                    elif event.type == pygame.KEYDOWN:
                        if show_login_screen:
                            if event.key == pygame.K_RETURN:
                                if active_input_rect == username_input_rect:
                                    print("Username:", username_text_input)
                                    #username_text_input = ""
                                elif active_input_rect == password_input_rect:
                                    print("Password:", password_text_input)
                                    #password_text_input = ""

                            if event.key == pygame.K_BACKSPACE:
                                if active_input_rect == username_input_rect:
                                    username_text_input = username_text_input[:-1]
                                else:
                                    password_text_input = password_text_input[:-1]
                            elif event.key != pygame.K_RETURN:
                                if active_input_rect == username_input_rect:
                                    username_text_input += event.unicode
                                else:
                                    password_text_input += event.unicode

                        elif show_signup_screen:
                            
                            if event.key == pygame.K_BACKSPACE:
                                if active_input_rect == signup_username_input_rect:
                                    signup_username_text_input = signup_username_text_input[:-1]
                                    
                                elif active_input_rect == signup_password_input_rect:
                                    
                                    signup_password_text_input = signup_password_text_input[:-1]

                                elif active_input_rect == signup_confirm_password_input_rect:
                                    signup_confirm_password_text_input = signup_confirm_password_text_input[:-1]
                                else:
                                    signup_email_text_input = signup_email_text_input[:-1]

                            elif event.key != pygame.K_RETURN:

                                if active_input_rect == signup_username_input_rect:
                                    signup_username_text_input += event.unicode
                                    
                                elif(active_input_rect == signup_password_input_rect):
                                    signup_password_text_input+= event.unicode

                                elif(active_input_rect == signup_confirm_password_input_rect):
                                    signup_confirm_password_text_input += event.unicode
                                elif(active_input_rect == signup_email_input_rect):
                                    signup_email_text_input += event.unicode



                # Clear the window
                if running:
                    window.fill(BLACK)

                if show_login_screen and running:
                    # Draw login screen
                    window.blit(login_background_image, (0, 0))
                    window.blit(username_text, (window_width // 2 - 150, window_height // 2 - 100))
                    window.blit(password_text, (window_width // 2 - 150, window_height // 2))

                    pygame.draw.rect(window, WHITE, username_input_rect, 2)
                    pygame.draw.rect(window, WHITE, password_input_rect, 2)


                    username_input_text = username_font.render(username_text_input, True, WHITE)
                    password_input_text = password_font.render(password_text_input, True, WHITE)


                    window.blit(username_input_text, (window_width // 2 - 140, window_height // 2 - 40))
                    window.blit(password_input_text, (window_width // 2 - 140, window_height // 2 + 60))
                    pygame.draw.rect(window, RED, back_button_rect)

                    pygame.draw.rect(window, WHITE, login_button_rect)
                    window.blit(login_text, (window_width // 2 - 100, window_height // 2 + 150))



                    window.blit(back_text, (60, 60))   

                elif show_signup_screen and running:
                    window.blit(login_background_image, (0, 0))
                    window.blit(signup_username_text, (window_width // 2 - 150, window_height // 2 - 250-50))
                    window.blit(signup_password_text, (window_width // 2 - 150, window_height // 2-100-50))
                    window.blit(signup_confirm_password_text, (window_width // 2 - 150, window_height // 2-50))
                    window.blit(signup_email_text, (window_width // 2 - 150, window_height // 2 + +50))

                    pygame.draw.rect(window, WHITE, signup_username_input_rect, 2)
                    pygame.draw.rect(window, WHITE, signup_password_input_rect, 2)
                    pygame.draw.rect(window, WHITE, signup_confirm_password_input_rect, 2)
                    pygame.draw.rect(window, WHITE, signup_email_input_rect, 2)


                    signup_username_input_text = username_font.render(signup_username_text_input, True, WHITE)
                    signup_password_input_text = password_font.render(signup_password_text_input, True, WHITE)
                    signup_confirm_password_input_text = password_font.render(signup_confirm_password_text_input, True, WHITE)
                    signup_email_input_text = username_font.render(signup_email_text_input, True, WHITE)    



                    window.blit(signup_username_input_text,  (window_width // 2 - 150, window_height // 2 - 250))
                    window.blit(signup_password_input_text, (window_width // 2 - 150, window_height // 2-100))
                    window.blit(signup_confirm_password_input_text, (window_width // 2 - 150, window_height // 2))
                    window.blit(signup_email_input_text, (window_width // 2 - 150, window_height // 2+100 ))
                    pygame.draw.rect(window, RED, back_button_rect)
                    pygame.draw.rect(window, RED,signup_toserver_button_rect)
                    window.blit(signup_text, (window_width // 2 - 100, window_height // 2 + 150))    
                    window.blit(back_text, (60, 60))      

                elif running:
                    # Draw main screen
                    window.blit(background_image, (0, 0))
                    pygame.draw.rect(window, RED, signup_button_rect)
                    pygame.draw.rect(window, RED, play_button_rect)
                    pygame.draw.rect(window, RED, quit_button_rect)
                    pygame.draw.rect(window, RED, other_button_rect)
                    window.blit(signup_text, (button_x + 50, button_y_start + 10))
                    window.blit(play_text, (button_x + 50, button_y_start + 70))
                    window.blit(quit_text, (button_x + 75, button_y_start + 130))
                    window.blit(other_text, (button_x + 50, button_y_start + 190))
                    window.blit(title_text, title_rect)

                # Update display
                if running:
                    pygame.display.flip()
        except KeyboardInterrupt as e:
            print(e)
            running = False
        # Quit PyGame

    def send_player_data(self):
        data="player_data~".encode()
        data+=pickle.dumps(self.game.player.player_data)
        data=self.send_msg(data)

        self.game.player.moved=False

    

    def recieve_data(self):
        global end
        timeout_seconds = 5
        self.s.settimeout(timeout_seconds)
        while not end:
            if(end==True):
                    break
            try: 
                with lock:
                    self.server_reply=recv_by_size(self.s)
                    try:
                        #print(self.server_reply)
                        self.server_reply=pickle.loads(self.server_reply) 
                        if type(self.server_reply)==player_position:
                            print(self.server_reply.__repr__())
                            self.game.update_other_players(self.game.other_players,self.server_reply.name,self.server_reply)
                        elif type(self.server_reply)==messging_msg:
                            textlist.append(f"from {self.server_reply.src_name.decode()} : {self.server_reply.message.decode()}")    

                        elif type(self.server_reply)==str or type(self.server_reply)==bytes:
                            reply=self.server_reply.split(b"~")
                            ans=self.handle_messages(self.server_reply)
                            if(ans!=None):
                                if ans=="yes":
                                    try:
                                    
                                        var=(f"query_responce~yes~{self.game.player.player_data.name.decode()}~{reply[1].decode()}").encode()
                                        data=send_by_size(self.s,var)
                                        print(data)
                                        print("sent yes")
                                    except Exception as e:
                                        #print(e)
                                        print("there was an exeption in sending msg ")
                                
                                if("load"in ans or "yes" in ans):
                                    global start_battle
                                    start_battle=True
                                    #self.game.load_battle()
                                print("the answer is",ans)
                                
                               
                                                                         

                    except Exception as e:
                        #print("error in handling data")
                        pass

            except Exception as e:
                pass
                #print("error in recieving data")
    def battle_request(self,player_name):
        #if abs(self.game.other_players[player_name].player_data.x_cord-self.game.player.player_data.x_cord)<=100:
        self.send_msg("battle_request~".encode()+self.game.player.player_data.name+ b"~"+ player_name)
            

    def draw_game_messages(self,message):
        myfont = pygame.font.SysFont("monospace", 30)

        # render text
        label = myfont.render(message, 3, (0,0,0))
        self.game.screen.blit(label, (0, 0))


    def draw_other_players(self):
        for player in self.game.other_players.values():
            self.game.sprite_group.draw()
            #needs work
        #self.game.other_players[]=pickle.loads(data)

    def handle_messages(self,server_reply):
        global textlist,saveText,battle_ended
        print(server_reply)
        if type(server_reply)==str:
            server_reply=server_reply.encode()

        reply=server_reply.split(b"~")
        if b"battle_query" in server_reply:
            textlist.append(server_reply.decode())
            var="do you want to battle with "+reply[1].decode()+" (yes/no)"
            textlist.append(var)
            self.print_msg_to_screen(var,(10,(count+1)*32))
            run=True
            saveText=""
            while run:
                if saveText=="yes" or saveText=="no ":
                    run=False
                    #print("finished loop")
                    break
            #recv from pygame the responce form the user
            #print("lol")
            return saveText
            

        elif b"query_responce" in server_reply:

            textlist.append(reply[1].decode()) 
            if reply[1].decode()=="yes":
                textlist.append("battle will start soon")
                return "loadbattle"
            else:
                textlist.append("player rejected battle request or already in battle")
                print("player rejected battle request or already in battle")
        elif b"won"in server_reply:
            textlist.append("you won the battle")
            battle_ended=True
        elif b"lost" in server_reply:
            textlist.append("you lost the battle")
            battle_ended=True




    def log_sent_print(self,msg):
        print("player sent:",msg)

    def log_received_print(self,msg):
        print("player recieved:",msg)

    def print_msg_to_screen(self,msg,cords,fromm=""):
        global user_text , ft_font
        textsurface = ft_font.render(fromm+msg, True, (255,255,255))
        self.game.screen.blit(textsurface, cords)
    
    def draw_messages_to_screen(self):
        global textlist
        global count
        maxim=max(0,len(textlist)-10)
        self.print_msg_to_screen("this is chat :",(5,50))
        count=1
        var=10
        for i in range(maxim,10+maxim):
            try:
                self.print_msg_to_screen(textlist[i],(5,var+count*32))  
            except:
                pass 
            count+=1  
    def run_commands(self,text):
        global enemy_name
        #print(text)
        if text[0]=="/":
            #print(text[1:7])
           #print(text[7])
            var=text[8:].encode()
            splitted=text.split("~")

            #print(splitted[1].encode() in self.game.other_players.keys())
            


            if text[1:7]=="battle" and text[7]=="~" and var in self.game.other_players.keys():
                enemy_name=splitted[1].encode()
                print("valid request")
                self.battle_request(text[8:].encode())
            elif "msg"in text and splitted[1].encode() in self.game.other_players.keys() :
               
                msg="message~"+self.game.player.player_data.name.decode()+"~"+splitted[1]+"~"+splitted[2]
                self.log_sent_print(msg)
                self.send_msg(msg)
                #print("message sent")
                

        
    def start_game(self): 
        #self.login()
        global window
        global start_battle
        start_battle=False
        print(player_cords)
        player_data=pickle.loads(player_cords)
        self.game=Game(player_data,window)
        #self.game.screen=window
        global input_rect,color_active,color_passive,user_text, saveText
        cords=(10,10)
        input_rect=pygame.Rect(200, 20, 140, 32)
        color_active=pygame.Color('lightskyblue3')
        color_passive=pygame.Color('gray15')
        global user_text , ft_font,textlist
        user_text = '' 
        global battle_ended
        battle_ended=False  
        ft_font = pygame.font.Font(None, 32)
        active=False
        textlist=[""]



        print(self.game.player.player_data.name)
        recv_thread=threading.Thread(target=self.recieve_data,daemon=True).start()
        running = True
        while running:
            try:
            
            
                if start_battle==True:
                    print("starting battle")
                    mainfunc(window)
                    start_battle=False
                    if not battle_ended:
                        self.send_msg(f"win~{self.game.player.player_data.name.decode()}".encode())

                    textlist.append("battle ended")
                    battle_ended=False
                    
            
                else:
                    try:
                        self.game.screen.fill((0, 0, 0))
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                self.send_msg(f"quit~{self.game.player.player_data.name}".encode())
                                
                                running = False
                                pygame.quit()
                                
                                sys.exit()
                                break
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if input_rect.collidepoint(event.pos):
                                    active = True
                                else:
                                    active = False
                            if event.type == pygame.KEYDOWN:
                                #print(event)
                                if event.key==pygame.K_RETURN:
                                    textlist.append(user_text)
                                    self.run_commands(user_text)
                                    saveText=user_text
                                    user_text=""
                                    #print(textlist)

                                elif active:
                                    if event.key == pygame.K_BACKSPACE:
                                        user_text=user_text[:-1]
                                    else:
                                        user_text += event.unicode
                    except Exception as e:
                        pass
    
                    
                    self.game.player.move(self.game.collision_objects) 
                    if(self.game.player.moved==True):
                        print("SENDING PLAYER DATA")
                        self.send_player_data()



                    moved=False
                    
                    # Draw everysprite and tile 
                    self.game.sprite_group.draw(self.game.player) 
                    

                    #render the messages on the screen
                    
                    self.draw_messages_to_screen()
                    if active:
                        color=color_active
                    else:
                        color=color_passive
                    self.print_msg_to_screen("enter input here:",(5,20))
                    pygame.draw.rect(self.game.screen, color, input_rect,2)
                    textsurface = ft_font.render(user_text, True, (255, 255, 255))
                    self.game.screen.blit(textsurface, (input_rect.x+5, input_rect.y+5))
                    input_rect.w = max(100, textsurface.get_width()+10)
                    #########

                # Update the display
                #print(self.game.clock.get_fps())
                pygame.display.flip()
                self.game.clock.tick(60)
            except KeyboardInterrupt as e:
                self.send_msg(f"quit~{self.game.player.player_data.name}".encode())
                self.s.close()
                print("client brutally closed")
                print(e)
                pass

        # Quit Pygame# Quit Pygame

        print("closed the game")
        pygame.quit()
        
def temp():
    while True:
        print('\n  1. start game ')
        print('\n  2. login')
        print('\n  3.sign_up')
        print('\n  4. message friend')
        print('\n  (5. some invalid data for testing)')
        var=input("enter hat you want to do ")
        if var=="1":
            clients.start_game()
        if var=="2":
            clients.login()
        if var=="3":
            clients.sign_up()
        if var=="4":
            print("enterd 4 ")
            print(clients.login())
            recv_thread=threading.Thread(target=clients.reciceve_messages).start()
            wrtie_thread=threading.Thread(target=clients.msg_friend).start()
            break
        if var=="5":
            print("sestion ended sucsesfully")      
    
    


if __name__ == "__main__":
    #client=client(port,ip)
    #for i in range (10):
        #client.send_msg(input("enter what you wnat to say"))
       # client.recieve_msg() 
    try:
        
        ip= sys.argv[1]
        port= int(sys.argv[2])
        print(ip,port)
    except:
        ip="127.0.0.1"
        port=1234      
        print("argv error")
    #user= user(ip,port)

    global gui
    gui=True
    clients=game_client(ip,port)
    username_text_input=""
    password_text_input=""
    signup_username_text_input=""
    signup_password_text_input=""
    signup_email_text_input=""

    pygame.init()
    global username , password,server_reply
    window_width = 1280
    window_height = 720
    username=None
    password=None
    window = pygame.display.set_mode((window_width, window_height))

    music_file = "game_music.mp3"
    pygame.mixer.music.load(music_file)

    # Play the music
    pygame.mixer.music.play()
    player_cords=None

    clients.starter_screen(window,clients.s)
    print("entered start game ")
    if player_cords is not None:
        clients.start_game()



            
        