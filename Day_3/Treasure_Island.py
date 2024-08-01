import random
import time 

def main():
    
    print("""
          
You awaken on a beach, your sand-covered body aches and protests with every movement. It has taken you a lot to get here. Your ship and your crew are both long gone, taken by the sea, but you have made it, after a lifetime of searching, to the famous...
          
          """
          """
      _____                                        _____     _                 _       
     /__   \_ __ ___  __ _ ___ _   _ _ __ ___      \_   \___| | __ _ _ __   __| |      
 _____ / /\/ '__/ _ \/ _` / __| | | | '__/ _ \      / /\/ __| |/ _` | '_ \ / _` |_____ 
|_____/ /  | | |  __/ (_| \__ \ |_| | | |  __/   /\/ /_ \__ \ | (_| | | | | (_| |_____|
      \/   |_|  \___|\__,_|___/\__,_|_|  \___|   \____/ |___/_|\__,_|_| |_|\__,_|      
                                                                                       
                                                                                       """)
    print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    #! START
    print("""
 You are standing on a beach. The white sands of the beach seem strangely smooth and empty as they stretch out around you. Further up the beach in front of you, you see palm trees sprouting, leading into a dense forest that covers the rest of the island.
          """)
    print()
    time.sleep(0.5)
    first_choice = input("Where do you want to go?  (Select The Number)\n"
                     "- - -\n"
                     "1: [Walk Down The Beach]\n"
                     "- - -\n"
                     "2: [Try To Swim Off The Island]\n"
                     "- - -\n"
                     "3: [Head Towards The Palm Trees]\n"
                     "- - -\n"
                     )
   
    #? Walk The Beach
    if first_choice == '1':
        print("""
You walk along the beach. The pounding of your footsteps in the sand and the rhythmic sound of the ocean create a steady tune that you lose track of time to. How long have you been walking? The beach remains featureless ahead of you.
              """)
        beach_march = input('Should you turn back or march on and hope to find the end of the beach?\n'
                            "- - -\n"
                            "1: [Keep Walking]\n"
                            "- - -\n"
                            "2: [Turn Back]\n"
                            "- - -\n"
                            "3 [Try To Swim Off The Island]\n"
                            "- - -\n"
                            )
        if beach_march == "1":
            pass
        
        elif beach_march == "2":
            pass
            
        elif beach_march == "3":    
            pass
        
        
        
        
    # Try To Swim 
    elif first_choice == '2':
        print("chpice 2")
        
    # Head To The Trees  
    elif first_choice == '3':
        print("choice 3")
                        
                         
if __name__ == '__main__':
    main()
 


