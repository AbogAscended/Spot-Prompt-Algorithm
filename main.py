class Generation():
    def __init__(self, command):
        self.command = command
        self.basic_movement = ["go", "come", "move", "walk", "run", "bring", "take", "fetch", "carry", "deliver", "send", "transport", 
    "escort", "return", "head", "travel", "drive", "fly", "sail", "ride", "cycle", "push", "pull", "lift", 
    "drag", "climb", "jump", "skip", "crawl", "rush", "hurry", "advance", "retreat", "proceed", "follow", 
    "leave", "arrive", "depart", "exit", "enter", "approach", "circle", "cross", "navigate", "transfer", 
    "relocate", "shift", "mail", "ship", "race", "sprint", "dash", "wander", "stroll", "meander", "march", 
    "patrol", "tour", "visit", "step", "trot", "gallop", "glide", "slide", "roll", "rotate", "swing", 
    "parade", "commute", "trek", "hike", "descend", "ascend", "dive", "swim", "float", "paddle", "row", 
    "accelerate", "reverse", "back", "forward", "maneuver", "relocate", "evacuate", "migrate", "emigrate", 
    "immigrate", "stray", "deviate", "veer", "meet", "chase", "flee", "escape", "pursue", "track", 
    "traverse", "circumnavigate", "orbit", "pass", "overtake", "weave", "zigzag", "shuffle", "tiptoe", 
    "strut", "saunter", "roam", "rove", "cruise", "sneak", "slither", "hop", "leap", "vault", "scamper", 
    "scurry", "scuttle", "bolt", "dart", "bustle", "hasten", "speed", "zoom", "whisk", "ferry", "channel", 
    "direct", "guide", "lead", "steer", "pilot", "transmit", "convey", "haul", "tote", "lug", "schlep", 
    "move", "reposition", "align", "realign", "shift", "mobilize", "smuggle", "maneuver", "scoot", 
    "meander", "beeline", "advance", "disembark", "embark", "transfer"]
        self.arm_movement  = [
    "grab", "grasp", "clutch", "snatch", "seize", "hold", "catch", "pluck", "pick", "lift", 
    "carry", "haul", "tug", "pull", "drag", "tote", "lug", "schlep", "hoist", "heave", 
    "retrieve", "fetch", "collect", "gather", "scoop", "clasp", "clench", "grip", "snag", 
    "yank", "wrench", "draw", "extract", "remove", "take", "bring", "transfer", "shift", 
    "move", "reposition", "adjust", "maneuver", "handle", "transport", "convey", "deliver", 
    "pass", "hand", "throw", "toss", "fling", "hurl", "push", "press", "shove", "place", 
    "set", "drop", "release", "unload", "load", "stack", "arrange", "organize", "pack", 
    "unpack", "reach", "stretch", "extend", "swing", "wave", "shake", "wield", "brandish", 
    "point", "gesture", "signal", "pat", "tap", "stroke", "rub", "scratch", "poke", "prod", 
    "nudge", "fumble", "fidget", "juggle", "twist", "turn", "rotate", "spin", "flip", 
    "fold", "unfold", "bend", "straighten", "squeeze", "compress", "pinch", "pluck", 
    "tweak", "adjust", "align", "realign", "position", "rearrange", "manipulate", "operate", 
    "control", "guide", "steer", "direct", "lead", "pull", "push", "lift", "lower", "raise", 
    "drop", "catch", "hold", "release", "carry", "move", "shift", "transfer", "transport"]

    def getKeywords(self, command):
        