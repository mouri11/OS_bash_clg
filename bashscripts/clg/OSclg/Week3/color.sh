read -p "Enter foreground color: " foregrd
read -p "Enter background color: " bckgrd

setterm -term linux -back $bckgrd -fore $foregrd -clear
