# vnav-knu2025
Компʼютерний зір для візуальної навігації 


## Оцінювання

якщо залік:

- 40 балів лаби 
- 40 балів курсовий проект
- 20 балів усне + конспект


іспит: 

- 40 балів лаби 
- 40 балів курсовий проект
- 20 балів усне + конспект


## Програма

### Механіка  (5 тижнів) 
1. Основи 3D геометрії **(2 лекції)**
3. Фізична модель квадрокоптера (**1 лекція**)
4. Автопілот. Знайомство з сенсорами, системами AHRS і EK3 в Ardupilot (**1 лекція**)
5. Автопілот. Знайомство з PID контролерами (**1 лекція**)
- **(*extra*)** Пошук оптимальних траекторій 

### Компʼютерний зір   (6 тижнів)
6. Основи проективної геометрії. Формування зображення 
7. Feature Detection and Tracking 
8. Епіполярні умови. Задача camera pose estimation 
9. RANSAC
10. Статистичні підходи в навігації: триангуляція, оцінка максимуму вірогідностей, bundle adjustment
- (***extra***) нелінійна оптимізація 
11. Візуально-інерційна одометрія

### SLAM   (2-3 тижні)
12. Bag-of-Words, Object detection 
13. SLAM на орієнтирах 
14. SLAM на Pose Graph Optimization 
- (***extra***) Обчислення на розріджених даних


### Лабораторні: 
1. встановлення Ubuntu, знайомство з терміналом, знайомство з Raspberry Pi 
2. встановлення ROS, знайомство з ROS (***під питанням***) 
	    АБО 
   знайомство з сенсорами коптера, Mavlink
3. керування коптером в Unity симуляторі (***під питанням***)
		AБО 
	оцінка положення з IMU
4. знайомство з Ardupilot. Аналіз польотних логів 
5. оптимізація траекторії коптера в Unity симуляторі (***під питанням***)
6. keypoints matching
7. camera pose estimation, RANSAC
8. bag of words, yolo
9. loop closures, slam
10. ORB-SLAM 3 (***під питанням***)
11. інтеграція з коптером: Mavlink, dronekit, etc 

### Курсовий проект: 
- аналіз датасету
- створення baseline моделей
- аналіз state-of-the-art підходів, робота з пейперами з використанням ChatGPT Deep Research або аналогів 
- імплементація деякого підходу 
- **презентація, демо на реальному коптері** (по можливості)



## References:


- основний ресурс: https://vnav.mit.edu/ 
- https://docs.google.com/document/d/14jM845S288DODpDoNj_TjYZv4jmoKlrkOq2PigPFUbI/edit?usp=sharing

- https://ardupilot.org/dev/docs/extended-kalman-filter.html#extended-kalman-filter
- https://www.ros.org/
- https://github.com/UZ-SLAMLab/ORB_SLAM3
- https://simondlevy.github.io/ekf-tutorial/
- https://github.com/simondlevy/TinyEKF/tree/master
