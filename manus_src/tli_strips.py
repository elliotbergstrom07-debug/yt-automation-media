SM="Smithsonian Magazine, 'What's the longest you can hold your breath?'"
STRIPS = {
 6: ("trained free divers have gone as deep as 700 feet on one breath", SM),
 10: ("rarely, hiccups can go on for months", "Mayo Clinic, 'Hiccups'"),
 15: ("a clock's second hand can seem to stand still when you first look at it", "Wikipedia, 'Chronostasis'"),
 20: ("pre-breathing pure oxygen before a hold is 'a bit of a trick'", "Ohio State Wexner Medical Center, Dr. Jonathan Parsons"),
 24: ("light already on its way could reach you for up to 8 minutes after time stopped", "Discovery, 'What Would Happen If You Stopped Time?'"),
 29: ("with pure oxygen first, a diver held 20 min 21 s in 2010", "Scientific American, 'Breath-holding: the diving reflex'"),
 32: ("the record before 2021: 24:03.45, Barcelona, 2016", "Guinness World Records"),
 35: ("2024: 858 bicyclist deaths in urban areas, 200 in rural", "IIHS, 'Fatality Facts 2024: Bicyclists'"),
 37: ("with ABS: practice NOT pumping the brake", "NHTSA, 'Antilock Brake Systems (ABS)'"),
 45: ("in winter, increase your following distance", "NHTSA, 'Winter Driving Tips'"),
 48: ("relativity: satellite clocks lose 7 µs a day to speed, gain 45 µs to weaker gravity", "Ohio State University, Prof. Richard Pogge"),
 54: ("1971: four cesium-beam clocks flew on regular airline flights", "HyperPhysics, Georgia State University"),
 56: ("uncorrected GPS would be wrong after only 2 minutes", "Ohio State University, Prof. Richard Pogge"),
 60: ("predicted in 1971: −40 ns flying east, +275 ns flying west", "Hafele & Keating, Science (1972), via HyperPhysics"),
 64: ("NYC health code requires pool signs warning against hyperventilating", "CDC, MMWR Vol. 64, No. 19 (2015)"),
 77: ("15 of those 16 incidents happened at New York State bathing facilities", "CDC, MMWR Erratum (2015)"),
 80: ("diving reflex: blood vessels in skin and limbs narrow, saving blood for the core", "Scientific American, 'Breath-holding: the diving reflex'"),
 83: ("divers with experience can strengthen the reflex (2000 study)", "Scientific American, 'Breath-holding: the diving reflex'"),
 90: ("hiccup sound: your vocal cords closing suddenly", "Mayo Clinic, 'Hiccups'"),
}
CUT = set()
CLOSE = set()
CLOSE_T = {}
NG="National Geographic, 'What is black ice?' (2026)"
NWS="National Weather Service, 'Ice Storms' safety page"
STRIPS.update({
 90: ("most black ice forms when temperatures hover around freezing", NG),
 95: ("black ice: a thin, clear layer of ice on dark asphalt", NG),
 97: ("bridges and overpasses freeze before other surfaces", NWS),
 99: ("a single vehicle rated 26,001 lb or more needs a commercial license", "FMCSA, 'Commercial Driver's License: Drivers'"),
 103: ("cold water on the face: the airway snaps shut, the diving reflex begins", "Scientific American, 'Breath-holding: the diving reflex'"),
 108: ("black ice is often clear, with the black road visible underneath", NWS),
 111: ("black ice also forms on sidewalks, steps and decks", NG),
 113: ("underpasses shade the road and keep it from warming", NG),
 115: ("black ice is most common in the early morning hours", NWS),
 117: ("the 24:37 record was set in Sisak, Croatia, on 27 March 2021", "Guinness World Records"),
})
CLOSE = {31, 44, 84, 108, 118}
CLOSE_T = {31: "0:30", 44: "MY NAME", 84: "NO AIR", 108: "TOO HEAVY", 118: "4 MINUTES"}
