import random
common = 36932
rare = 50890
legendary = 51000

commonchance = 4282
tc = 102768
oc = 2581
#where oc represents the number of each "He Called Game" moment in packs#
mcc = 3015
#where mcc represents the number of each "Make the Stop" moment in packs #
rcc = 3445
#where rcc represents the number of each "Move the Chains" moment in packs#
ree = tc + oc * 4
ree2 = ree + mcc * 4

rarechance = 751
baserc = 6008
launchcodes = 563
lct = rarechance * 8
twomin = 314
twom = lct + launchcodes * 4
aftb = 501
aftbm = twom + twomin
ballhawk = 626
bhm = aftbm + aftb * 4
itt = 438
ittm = bhm + ballhawk * 4



def rolldice(min,max):
    print("Rolling dice...")
    number = random.randint(min,max)
    #print("Your number : {}".format(number))#
    if number <= common:
        print("You pulled 3 commons")
        num2 = random.randint(0,138932)
        #print("Your common card # is : {}".format(num2))
        if num2 <= commonchance:
            print("You pulled Christian Kirk")
        if commonchance < num2 <= commonchance*2:
            print("You pulled Russell Gage")
        if commonchance * 2 < num2 <= commonchance*3:
            print("You pulled Josh Allen")
        if commonchance * 3 < num2 <= commonchance * 4:
            print("You pulled Cam Newton")
        if commonchance * 4 < num2 <= commonchance * 5:
            print("You pulled Robby Anderson")
        if commonchance * 5 < num2 <= commonchance * 6:
            print("You pulled Damiere Byrd")
        if commonchance * 6 < num2 <= commonchance * 7:
            print("You pulled Joe Burrow")
        if commonchance * 7 < num2 <= commonchance * 8:
            print("You pulled Jarvis Landry")
        if commonchance * 8 < num2 <= commonchance * 9:
            print("You pulled Albert Okwuegbunam")
        if commonchance * 9 < num2 <= commonchance * 10:
            print("You pulled Dre'Mont Jones")
        if commonchance * 10 < num2 <= commonchance * 11:
            print("You pulled Javonte Williams")
        if commonchance * 11 < num2 <= commonchance * 12:
            print("You pulled Ka'imi Fairbairn")
        if commonchance * 12 < num2 <= commonchance * 13:
            print("You pulled Laquon Treadwell")
        if commonchance * 13 < num2 <= commonchance * 14:
            print("You pulled Alex Okafor")
        if commonchance * 14 < num2 <= commonchance * 15:
            print("You pulled Josh Gordon")
        if commonchance * 15 < num2 <= commonchance * 16:
            print("You pulled Hunter Renfrow")
        if commonchance * 16 < num2 <= commonchance * 17:
            print("You pulled Josh Palmer")
        if commonchance * 17 < num2 <= commonchance * 18:
            print("You pulled Alvin Kamara")
        if commonchance * 18 < num2 <= commonchance * 19:
            print("You pulled Riley Dixon")
        if commonchance * 19 < num2 <= commonchance * 20:
            print("You pulled Saquon Barkley")
        if commonchance * 20 < num2 <= commonchance * 21:
            print("You pulled Keelan Cole")
        if commonchance * 21 < num2 <= commonchance * 22:
            print("You pulled Zach Wilson")
        if commonchance * 22 < num2 <= commonchance * 23:
            print("You pulled Richard Sherman")
        if commonchance * 23 < num2 <= commonchance * 24:
            print("You pulled Tom Brady")

        if tc < num2 <= tc + oc:
            print("You pulled Denzel Ward (He Called Game)")
        if tc + oc < num2 <= tc + oc * 2:
            print("You pulled Randy Gregory (He Called Game)")
        if tc + oc * 2 < num2 <= tc + oc * 3:
            print("You pulled Nick Niemann (He Called Game")
        if tc + oc * 3 < num2 <= tc + oc * 4:
            print("You pulled Minnesota Vikings (He Called Game)")

        if ree < num2 <= tc + mcc:
            print("You pulled Jadeveon Clowney (Make the Stop)")
        if ree + mcc < num2 <= tc + mcc * 2:
            print("You pulled Tyrann Mathieu (Make the Stop)")
        if ree + mcc * 2 < num2 <= ree + mcc * 3:
            print("You pulled Leonard Floyd (Make the Stop)")
        if ree + mcc * 3 < num2 <= ree + mcc * 4:
            print("You pulled Landon Collins (Make the Stop)")

        if ree2 < num2 <= ree2 + rcc:
            print("You pulled Tyler Huntley (Move the Chains)")
        if ree2 + rcc < num2 <= ree2 + rcc * 2:
            print("You pulled DJ Moore (Move the Chains)")
        if ree2 + rcc * 2 < num2 <= ree2 + rcc * 3:
            print("You pulled Matthew Stafford (Move the Chains)")
        if ree2 + rcc * 3 < num2 <= ree2 + rcc * 4:
            print("You pulled Kyle Rudolph (Move the Chains)")

        num2 = random.randint(0, 138932)
        #print("Your common card # is : {}".format(num2))
        if num2 <= commonchance:
            print("You pulled Christian Kirk")
        if commonchance < num2 <= commonchance * 2:
            print("You pulled Russell Gage")
        if commonchance * 2 < num2 <= commonchance * 3:
            print("You pulled Josh Allen")
        if commonchance * 3 < num2 <= commonchance * 4:
            print("You pulled Cam Newton")
        if commonchance * 4 < num2 <= commonchance * 5:
            print("You pulled Robby Anderson")
        if commonchance * 5 < num2 <= commonchance * 6:
            print("You pulled Damiere Byrd")
        if commonchance * 6 < num2 <= commonchance * 7:
            print("You pulled Joe Burrow")
        if commonchance * 7 < num2 <= commonchance * 8:
            print("You pulled Jarvis Landry")
        if commonchance * 8 < num2 <= commonchance * 9:
            print("You pulled Albert Okwuegbunam")
        if commonchance * 9 < num2 <= commonchance * 10:
            print("You pulled Dre'Mont Jones")
        if commonchance * 10 < num2 <= commonchance * 11:
            print("You pulled Javonte Williams")
        if commonchance * 11 < num2 <= commonchance * 12:
            print("You pulled Ka'imi Fairbairn")
        if commonchance * 12 < num2 <= commonchance * 13:
            print("You pulled Laquon Treadwell")
        if commonchance * 13 < num2 <= commonchance * 14:
            print("You pulled Alex Okafor")
        if commonchance * 14 < num2 <= commonchance * 15:
            print("You pulled Josh Gordon")
        if commonchance * 15 < num2 <= commonchance * 16:
            print("You pulled Hunter Renfrow")
        if commonchance * 16 < num2 <= commonchance * 17:
            print("You pulled Josh Palmer")
        if commonchance * 17 < num2 <= commonchance * 18:
            print("You pulled Alvin Kamara")
        if commonchance * 18 < num2 <= commonchance * 19:
            print("You pulled Riley Dixon")
        if commonchance * 19 < num2 <= commonchance * 20:
            print("You pulled Saquon Barkley")
        if commonchance * 20 < num2 <= commonchance * 21:
            print("You pulled Keelan Cole")
        if commonchance * 21 < num2 <= commonchance * 22:
            print("You pulled Zach Wilson")
        if commonchance * 22 < num2 <= commonchance * 23:
            print("You pulled Richard Sherman")
        if commonchance * 23 < num2 <= commonchance * 24:
            print("You pulled Tom Brady")

        if tc < num2 <= tc + oc:
            print("You pulled Denzel Ward (He Called Game)")
        if tc + oc < num2 <= tc + oc * 2:
            print("You pulled Randy Gregory (He Called Game)")
        if tc + oc * 2 < num2 <= tc + oc * 3:
            print("You pulled Nick Niemann (He Called Game")
        if tc + oc * 3 < num2 <= tc + oc * 4:
            print("You pulled Minnesota Vikings (He Called Game)")

        if ree < num2 <= tc + mcc:
            print("You pulled Jadeveon Clowney (Make the Stop)")
        if ree + mcc < num2 <= tc + mcc * 2:
            print("You pulled Tyrann Mathieu (Make the Stop)")
        if ree + mcc * 2 < num2 <= ree + mcc * 3:
            print("You pulled Leonard Floyd (Make the Stop)")
        if ree + mcc * 3 < num2 <= ree + mcc * 4:
            print("You pulled Landon Collins (Make the Stop)")

        if ree2 < num2 <= ree2 + rcc:
            print("You pulled Tyler Huntley (Move the Chains)")
        if ree2 + rcc < num2 <= ree2 + rcc * 2:
            print("You pulled DJ Moore (Move the Chains)")
        if ree2 + rcc * 2 < num2 <= ree2 + rcc * 3:
            print("You pulled Matthew Stafford (Move the Chains)")
        if ree2 + rcc * 3 < num2 <= ree2 + rcc * 4:
            print("You pulled Kyle Rudolph (Move the Chains)")
        num2 = random.randint(0, 138932)
        #print("Your common card # is : {}".format(num2))
        if num2 <= commonchance:
            print("You pulled Christian Kirk")
        if commonchance < num2 <= commonchance * 2:
            print("You pulled Russell Gage")
        if commonchance * 2 < num2 <= commonchance * 3:
            print("You pulled Josh Allen")
        if commonchance * 3 < num2 <= commonchance * 4:
            print("You pulled Cam Newton")
        if commonchance * 4 < num2 <= commonchance * 5:
            print("You pulled Robby Anderson")
        if commonchance * 5 < num2 <= commonchance * 6:
            print("You pulled Damiere Byrd")
        if commonchance * 6 < num2 <= commonchance * 7:
            print("You pulled Joe Burrow")
        if commonchance * 7 < num2 <= commonchance * 8:
            print("You pulled Jarvis Landry")
        if commonchance * 8 < num2 <= commonchance * 9:
            print("You pulled Albert Okwuegbunam")
        if commonchance * 9 < num2 <= commonchance * 10:
            print("You pulled Dre'Mont Jones")
        if commonchance * 10 < num2 <= commonchance * 11:
            print("You pulled Javonte Williams")
        if commonchance * 11 < num2 <= commonchance * 12:
            print("You pulled Ka'imi Fairbairn")
        if commonchance * 12 < num2 <= commonchance * 13:
            print("You pulled Laquon Treadwell")
        if commonchance * 13 < num2 <= commonchance * 14:
            print("You pulled Alex Okafor")
        if commonchance * 14 < num2 <= commonchance * 15:
            print("You pulled Josh Gordon")
        if commonchance * 15 < num2 <= commonchance * 16:
            print("You pulled Hunter Renfrow")
        if commonchance * 16 < num2 <= commonchance * 17:
            print("You pulled Josh Palmer")
        if commonchance * 17 < num2 <= commonchance * 18:
            print("You pulled Alvin Kamara")
        if commonchance * 18 < num2 <= commonchance * 19:
            print("You pulled Riley Dixon")
        if commonchance * 19 < num2 <= commonchance * 20:
            print("You pulled Saquon Barkley")
        if commonchance * 20 < num2 <= commonchance * 21:
            print("You pulled Keelan Cole")
        if commonchance * 21 < num2 <= commonchance * 22:
            print("You pulled Zach Wilson")
        if commonchance * 22 < num2 <= commonchance * 23:
            print("You pulled Richard Sherman")
        if commonchance * 23 < num2 <= commonchance * 24:
            print("You pulled Tom Brady")

        if tc < num2 <= tc + oc:
            print("You pulled Denzel Ward (He Called Game)")
        if tc + oc < num2 <= tc + oc * 2:
            print("You pulled Randy Gregory (He Called Game)")
        if tc + oc * 2 < num2 <= tc + oc * 3:
            print("You pulled Nick Niemann (He Called Game")
        if tc + oc * 3 < num2 <= tc + oc * 4:
            print("You pulled Minnesota Vikings (He Called Game)")

        if ree < num2 <= tc + mcc:
            print("You pulled Jadeveon Clowney (Make the Stop)")
        if ree + mcc < num2 <= tc + mcc * 2:
            print("You pulled Tyrann Mathieu (Make the Stop)")
        if ree + mcc * 2 < num2 <= ree + mcc * 3:
            print("You pulled Leonard Floyd (Make the Stop)")
        if ree + mcc * 3 < num2 <= ree + mcc * 4:
            print("You pulled Landon Collins (Make the Stop)")

        if ree2 < num2 <= ree2 + rcc:
            print("You pulled Tyler Huntley (Move the Chains)")
        if ree2 + rcc < num2 <= ree2 + rcc * 2:
            print("You pulled DJ Moore (Move the Chains)")
        if ree2 + rcc * 2 < num2 <= ree2 + rcc * 3:
            print("You pulled Matthew Stafford (Move the Chains)")
        if ree2 + rcc * 3 < num2 <= ree2 + rcc * 4:
            print("You pulled Kyle Rudolph (Move the Chains)")
    if common < number <= rare:
        print("You pulled 2 commons and a rare!")

        num2 = random.randint(0, 138932)
        # print("Your common card # is : {}".format(num2))
        if num2 <= commonchance:
            print("You pulled Christian Kirk")
        if commonchance < num2 <= commonchance * 2:
            print("You pulled Russell Gage")
        if commonchance * 2 < num2 <= commonchance * 3:
            print("You pulled Josh Allen")
        if commonchance * 3 < num2 <= commonchance * 4:
            print("You pulled Cam Newton")
        if commonchance * 4 < num2 <= commonchance * 5:
            print("You pulled Robby Anderson")
        if commonchance * 5 < num2 <= commonchance * 6:
            print("You pulled Damiere Byrd")
        if commonchance * 6 < num2 <= commonchance * 7:
            print("You pulled Joe Burrow")
        if commonchance * 7 < num2 <= commonchance * 8:
            print("You pulled Jarvis Landry")
        if commonchance * 8 < num2 <= commonchance * 9:
            print("You pulled Albert Okwuegbunam")
        if commonchance * 9 < num2 <= commonchance * 10:
            print("You pulled Dre'Mont Jones")
        if commonchance * 10 < num2 <= commonchance * 11:
            print("You pulled Javonte Williams")
        if commonchance * 11 < num2 <= commonchance * 12:
            print("You pulled Ka'imi Fairbairn")
        if commonchance * 12 < num2 <= commonchance * 13:
            print("You pulled Laquon Treadwell")
        if commonchance * 13 < num2 <= commonchance * 14:
            print("You pulled Alex Okafor")
        if commonchance * 14 < num2 <= commonchance * 15:
            print("You pulled Josh Gordon")
        if commonchance * 15 < num2 <= commonchance * 16:
            print("You pulled Hunter Renfrow")
        if commonchance * 16 < num2 <= commonchance * 17:
            print("You pulled Josh Palmer")
        if commonchance * 17 < num2 <= commonchance * 18:
            print("You pulled Alvin Kamara")
        if commonchance * 18 < num2 <= commonchance * 19:
            print("You pulled Riley Dixon")
        if commonchance * 19 < num2 <= commonchance * 20:
            print("You pulled Saquon Barkley")
        if commonchance * 20 < num2 <= commonchance * 21:
            print("You pulled Keelan Cole")
        if commonchance * 21 < num2 <= commonchance * 22:
            print("You pulled Zach Wilson")
        if commonchance * 22 < num2 <= commonchance * 23:
            print("You pulled Richard Sherman")
        if commonchance * 23 < num2 <= commonchance * 24:
            print("You pulled Tom Brady")

        if tc < num2 <= tc + oc:
            print("You pulled Denzel Ward (He Called Game)")
        if tc + oc < num2 <= tc + oc * 2:
            print("You pulled Randy Gregory (He Called Game)")
        if tc + oc * 2 < num2 <= tc + oc * 3:
            print("You pulled Nick Niemann (He Called Game")
        if tc + oc * 3 < num2 <= tc + oc * 4:
            print("You pulled Minnesota Vikings (He Called Game)")

        if ree < num2 <= tc + mcc:
            print("You pulled Jadeveon Clowney (Make the Stop)")
        if ree + mcc < num2 <= tc + mcc * 2:
            print("You pulled Tyrann Mathieu (Make the Stop)")
        if ree + mcc * 2 < num2 <= ree + mcc * 3:
            print("You pulled Leonard Floyd (Make the Stop)")
        if ree + mcc * 3 < num2 <= ree + mcc * 4:
            print("You pulled Landon Collins (Make the Stop)")

        if ree2 < num2 <= ree2 + rcc:
            print("You pulled Tyler Huntley (Move the Chains)")
        if ree2 + rcc < num2 <= ree2 + rcc * 2:
            print("You pulled DJ Moore (Move the Chains)")
        if ree2 + rcc * 2 < num2 <= ree2 + rcc * 3:
            print("You pulled Matthew Stafford (Move the Chains)")
        if ree2 + rcc * 3 < num2 <= ree2 + rcc * 4:
            print("You pulled Kyle Rudolph (Move the Chains)")
        num2 = random.randint(0, 138932)
       # print("Your common card # is : {}".format(num2))
        if num2 <= commonchance:
            print("You pulled Christian Kirk")
        if commonchance < num2 <= commonchance * 2:
            print("You pulled Russell Gage")
        if commonchance * 2 < num2 <= commonchance * 3:
            print("You pulled Josh Allen")
        if commonchance * 3 < num2 <= commonchance * 4:
            print("You pulled Cam Newton")
        if commonchance * 4 < num2 <= commonchance * 5:
            print("You pulled Robby Anderson")
        if commonchance * 5 < num2 <= commonchance * 6:
            print("You pulled Damiere Byrd")
        if commonchance * 6 < num2 <= commonchance * 7:
            print("You pulled Joe Burrow")
        if commonchance * 7 < num2 <= commonchance * 8:
            print("You pulled Jarvis Landry")
        if commonchance * 8 < num2 <= commonchance * 9:
            print("You pulled Albert Okwuegbunam")
        if commonchance * 9 < num2 <= commonchance * 10:
            print("You pulled Dre'Mont Jones")
        if commonchance * 10 < num2 <= commonchance * 11:
            print("You pulled Javonte Williams")
        if commonchance * 11 < num2 <= commonchance * 12:
            print("You pulled Ka'imi Fairbairn")
        if commonchance * 12 < num2 <= commonchance * 13:
            print("You pulled Laquon Treadwell")
        if commonchance * 13 < num2 <= commonchance * 14:
            print("You pulled Alex Okafor")
        if commonchance * 14 < num2 <= commonchance * 15:
            print("You pulled Josh Gordon")
        if commonchance * 15 < num2 <= commonchance * 16:
            print("You pulled Hunter Renfrow")
        if commonchance * 16 < num2 <= commonchance * 17:
            print("You pulled Josh Palmer")
        if commonchance * 17 < num2 <= commonchance * 18:
            print("You pulled Alvin Kamara")
        if commonchance * 18 < num2 <= commonchance * 19:
            print("You pulled Riley Dixon")
        if commonchance * 19 < num2 <= commonchance * 20:
            print("You pulled Saquon Barkley")
        if commonchance * 20 < num2 <= commonchance * 21:
            print("You pulled Keelan Cole")
        if commonchance * 21 < num2 <= commonchance * 22:
            print("You pulled Zach Wilson")
        if commonchance * 22 < num2 <= commonchance * 23:
            print("You pulled Richard Sherman")
        if commonchance * 23 < num2 <= commonchance * 24:
            print("You pulled Tom Brady")

        if tc < num2 <= tc + oc:
            print("You pulled Denzel Ward (He Called Game)")
        if tc + oc < num2 <= tc + oc * 2:
            print("You pulled Randy Gregory (He Called Game)")
        if tc + oc * 2 < num2 <= tc + oc * 3:
            print("You pulled Nick Niemann (He Called Game")
        if tc + oc * 3 < num2 <= tc + oc * 4:
            print("You pulled Minnesota Vikings (He Called Game)")

        if ree < num2 <= tc + mcc:
            print("You pulled Jadeveon Clowney (Make the Stop)")
        if ree + mcc < num2 <= tc + mcc * 2:
            print("You pulled Tyrann Mathieu (Make the Stop)")
        if ree + mcc * 2 < num2 <= ree + mcc * 3:
            print("You pulled Leonard Floyd (Make the Stop)")
        if ree + mcc * 3 < num2 <= ree + mcc * 4:
            print("You pulled Landon Collins (Make the Stop)")

        if ree2 < num2 <= ree2 + rcc:
            print("You pulled Tyler Huntley (Move the Chains)")
        if ree2 + rcc < num2 <= ree2 + rcc * 2:
            print("You pulled DJ Moore (Move the Chains)")
        if ree2 + rcc * 2 < num2 <= ree2 + rcc * 3:
            print("You pulled Matthew Stafford (Move the Chains)")
        if ree2 + rcc * 3 < num2 <= ree2 + rcc * 4:
            print("You pulled Kyle Rudolph (Move the Chains)")

        num3 = random.randint(0, 6008)
        #print("Your rare card # is : {}".format(num3))
        if num3 <= rarechance:
            print("You pulled Mark Andrews")
        if rarechance < num3 <= rarechance * 2:
            print("You pulled Myles Garrett")
        if rarechance * 2 < num3 <= rarechance * 3:
            print("You pulled Mike Hughes")
        if rarechance * 3 < num3 <= rarechance * 4:
            print("You pulled Marquez Callaway")
        if rarechance * 4 < num3 <= rarechance * 5:
            print("You pulled James Washington")
        if rarechance * 5 < num3 <= rarechance * 6:
            print("You pulled Rashaad Penny")
        if rarechance * 6 < num3 <= rarechance * 7:
            print("You pulled George Kittle")
        if rarechance * 7 < num3 <= rarechance * 8:
            print("You pulled Cam Sims")
        if lct < num3 <= lct + launchcodes:
            print("You pulled Patrick Mahomes")
        if lct + launchcodes < num3 <= lct + launchcodes * 2:
            print("You pulled Van Jefferson")
        if lct + launchcodes * 2 < num3 <= lct + launchcodes * 3:
            print("You pulled Kirk Cousins")
        if lct + launchcodes * 3 < num3 <= lct + launchcodes * 4:
            print("You pulled Tyler Lockett")
        if twom < num3 <= twom + twomin:
            print("You pulled Buffalo Bills")
        if aftbm < num3 <= aftbm + aftb:
            print("You pulled Jakeem Grant")
        if aftbm + aftbm < num3 <= aftbm + aftb * 2:
            print("You pulled Derrick Gore")
        if aftbm + aftbm * 2 < num3 <= aftbm + aftb * 3:
            print("You pulled Taysom Hill")
        if aftbm + aftbm * 3 < num3 <= aftbm + aftb * 4:
            print("You pulled Leonard Fournette")
        if bhm < num3 <= bhm + ballhawk:
            print("You pulled Mykal Walker")
        if bhm + ballhawk < num3 <= bhm + ballhawk * 2:
            print("You pulled Justin Simmons")
        if bhm + ballhawk * 2 < num3 <= bhm + ballhawk * 3:
            print("You pulled Rasul Douglas")
        if bhm + ballhawk * 3 < num3 <= bhm + ballhawk * 4:
            print("You pulled Cole Holcomb")
        if ittm < num3 <= itt + ittm:
            print("You pulled Micah Parsons")
        if itt + ittm < num3 <= itt + ittm * 2:
            print("You pulled Ali Marpet")

    if rare < number <= legendary:
        print("You pulled 2 commons and a legendary!!!")
        num2 = random.randint(0, 138932)
        print("Your common card # is : {}".format(num2))
        if num2 <= commonchance:
            print("You pulled Christian Kirk")
        if commonchance < num2 <= commonchance * 2:
            print("You pulled Russell Gage")
        if commonchance * 2 < num2 <= commonchance * 3:
            print("You pulled Josh Allen")
        if commonchance * 3 < num2 <= commonchance * 4:
            print("You pulled Cam Newton")
        if commonchance * 4 < num2 <= commonchance * 5:
            print("You pulled Robby Anderson")
        if commonchance * 5 < num2 <= commonchance * 6:
            print("You pulled Damiere Byrd")
        if commonchance * 6 < num2 <= commonchance * 7:
            print("You pulled Joe Burrow")
        if commonchance * 7 < num2 <= commonchance * 8:
            print("You pulled Jarvis Landry")
        if commonchance * 8 < num2 <= commonchance * 9:
            print("You pulled Albert Okwuegbunam")
        if commonchance * 9 < num2 <= commonchance * 10:
            print("You pulled Dre'Mont Jones")
        if commonchance * 10 < num2 <= commonchance * 11:
            print("You pulled Javonte Williams")
        if commonchance * 11 < num2 <= commonchance * 12:
            print("You pulled Ka'imi Fairbairn")
        if commonchance * 12 < num2 <= commonchance * 13:
            print("You pulled Laquon Treadwell")
        if commonchance * 13 < num2 <= commonchance * 14:
            print("You pulled Alex Okafor")
        if commonchance * 14 < num2 <= commonchance * 15:
            print("You pulled Josh Gordon")
        if commonchance * 15 < num2 <= commonchance * 16:
            print("You pulled Hunter Renfrow")
        if commonchance * 16 < num2 <= commonchance * 17:
            print("You pulled Josh Palmer")
        if commonchance * 17 < num2 <= commonchance * 18:
            print("You pulled Alvin Kamara")
        if commonchance * 18 < num2 <= commonchance * 19:
            print("You pulled Riley Dixon")
        if commonchance * 19 < num2 <= commonchance * 20:
            print("You pulled Saquon Barkley")
        if commonchance * 20 < num2 <= commonchance * 21:
            print("You pulled Keelan Cole")
        if commonchance * 21 < num2 <= commonchance * 22:
            print("You pulled Zach Wilson")
        if commonchance * 22 < num2 <= commonchance * 23:
            print("You pulled Richard Sherman")
        if commonchance * 23 < num2 <= commonchance * 24:
            print("You pulled Tom Brady")

        if tc < num2 <= tc + oc:
            print("You pulled Denzel Ward (He Called Game)")
        if tc + oc < num2 <= tc + oc * 2:
            print("You pulled Randy Gregory (He Called Game)")
        if tc + oc * 2 < num2 <= tc + oc * 3:
            print("You pulled Nick Niemann (He Called Game")
        if tc + oc * 3 < num2 <= tc + oc * 4:
            print("You pulled Minnesota Vikings (He Called Game)")

        if ree < num2 <= tc + mcc:
            print("You pulled Jadeveon Clowney (Make the Stop)")
        if ree + mcc < num2 <= tc + mcc * 2:
            print("You pulled Tyrann Mathieu (Make the Stop)")
        if ree + mcc * 2 < num2 <= ree + mcc * 3:
            print("You pulled Leonard Floyd (Make the Stop)")
        if ree + mcc * 3 < num2 <= ree + mcc * 4:
            print("You pulled Landon Collins (Make the Stop)")

        if ree2 < num2 <= ree2 + rcc:
            print("You pulled Tyler Huntley (Move the Chains)")
        if ree2 + rcc < num2 <= ree2 + rcc * 2:
            print("You pulled DJ Moore (Move the Chains)")
        if ree2 + rcc * 2 < num2 <= ree2 + rcc * 3:
            print("You pulled Matthew Stafford (Move the Chains)")
        if ree2 + rcc * 3 < num2 <= ree2 + rcc * 4:
            print("You pulled Kyle Rudolph (Move the Chains)")

rolldice(1,51000)


