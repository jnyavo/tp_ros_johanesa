# tp_ros_johanesa
## ROS trajet carré

[![ROS](https://www.ros.org/wp-content/uploads/2013/10/rosorg-logo1.png)](https://www.ros.org/)


Ce projet consiste à publier la position d'un point effectuant une trajectoire carrée sur un topic ROS
 - Le mouvement peut être suivi sur rviz
 - Le mouvement s'arrête et continue en actionant le bouton


## Lancement

Le roslaunch peut être utilisé pour lancer depuis le workspace

```sh
roslaunch tp_ros_johanesa trajet_carre.launch
```

Avec rosrun

```sh
rosrun tp_ros_johanesa publisher.py
```
Ce projet necéssite le lancement de l'interface bouton <br>
Interface bouton : <br>
https://github.com/Kramoth/button_gui


