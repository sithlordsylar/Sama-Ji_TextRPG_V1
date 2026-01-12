import random
from temples import TempleFactory
from realms import RealmFactory
from combat import start_final_combat
from lore import KUNJUS

class Game:
    def __init__(self):
        self.temples = [TempleFactory.create(k) for k in KUNJUS]
        self.visited = []
        self.cards = []
        self.inventory = []

    def main_menu(self):
        while True:
            print("---------------------------------------------------------")
            print("The Sama-Ji Scroll: Arena 69")
            print("Welcome to Sama-Ji Text RPG. Inspired by the legendary Zork")
            print("This game is developed in Python by the Left Hand of Sama-Ji \nto choose the right Vessel for Sama-Ji's Return!")
            print("By utilizing the latest technology of Earth-1218 of the 3rd Dimension \nWe managed to simulate and experience 0.00000069% of Sama-Ji's greatness")
            print("Owh Yeah!")
            print("---------------------------------------------------------")
            print("1) Start Game")
            print("2) How to Play")
            print("3) Exit")
            choice = input("Choose an option (1-3): ").strip()
            if choice == '1':
                self.start()
                break
            elif choice == '2':
                self.show_help()
            elif choice == '3':
                print("Goodbye!")
                exit()
            else:
                print("Invalid choice.")

    def show_help(self):
        print("\n--- How to Play ---")
        print("Use commands to interact with environments:")
        print(" - move <direction> (or 'go')")
        print(" - inspect <object> (or 'look', 'look around', 'read')")
        print(" - take <item> (or 'get')")
        print(" - use <item>")
        print(" - solve <puzzle> (or 'unlock', 'open')")
        print(" - inventory (or 'inv') to view inventory")
        print(" - enter to pass through opened doors or portals")
        print(" - help (or '?') to show this message anytime")
        print("\nPress Enter to return to menu...")
        input()

    def start(self):
        print("---------------------------------------------------------")
        print("You find yourself in a featureless and infinitely expanding white room.")
        print("A single door stands before you with two gigantic statue on it's each side")
        print("On the right of the door stands a Hot Cat-Girl in maid outfit")
        print("On the left of the door stands a Hot Anubis Mommy stands seductively")
        print("Beside the Hot Cat-Girl affixed an old wooden sign")
        print("In the otherwise empty space, a tiny hole, about 5 cm across, floats in mid-air. MENACINGLY. ゴゴゴ")
        sign_read = False
        while True:
            cmd = input("\nWhat do you do? ").strip().lower()
            if cmd in ('read sign', 'inspect sign', 'look sign'):
                print("The sign reads: 'Life is like a blank canvas, you paint what you want to show.'")
                print("There's a subtitle in the sign that reads:\n'Here are some basic interaction mechanics of the game'")
                self.show_help()
                sign_read = True
            elif cmd in ('open door', 'enter door', 'open'):
                if not sign_read:
                    print("Is it safe? I better read the sign.")
                else:
                    print("You push the door open and step through...")
                    break
            elif cmd in ('inspect door', 'look door'):
                print("A divine aura radiates from within; your soul feels drawn toward it.")
            elif cmd in ('inspect cat', 'look cat', 'inspect cat girl', 'inspect cat-girl'):
                print("A Plaque Reads 'Divine Statue of Catto Waifu. Dedicated to the Kunju; Rishi D. Owh Yeah. The all-loving heart of Sama-Ji'")
                print("uWu the Cat-Girl-Goddess Making me feel 'uWu-fied'. I better control myself")
            elif cmd in ('inspect anubis', 'look anubis', 'inspect mommy', 'inspect mommy'):
                print("A Plaque Reads 'Divine Statue of Anubis Mommy. Dedicated to the Kunju; Mob Siva. The Body of Sama-Ji – The source of Strength and Defense.'")
                print("'Woof Woof' Did you just barked? Boy calm yourself.")       
            elif cmd in ('inspect hole', 'look hole'):
                print("There's something about this hole, it makes me feel funny and should I...")
                self.hole_interaction()
            elif cmd in ('look around', 'look', 'inspect room'):
                print("The white walls stretch endlessly; only the door, two great waifu statues, the sign, and the floating hole occupy the room.")
            elif cmd in ('help', '?'):
                self.show_help()
            else:
                print("Unknown command. (type 'help')")
        self.play_temple_sequence()

    def hole_interaction(self):
        while True:
            choice = input("\nOptions: look closer / give in to intrusive thoughts / leave\n> ").strip().lower()
            if choice == 'leave':
                print("You realize staring at the hole gives your boner, confused, you step back, refocusing on the door and sign.")
                return
            elif choice in ('look closer', 'look closer at hole'):
                print("You walk closer and realize you're getting harder… 'No!' You said \n'KANDARA KAWASAKI!' \nyou shouted and the voices stopped")
                print("You awaken back in the white room, dizzy but unharmed.")
                return
            elif choice in ('give in', 'give in to intrusive thoughts'):
                sub = input("\nOptions: lick it / do it\n> ").strip().lower()
                if sub == 'lick it':
                    print("You kneel… a stream of white liquid gushes.\nYou choke as you swallow the thick white liquid \n'That's a good Bitch' Says an Evil voice 'Zehahaha' it laughs\n you fainted.")
                    print("You awaken back in the white room, you felt wrong")
                    return
                elif sub == 'do it':
                    print("You walk closer and realize you're getting harder… \nyou realize what you have to do, your instinct don't lie \nYou got on your knees and your sight is fixed on the hole \nIt makes you drool, makes you feel-naughty")
                    input()
                    print("A voice from the hole says 'Who's a dirty bitch' \n'I am' you replied as you lick the hole /nAs ecstacy fills you and the hole moans louder.")
                    print("You give in to your primordial instinct and rip open your pants \nYou connect your hard rod into the hold \nIt's so tight but slippery \nYou feel pleasure")
                    input()
                    print("Suddenly you're overwhelmed with a sick vision \nYou see yourself as the great Kandara Kawasaki; Ste'vi 'Ra \nYou Realized you fell for his temptation")
                    input()
                    print("The voice echoes in your head laughing and saying 'You have given Dato a Rim Job! Zehahahaha!' \nThen the vision of the great Annunaki War fills your head \nYou see the men dying, not just the Men but the Women and Children too! \nYou slaid them like animals")
                    input()
                    print("Your vision changed, now you're Rudolph Hitla! \nYou witness the genocide of Juice Box People \nYou laugh as the boxes get flattened \nTheir snipped-tipped-straws being thrown into Oceans \nA Great Disaster")
                    input()
                    print("You can't take it no more! \n'Please Stop! I yield! I yield!' You screamed \n'Scream and Cream you bitch!' says Ste'Vi 'Ra \nSuddenly a loud divine voice boomed 'KANDARA KAWASAKI! UMBE!' \nSte'Vi 'Ra is silenced")
                    print("Everything becomes black. Your soul feels lighter.")
                    input()
                    print("You awaken back in the white room, dizzy but unharmed. Sama-Ji saved your kunju!")
                    return
                else:
                    print("Invalid choice.")
            else:
                print("Invalid option.")

    def play_temple_sequence(self):
        for temple in random.sample(self.temples, len(self.temples)):
            self.visited.append(temple.name)
            self.enter_area(temple, is_temple=True)
            if temple.card_collected:
                self.cards.append(temple.name)
                realm = RealmFactory.create(temple.name)
                self.enter_area(realm, is_temple=False)
            else:
                print(f"You leave the Temple of {temple.name} without its card.")
        self.ascend()
        self.final_challenge()

    def enter_area(self, area_obj, is_temple):
        # unified setup call
        area_obj.setup(self.inventory)
        print(f"\n--- Entering {'Temple' if is_temple else 'Realm'} of {area_obj.name} ---")
        print(area_obj.describe_current())

        while True:
            parts = input("> ").strip().lower().split()
            if not parts:
                continue
            verb, *args = parts
            moved = False

            if verb in ('move', 'go'):
                area_obj.move(args)
                moved = True

            elif verb in ('inspect', 'look'):
                if not args:
                    print(area_obj.describe_current())
                else:
                    area_obj.inspect(args, self.inventory)

            elif verb in ('take', 'get'):
                item = area_obj.take(args, self.inventory)
                if item:
                    print(f"You take the {item}.")

            elif verb == 'use':
                area_obj.use(args, self.inventory)

            elif verb in ('solve', 'unlock', 'open'):
                area_obj.solve_puzzle(args, self.inventory)

            elif verb in ('inventory', 'inv'):
                print("Inventory:", self.inventory or "(empty)")

            elif verb == 'enter':
                if area_obj.can_exit():
                    print(f"You pass through the threshold of {area_obj.name}.")
                    print(f"You depart the {'Temple' if is_temple else 'Realm'} of {area_obj.name}.")
                    break
                else:
                    print("You cannot enter yet.")

            elif verb in ('help', '?'):
                self.show_help()

            else:
                print("Unknown command. (type 'help')")

            if moved:
                print(area_obj.describe_current())

    def ascend(self):
        print("\nAs you collect the final Kunju card, a surge of power flows through you.")
        print("You have absorbed the essence of the Kunjus and become one with Sama-Ji.")

    def final_challenge(self):
        print("\n--- The Apex of Existence: Dimension 69 ---")
        print("The seal in Datorim has weakened—Ste'vi Ra and Veesus burst forth to challenge you!")
        start_final_combat(self.cards)

if __name__ == '__main__':
    Game().main_menu()



