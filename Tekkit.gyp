class item():

    def __init__(self, name, num=0):
        self.name = name
        self.num = num

def mirror(num):
    glass = 3*num
    sn_fe_al = num
    glass = 0.5*glass
    sn_fe_al = 0.5*sn_fe_al
    print(f"You need {glass} glass and,{sn_fe_al} tin/iron/aluminium ingots") 
    print(f"For {num} mirrors")
    print("\n")
    return

def piston(num):
    cobble = 4*num
    planks = 3*num
    iron = num
    redstone = num
    print(f"You need {cobble} cobble, {planks} wooden planks, {iron} iron ingots, and {redstone} redstone") 
    print(f"For {num} pistons")
    print("\n")

def quartz_block(num):
    nether_quartz = 4*num
    print(f"You need {nether_quartz} nether quartz")
    print(f"For {num} quartz blocks")
    print("\n")

def copper_block(num):
    copper = 9*num
    print(f"You need {copper} copper ingots") 
    print(f"For {num} copper blocks")
    print("\n")

def glowstone_block(num):
    glowstone = 4*num
    print(f"You need {glowstone} glowstone")
    print(f"For {num} glowstone blocks")
    print("\n")

def iron_block(num):
    iron = 9*num
    print(f"You need {iron} ingots")
    print(f"For {num} iron blocks")
    print("\n")

def gold_block(num):
    gold = 9*num
    print(f"You need {gold} gold ingots")
    print(f"For {num} gold blocks")
    print("\n")

def diamond_block(num):
    diamond = 9*num
    print(f"You need {diamond} diamonds")
    print(f"For {num} diamond blocks")
    print("\n")

def stick(num):
    planks = 2*num
    planks = 0.25*planks
    print(f"You need {planks} wooden planks") 
    print(f"For {num} sticks")
    print("\n")

def redstone_torch(num):
    stick = num
    redstone = num
    print(f"You need {stick} sticks, and {redstone} redstone") 
    print(f"For {num} redstone torches")
    print("\n")

def redstone_repeater(num):
    stone = 3*num
    redstone_torch(2*num)
    redstone = num
    print(f"You need {stone} stone, and {redstone} redstone")
    print(f"For {num} redstone repeaters")
    print("\n")

def clock(num):
    gold = 4*num
    redstone = 1*num
    print(f"You need {gold} gold ingots, and {redstone} redstone")
    print(f"For {num} clocks")
    print("\n")

def redstone_lamp(num):
    redstone = 4*num
    glowstone_block(num)
    print(f"You need {redstone} redstone")
    print(f"For {num} redstone lamps")
    print("\n")

def pho_I(num):
    glass = 3*num
    lapis = 3*num
    mirror(3*num)
    print(f"You need {glass} glass, and {lapis} lapis lazuli") 
    print(f"For {num} photovoltaic cell I's")
    print("\n")

def pho_II(num):
    pho_I(num)
    mirror(2*num)
    lapis = 3*num
    clay = 3*num
    print(f"You need {lapis} lapis lazuli, and {clay}clay")
    print(f"For {num} photovoltaic cell II's")
    print("\n")

def pho_III(num):
    glass = 3*num
    glowstone = 3*num
    obsididan = 2*num
    pho_II(num)
    print(f"You need {glass} glass, {glowstone} glowstone dust, and {obsididan} obisdian")
    print(f"For {num} photovoltaic cell III's")
    print("\n")

def pho_IV(num):
    blaze_rod = 3*num
    glowstone = 2*num
    diamond_block(num)
    pho_III(num)
    quartz_block(2*num)
    print(f"You need {blaze_rod} blaze rods, and {glowstone} glowstone")
    print(f"For {num} photovoltaic cell IV's")
    print("\n")

def solar_I(num):
    planks = 5*num
    redstone = num
    mirror(3*num)
    print(f"You need {planks} wooden planks and {redstone} redstone") 
    print(f"For {num} solar I's")
    print("\n")

def solar_II(num):
    solar_I(8*num)
    piston(num)
    print(f"For {num} solar II's")
    print("\n")

def solar_III(num):
    solar_II(4*num)
    copper_block(num)
    redstone_repeater(num)
    pho_I(3*num)
    print(f"For {num} solar III's")
    print("\n")

def solar_IV(num):
    solar_III(4*num)
    iron_block(num)
    clock(num)
    pho_II(3*num)
    print(f"For {num} solar IV's")
    print("\n")

def solar_V(num):
    solar_IV(4*num)
    pho_III(3*num)
    gold_block(num)
    redstone_lamp(num)
    print(f"For {num} solar V's")
    print("\n")
    
def solar_VI(num):
    solar_V(4*num)
    redstone_lamp(num)
    diamond_block(num)
    pho_IV(3*num)
    print(f"For {num} solar VI's")
    print("\n")

def machine(energy_input):

    m_c_e = {
        "zero":2,
        "one":3,
        "two":5,
        "three":8,
        "four":13,
        "five":20,
        "six":33,
        "seven":53,
        "eight":85,
        "nine":137,
        "ten":219,
        "eleven":351,
        "twelve":562,
        "thirteen":900,
        "fourteen":1441,
        "fifteen":2305,
        "sixteen":3689
        }
    e_f = {
        "zero":3,
        "one":4,
        "two":7,
        "three":12,
        "four":19,
        "five":31,
        "six":50,
        "seven":80,
        "eight":128,
        "nine":206,
        "ten":329,
        "eleven":527,
        "twelve":844,
        "thirteen":1351
        }

    num = []
    m_c_e_mach = 3
    e_f_mach = 1

    for i in m_c_e and e_f:
        x = m_c_e[i]
        y = e_f[i]
        w = (m_c_e_mach*x)+(e_f_mach*y)
        if w <= energy_input:
            z = energy_input - w
            num.append("o")
        else:
            print(f"{z} power left")
            break   
    print(f"{len(num)-1} overclockers each")

if __name__ == "__main__":
    machine(energy_input=128)