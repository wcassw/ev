from evapp import db

# create the database and the db table
db.create_all()

# insert data ####################################################
# db.session.add()

# Audi
car1 = Vehicle(1,"Audi","e-tron GT quattro (s)",106050, 93.4, 487, 420)
car2 = Vehicle(2,"Audi","e-tron GT RS (s)",145360, 93.4, 487, 405)
car3 = Vehicle(3,"Audi","Q4 e-tron, (V)",56780, 82, 490, 385)
car4 = Vehicle(4,"Audi","Q4 e-tron Sportback (V)",60735, 82, 511, 400)
car5 = Vehicle(5,"Audi","Q8 e-tron (V)",86400, 114, 582, 495)
db.session.add(car1) 
db.session.add(car2) 
db.session.add(car3) 
db.session.add(car4) 
db.session.add(car5) 

# BMW
car1 = Vehicle(1,"BMW","i3 (h four-seater)", 44695, 42, 308, 280 )
car2 = Vehicle(2,"BMW", "i4 (s)", 63565, 83.9, 589, 470)
car3 = Vehicle(3,"BMW", "i7 (s)", 135845, 105, 625, 510)
car4 = Vehicle(4,"BMW", "iX xDrive M Sport (V)", 124565, 115.5, 630, 505)
car5 = Vehicle(5,"BMW","iX1 (V)", 63995, 68, 440, 355)
db.session.add(car1) 
db.session.add(car2) 
db.session.add(car3) 
db.session.add(car4) 
db.session.add(car5)


"""

Citroën
C4 (x) €39,789, 50 kWh; 357 km (265 km);
E-Berlingo (u) €36,462, 50 kWh, 280 km (195 km);
Spacetourer (P) €42,181, 50 kW, 230 km (180 km).
Cupra
Born 58 (h) €40,920, 62 kWh, 424 km (350 km);
Born 77 (h) €50,780, 82 kWh, 548 km (450 km).
DS Automobiles
DS 3 Crossback E-Tense (x) €43,362, 50 kWh, 320 km (260 km).
Fiat
500e Action (h) €25,995, 24 kWh, 190 km (135 km);
Icon (h) €29,995, 42 kWh, 320 km (235 km);
Icon Convertible (h) €34,995, 42 kWh, 320 km (235 km).
Ford
Mustang Mach-E RWD Standard (x) €67,666, 75.7 kWh, 440 km (355 km);
Mustang Mach-E RWD Extended (x) €63,510, 98.7 kWh, 610 km (455 km);
Mustang Mach-E AWD Extended (x) €93,836, 98.7 kWh, 550 km (440 km).
Honda
Honda e (h) €29,995, 35.5 kWh, 222 km (170 km).
Hyundai
Ioniq5 (V) €39,995, 58 kWh, 384 km (295 km);
Ioniq5 (V) €48,495, 77.4 kWh, 507 km (390 km);
Kona 39 (x) €32,495, 42 kWh, 305 km (250 km);
Kona 64 (x) €39,995, 67.5 kWh, 484 km (395 km);
Ioniq6 (s) - to be launched late 2023
Jaguar
I-Pace (x) €80,380; 90 kWh, 470 km (380 km).
Jeep
Avenger (V).
Kia
EV6 (x) €54,300, 77.4 kWh, 528 km (410 km);
Niro (x) €44,990, 68 kWh, 460 km (380 km).
Lexus
UX 300e (x) €57,805, 54.3 kWh, 315 km (235 km).
Mazda
MX-30 (x) €42,090, 35.5 kWh, 200 km (170 km).
Mercedes Benz
EQE 300 (s) €85,295, 100 kWh, 622 km (515 km);
EQE 350 4MATIC (s) €92,645, 100 kWh, 579 km (500 km);
EQS 450+ (s) €135,245, 120 kWh, 743 km (640 km);
EQS 500 4MATIC (s) €86,710, 120 kWh, 683 km (605 km);
EQS SUV 450+ (V) €139,880, 120 kWh, 655 km (495 km);
EQS SUV 580 4MATIC (V) €168,265, 120 kWh, 594 km (485 km).
MG
MG4 Standard Range (h) €27,495, 51.1 kWh, 350 km (298 km);
MG4 Long Range (h) €35,345, 64 kWh, 450 km (363 km);
MG5 (e) €34,645, 61.1 kWh, 403 km (322 km);
ZS Standard Range(x) €31,995, 51.1 kWh, 320 km (265 km);
ZS Long Range (x) 72.6 kWh, 440 km (362 km).
Mini
Cooper (h, four-seater) €35,615, 33 kWh, 233 km (180 km).
Nissan
Ariya 63 (V), 66 kWh, 402 km (320 km)
Ariya 87 (V), 91 kWh, 519 km (445 km).
Leaf (h) €30,345, 40 kWh, 270 km (235 km);
Leaf e+ (h) €38,590, 62 kWh, 385 km (340 km).
Opel
Astra (h) Price to be announced, 54 kWh, 416 km (310 km);
Combo-e Life (u) €37,161, 50 kWh, 285 km (200 km);
Corsa (h) €34,818, 50 kWh, 337 km (285 km);
Mokka (x) €35,568, 50 kWh, 322 km (255 km);
Vivaro (u) €48,695, 50 kWh, 230 km, (180 km);
Zafira (u) €59,372, 75 kWh, 330 km, (260 km).
Peugeot
208 (h) €31,995, 50 kWh, 339 km (285 km);
2008 (V) €35,135, 50 kWh, 362 km (255 km);
e-Rifter (u) €37,565, 50 kWh, 274 km (195 km);
e-Combi (P) €49,030, 50 kWh, 225 km, (180 km).
Polestar
Polestar 2 Standard Range Single Motor (v) €53,205, 69 kWh, 473 km;
Polestar 2 Long Range Dual Motor (v) €65,921, 78 kWh, 483 km (390 km).
Porsche
Taycan (l) €96,080, 79.2 kWh, 432 km (410 km);
Taycan 4 Cross Turismo (e) €107,551, 93.4 kWh, 456 km (425 km);
Taycan Turbo S Cross Turismo (e) €182,506, 93.4 kWh, 419 km (385 km).
Renault
Zoe (h) €33,995, 54.7 kWh, 395 km (315 km);
Megane E-Tech 40 (x) €37,495, 40 kWh, 300 km (250 km);
Megane E-tech 60 (x) €41,995, 60 kWh, 450 km (335 km).
Skoda
Enyaq iV 60 (V) €44,369, 62 kWh, 397 km (330 km);
Enyaq iV 80 (V) €52,885, 82 kWh, 535 km (420 km).
Subaru
Solterra AWD (V) €49,995, 71.4 kWh, 465 km (355 km).
Tesla
Model 3 (s) €54,800, 60 kWh, 491 km (378 km);
Model 3 Long Range (s) €70,553, 82 kWh, 602 km (483 km);
Model 3 Performance (s) €75,177, 82 kWh, 547 km (459 km);
Model S (s) 95 kWh, 652 km;
Model S Plaid (s) 95 kWh, 637 km;
Model X (s) 95 kWh, 560 km (467 km);
Model X Plaid (s) 95 kWh, 536 km (451 km);
Model Y (s) €52,972, 60 kWh, 455 km (346 km);
Model Y Long Range (s) €74,478, 82 kWh, 542 km (434 km);
Model Y Performance (s) €79,478, 82 kWh, 513 km (418 km).
Toyota
bZ4X Sport (V) €50,000, 71.4 kWh, 516 km (370 km).
Volkswagen
ID.3 Life (h) €40,862, 58 kWh, 425 km (350 km);
ID.4 Life (V) €50,090, 82 kWh, 517 km (410 km);
ID.5 Life (V) €61,345, 82 kWh, 517 km (430 km).
Volvo
C40 Recharge Single (x) €62,515, 78 kWh, 531 km;
C40 Recharge Twin (x) €67,515, 78 kWh, 508 km;
XC40 Recharge Single (V) €61,715, 82 kWh, 515 km (385 km);
XC40 Recharge Twin (V) €64,920, 82 kWh, 500 km (380 km);
EX90 (7-seater V) €117,910, 111 kWh, 585 km (455 km).


"""

# commit the changes ############################################
db.session.commit()
